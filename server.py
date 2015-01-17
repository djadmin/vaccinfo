from flask import Flask
app = Flask(__name__, static_folder='client', static_url_path='')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/getNextVaccinationInfo')
def getNextVaccinationInfo():
    return 'Vaccination V1 due on 19-12-2015'

def registerInfant():
    pass

def getInfantInfo():
    raise NotImplementedError

if __name__ == '__main__':
    app.run(host='0.0.0.0')
