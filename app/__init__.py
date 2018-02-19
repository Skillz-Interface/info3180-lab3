from flask import Flask
from flask_mail import Mail

app = Flask(__name__)

app.config['SECRET_KEY'] = 'passphrase'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '2525'
app.config['MAIL_USERNAME'] ='9e8174f5085ea0'
app.config['MAIL_PASSWORD'] = '7fb25a3e5ebba3'

mail = Mail(app)
from app import views