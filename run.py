from flask import Flask

app = Flask(__name__)
@app.route('/')

def index():
    return 'hola mundo que tal'

if __name__ == '__main__':
    app.run(debug=True,port=8000)