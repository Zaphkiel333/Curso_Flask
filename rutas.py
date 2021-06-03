from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return 'hola mundo que tal'

@app.route('/params')
def params():
    param=request.args.get('params1','el parametro no vino')
    param2=request.args.get('params2','el parametro no vino')
    return 'el parametro es: {},{}'.format(param, param2)

if __name__ == '__main__':
    app.run(debug=True, port=8000)