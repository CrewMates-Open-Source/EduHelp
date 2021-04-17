from decouple import config

from flask import Flask, request, render_template
from flask_mail import Mail, Message


app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = config('EMAIL')
app.config['MAIL_PASSWORD'] = config('PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEFAULT_SENDER'] = config('EMAIL')

mail = Mail(app)

@app.route("/contactUs", methods=['POST'])
def contactUs():
    req = request.form
    
    formData = getFormData(req)

    if not validateInput(formData):
        return "COULD_NOT_SEND_EMAIL_SUCCESSFULLY"
    else:
        firstName, lastName, email = formData
        sendEmail(firstName, lastName, email)
        return "EMAIL_SENT_SUCCESSFULLY"

def getFormData(req):
    firstName = req.get('first_name')
    lastName = req.get('last_name')
    email = req.get('email')

    return (firstName, lastName, email)

def validateInput(formData):
    return [False if not data else True for data in formData]
    
def sendEmail(firstName, lastName, email):
    subject = 'Welcome to EduHelp'
    msg = Message(recipients=[email], subject=subject)
    msg.html = "<h2>Hi {} {},</h2> <p> Greetings from team EduHelp. </p> <p> Thanks for reaching out to us. </p> <p> Here is the google drive link to our product. </p> <p> Feel free to download and use our application.</p>".format(firstName, lastName)
    mail.send(msg)

if __name__ == '__main__':
   app.run(debug = True)




