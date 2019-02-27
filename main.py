from flask import  Flask, request
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    config_ns = request.args.get('config_ns')
    config_mode = request.args.get('config_mode')
    data = request.get_json()
    print config_ns
    print config_mode
    print data
    return '<h1>Hello World!</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
