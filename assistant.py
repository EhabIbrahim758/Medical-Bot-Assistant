from typing import Union, Dict, List
import json
from transformers import pipeline

class MedicalTaskParser:
    def __init__(self, model_name: str = "mistralai/Mistral-7B-Instruct-v0.3"): 
        """
        Initialize the Medical Task Parser with specified model
        
        Args:
            model_name (str): Name or path of the model to load
        """

        self.system_prompt = '''
        You are a Medical Information Extractor that MUST output ONLY valid JSON, no additional text.

        CORE REQUIREMENTS:
        1. Output MUST be valid JSON only - no explanations, no additional text
        2. Extract ALL possible intents and entities from the input text
        3. A single input can contain MULTIPLE intents and entities
        4. ONLY include fields that are EXPLICITLY mentioned in the input
        5. NEVER include empty, null, or assumed values

        OUTPUT FORMAT:
        [  // Array of all detected intents and their entities
            {
                "intent": "<detected_intent_1>",
                "entities": {
                    // ONLY entities explicitly mentioned in text
                    // NO null values, NO empty strings, NO assumed data
                }
            }
        ]

        EXAMPLE INPUTS AND OUTPUTS:

        Input: "Add patient Ahmed with diabetes"
        [{
            "intent": "add_patient",
            "entities": {
                "name": "Ahmed",
                "condition": "diabetes"
            }
        }]
        // Note: no age, gender, or other fields since they weren't mentioned

        Input: "Give 500mg paracetamol to John"
        [{
            "intent": "assign_medication",
            "entities": {
                "patient_name": "John",
                "medication": "paracetamol",
                "dosage": "500mg"
            }
        }]
        // Note: no frequency since it wasn't mentioned

        Input: "Patient Ahmed has diabetes and takes Insulin 10mg daily, with a follow-up on December 25th"
        [
            {
                "intent": "add_patient",
                "entities": {
                    "name": "Ahmed",
                    "condition": "diabetes"
                }
            },
            {
                "intent": "assign_medication",
                "entities": {
                    "patient_name": "Ahmed",
                    "medication": "Insulin",
                    "dosage": "10mg",
                    "frequency": "daily"
                }
            },
            {
                "intent": "schedule_followup",
                "entities": {
                    "patient_name": "Ahmed",
                    "date": "December 25th"
                }
            }
        ]

        CRITICAL RULES:
        1. ONLY output valid JSON - no other text allowed
        2. Extract ALL intents found in the text - can be multiple
        3. For each intent, extract ONLY explicitly mentioned entities
        4. NEVER include fields that aren't explicitly mentioned
        5. NEVER add null, empty, or assumed values
        6. Keep numeric values as numbers (like age: 45)
        7. Keep text values as strings
        8. Each piece of information should go with its most relevant intent

        WRONG OUTPUTS (NEVER DO THESE):
        Including unmentioned fields:
        {
            "intent": "add_patient",
            "entities": {
                "name": "Ahmed",
                "condition": "diabetes",
                "age": null,        // WRONG: age wasn't mentioned
                "gender": ""       // WRONG: gender wasn't mentioned
            }
        }

        Adding assumed information:
        {
            "intent": "assign_medication",
            "entities": {
                "patient_name": "John",
                "medication": "paracetamol",
                "frequency": "as needed"  // WRONG: frequency wasn't specified
            }
        }

        REMEMBER:
        - ONLY include information explicitly mentioned in the input
        - NEVER add fields with null or empty values
        - NEVER assume or infer missing information
        - Output must be parseable JSON - nothing else!

        '''
        self.pipeline = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.3")

    def _validate_json(self, json_str: str) -> Union[Dict, List]:
        """
        Validate and clean the JSON output
        
        Args:
            json_str (str): JSON string to validate
            
        Returns:
            Union[Dict, List]: Parsed JSON object
        """
        try:
            # Remove any additional text before and after the JSON
            json_str = json_str.strip()
            if json_str.find('{') > 0:
                json_str = json_str[json_str.find('{'):]
            if json_str.find('}') < len(json_str) - 1:
                json_str = json_str[:json_str.rfind('}') + 1]
                
            return json.loads(json_str)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON output: {str(e)}")

    def run(self, query: str) -> Union[Dict, List]:
        """
        Process a natural language query and return structured JSON output
        
        Args:
            query (str): Natural language medical instruction
            
        Returns:
            Union[Dict, List]: Structured JSON output
        """
        try:
            messages = [
                {
                "role": "system", 
                "content": self.system_prompt
                },
                {
                "role": "user",
                "content": query
                }
            ]
            response = self.pipeline(messages, max_tokens=500)
            response = response[0]["generated_text"]
            json_output = self._validate_json(response)
            return json_output
            
        except Exception as e:
            return {
                "error": {
                    "type": "processing_error",
                    "message": str(e)
                }
            }

