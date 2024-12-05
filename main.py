import logging
from flask import Flask, jsonify, request
from fictional_names import name_generator
from flask_cors import CORS

# Initialize the Flask app
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Set up logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/api/v1/generate_name', methods=['GET'])
def generate_names():
    # Log the request to see if we are getting there
    app.logger.debug('API Request received')

    # Extract query parameters
    gender = request.args.get('gender')
    style = request.args.get('style')
    library = request.args.get('library', type=bool)  # Default to False if not specified

    # Log extracted parameters
    app.logger.debug(f"Parameters received: gender={gender}, style={style}, library={library}")

    # Ensure all parameters are provided
    if not gender or not style:
        app.logger.error("Missing required parameters 'gender' or 'style'")
        return jsonify({"error": "Missing required parameters 'gender' or 'style'"}), 400
    
    try:
        # Generate name (Assuming the name_generator function is correct)
        name = name_generator.generate_name(gender=gender, style=style, library=library)
        
        # Log generated name
        app.logger.debug(f"Generated name: {name}")
        
        return jsonify({
            "data": {
                "type": "{} {} name".format(style, gender),
                "attributes": {
                    "name": name,
                    "gender": gender,
                    "style": style
                }
            }
        })
    except Exception as e:
        app.logger.error(f"Error generating name: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

# Run the Flask app
if __name__ == '__main__':
    port = 5000
    host = 'localhost'
    app.run(host=host, port=port, debug=True)  # Debug mode for more insights
