from flask import Flask
from datetime import datetime
app = Flask(__name__, static_folder='client', static_url_path='')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/getNextVaccinationInfo/<mobileNo>')
def getNextVaccinationInfo(mobileNo):
    a,d = getDueDate(mobileNo)
    #int_birthDate = 01012015
    #str_birthTime = str('01012015')
    #date = calculateWeeks(str_birthTime)
    return 'Vaccination' + a + 'due on ' + d + 'for MobileNumber: ' + mobileNo
    
@app.route('/calcWeeks/<strBirthDate>')
def calcWeeks(strBirthDate):
    date = datetime.strptime(strBirthDate, '%d%m%Y')
    today = date.today() 
    delta = (today - date)
    return str(date) + '--' + str(delta)
    
def registerInfant():
    pass

def getInfantInfo():
    raise NotImplementedError

def calculateWeeks(str_birthDate):
    '''Expected format is DDMMYYYY'''
    #int_birthDate = 01012015
    #date = datetime(year = int_birthDate[4:8], month = int_birthDate[2:4], day = int_birthDate[0:2])
    date = datetime.strptime(str_birthDate, '%d%m%Y') 
    return date
    
'''DB Fetch methods here'''
def getDueDate(mobileNo):
    return 'V1','18-12-2015'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


