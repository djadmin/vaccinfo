from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/getNextVaccinationInfo/<mobileNo>')
def getNextVaccinationInfo(mobileNo):
    a,d = getDueDate(mobileNo)
    return 'Vaccination' + a + 'due on ' + d + 'for MobileNumber: ' + mobileNo

def registerInfant():
    pass

def getInfantInfo():
    raise NotImplementedError


'''DB Fetch methods here'''
def getDueDate(mobileNo):
    return 'V1','18-12-2015'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)