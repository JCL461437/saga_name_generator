from fictional_names import name_generator
import os
import requests
import flask import Flask, jsonify, request 
import flask_cors import CORS

# Initialize the Flask app
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

### Function for Name Generation and API Endpoint ###
@app.route('/api/v1/generate_names?gender=<gender>?style=<style>?library=<library>')
def generate_names(gender, style, library):
  name = name_generator.generate_name(gender=gender, style=style, library=True)
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
    socketio.run(app, host=host, port=port, debug=True)

