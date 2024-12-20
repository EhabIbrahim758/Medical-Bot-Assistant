import requests
import json

def parse_medical_instruction(query):
    response = requests.post(
        'http://localhost:5000/parse',
        json={'query': query}
    )
    return response.json()


def batch_parse_instructions(queries):
    response = requests.post(
        'http://localhost:5000/batch_parse',
        json={'queries': queries}
    )
    return response.json()


if __name__ == '__main__':
    
    text = '''Add new patient Ahmed Hassan, 45 years old male with diabetes and high blood pressure
        '''
    result = parse_medical_instruction(
        json.dumps({'query': text})
    )
    print('='*10, 'First Example', '='*10)
    print(result)
    # =================================================================

    text = '''Give patient Sarah Wilson 500mg paracetamol every 6 hours for fever, and 250mg amoxicillin twice daily for 7 days
        '''
    result = parse_medical_instruction(
        json.dumps({'query': text})
    )
    print('='*10, 'Second Example', '='*10)
    print(result)
    # =================================================================

    text = '''Register Mike Brown, 32 years old with asthma, and record his vitals: BP 120/80, temp 37.5, heart rate 75
        '''
    result = parse_medical_instruction(
        json.dumps({'query': text})
    )
    print('='*10, 'Third Example', '='*10)
    print(result)
    # =================================================================

    text = '''Initiate Code Blue for patient in Room 203, John Doe unresponsive with no pulse
        '''
    result = parse_medical_instruction(
        json.dumps({'query': text})
    )
    print('='*10, 'Fourth Example', '='*10)
    print(result)
    # =================================================================

    text = '''Change dressing for Maria Garcia's wound in Room 105, then collect blood samples for CBC and liver function tests
        '''
    result = parse_medical_instruction(
        json.dumps({'query': text})
    )
    print('='*10, 'Fifth Example', '='*10)
    print(result)
    # =================================================================

    text = '''Schedule follow-up appointment for James Smith next Monday at 2pm with Dr. Johnson for wound assessment and arrange transportation
        '''
    result = parse_medical_instruction(
        json.dumps({'query': text})
    )
    print('='*10, 'Sixth Example', '='*10)
    print(result)
    # =================================================================

    text = '''Monitor patient Lisa Chen every 2 hours for fever, blood pressure, and oxygen levels, alert if temperature exceeds 38.5
        '''
    result = parse_medical_instruction(
        json.dumps({'query': text})
    )
    print('='*10, 'Seventh Example', '='*10)
    print(result)
    # =================================================================

    text = '''Urgently order 50 units of gauze, 2 boxes of surgical gloves size M, and 3 bottles of antiseptic solution
        '''
    result = parse_medical_instruction(
        json.dumps({'query': text})
    )
    print('='*10, 'Eighth Example', '='*10)
    print(result)
    # =================================================================

    text = '''Transfer diabetic patient Robert Young from ICU to Ward 4B, needs wheelchair assistance and continuous glucose monitoring
        '''
    result = parse_medical_instruction(
        json.dumps({'query': text})
    )
    print('='*10, 'Ninth Example', '='*10)
    print(result)
    # =================================================================

    text = '''Document patient Emma Watson's symptoms: severe headache since morning, nausea, sensitivity to light, and record vital signs: BP 135/85, temp 37.8
        '''
    result = parse_medical_instruction(
        json.dumps({'query': text})
    )
    print('='*10, 'Tenth Example', '='*10)
    print(result)
    # =================================================================
    
    text1 = '''Add new patient Ahmed Hassan, 45 years old male with diabetes and high blood pressure
    '''
    text2 = '''Document patient Emma Watson's symptoms: severe headache since morning, nausea, sensitivity to light, and record vital signs: BP 135/85, temp 37.8
        '''
    result = parse_medical_instruction(
        json.dumps({'queries': [text1, text2]})
    )
    