from flask import Flask, request, jsonify
from assistant import MedicalTaskParser


app = Flask(__name__)

# Initialize parser
parser = MedicalTaskParser()

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy"}), 200

@app.route('/parse', methods=['POST'])
def parse_task():
    """
    Parse medical task endpoint
    
    Expected JSON body:
    {
        "query": "your natural language query here"
    }
    """
    try:
        data = request.get_json()
        
        if not data or 'query' not in data:
            return jsonify({
                "error": {
                    "type": "invalid_request",
                    "message": "Missing 'query' field in request body"
                }
            }), 400
            
        query = data['query']
        result = parser.run(query)
        
        return jsonify(result), 200
        
    except Exception as e:
        return jsonify({
            "error": {
                "type": "server_error",
                "message": str(e)
            }
        }), 500

@app.route('/batch_parse', methods=['POST'])
def batch_parse():
    """
    Batch parse multiple queries
    
    Expected JSON body:
    {
        "queries": ["query1", "query2", ...]
    }
    """
    try:
        data = request.get_json()
        
        if not data or 'queries' not in data:
            return jsonify({
                "error": {
                    "type": "invalid_request",
                    "message": "Missing 'queries' field in request body"
                }
            }), 400
            
        queries = data['queries']
        results = [parser.run(query) for query in queries]
        
        return jsonify({"results": results}), 200
        
    except Exception as e:
        return jsonify({
            "error": {
                "type": "server_error",
                "message": str(e)
            }
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)