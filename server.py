from flask import Flask
app = Flask(__name__)

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