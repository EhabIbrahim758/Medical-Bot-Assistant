# Medical Task Parser Bot

## 1. Introduction
The Medical Task Parser Bot is an intelligent system designed to parse natural language medical instructions into structured JSON format. It can handle various medical tasks including patient management, medication instructions, vital recordings, and administrative tasks. The bot supports both single and multiple intents in one query, making it versatile for different healthcare scenarios.

Key Features:
- Natural language understanding for medical instructions
- Support for multiple medical intents
- Structured JSON output
- RESTful API interface
- Batch processing capabilities
- Robust error handling

## 2. Installation and Setup

### Hardware Requirements
- Minumum system ram 30GB 
- Minimum system VRam 30GB
### Prerequisites
- Python 3.9 or higher
- pip package manager

### Dependencies Installation
```bash
# Clone the repository
git clone https://github.com/EhabIbrahim758/Medical-Bot-Assistant.git
cd medical-task-parser

# Create and activate conda environment (optional but recommended)
conda create --name assistant-env python==3.10 -y
conda activate assistant-env
pip install -r requirements.txt
huggingface-cli login >> put your huggingface access token  
```

## 3. Usage

starting the server

```bash
python medical_parser_api.py
```
The server will start on http://localhost:5000


## 4. Examples 

#### Single Intent Example
# Request

POST /parse
{
    "query": "Add patient John Smith, 45 years old male with diabetes"
}

# Response
{
    "intent": "add_patient",
    "entities": {
        "name": "John Smith",
        "age": 45,
        "gender": "male",
        "conditions": ["diabetes"]
    }
}

#### Multiple Intents Example
# Request
POST /parse
{
    "query": "Add patient Sarah Wilson with hypertension and schedule her blood test for tomorrow"
}

# Response
[
    {
        "intent": "add_patient",
        "entities": {
            "name": "Sarah Wilson",
            "conditions": ["hypertension"]
        }
    },
    {
        "intent": "schedule_procedure",
        "entities": {
            "name": "Sarah Wilson",
            "procedure": "blood test",
            "dates": ["tomorrow"]
        }
    }
]


## 5. API Documentation



### Endpoints Overview

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check endpoint |
| POST | `/parse` | Parse single medical instruction |
| POST | `/batch_parse` | Parse multiple medical instructions |


- you will find many API calls in the Testing Section 

## 6. How To Run Tests 

```bash
python test.py 
```
