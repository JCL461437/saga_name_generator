import os
from flask import Flask, jsonify, request
from fictional_names import name_generator

# Initialize the Flask app
app = Flask(__name__)

### Function for Name Generation and API Endpoint ###
@app.route('/api/v1/generate_name')
def generate_names():
    # Extract query parameters
    gender = request.args.get('gender')
    style = request.args.get('style')
    library = request.args.get('library', type=bool)  # Default to False if not specified
    
    # Ensure all parameters are provided
    if not gender or not style:
        return jsonify({"error": "Missing required parameters 'gender' or 'style'"}), 400
    
    # Generate name (Assuming the name_generator function is correct)
    name = name_generator.generate_name(gender=gender, style=style, library=library)
    
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

# Run the Flask app
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    host = os.environ.get('HOST', 'localhost')
    app.run(host=host, port=port, debug=True)
