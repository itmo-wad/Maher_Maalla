from flask import Flask, send_from_directory
app = Flask(__name__, static_folder='static')


@app.route('/')
def index():
    return app.send_static_file('index.html')
	
@app.route('/<path:path>')
def images(path):
    return send_from_directory(app.static_folder,path)
app.run(host='localhost', port=5000, debug=True)