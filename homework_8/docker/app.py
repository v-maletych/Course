from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Web App sadsaaasdsadsaasdasdkek lol'


app.run(host='0.0.0.0', port=5000, debug=True)
