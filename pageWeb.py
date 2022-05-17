from flask import Flask, render_template, redirect, url_for, request
from flask_mail import Mail, Message
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,validators
from wtforms.validators import DataRequired
#import local_settings

mail = Mail()
app = Flask(__name__)
app.secret_key ="devkey"
# mail setup 
app.config.update(

MAIL_SERVER = "smtp.gmail.com",
MAIL_PORT = 465,
MAIL_USE_SSL= True,
MAIL_USERNAME= 'aouataf.djillani@gmail.com',
#MAIL_PASSWORD = local_settings.MAIL_PASSWORD
)

mail.init_app(app)

# contact form setup 
class ContactForm(FlaskForm):

    name = StringField("Name", [validators.DataRequired("your name")],render_kw={"placeholder": "Your name"})
    email = StringField("Email", [validators.DataRequired("your email")],render_kw={"placeholder": "Youe email"})
    message = StringField("Message",[validators.DataRequired("leave your message")],render_kw={"placeholder": "Your message"})
    subject = StringField("Subject", [validators.Optional()],render_kw={"placeholder": "Optional "})
    submit = SubmitField("SUBMIT")

# home page 
@app.route('/', methods=['GET','POST'])
def index():
	form = ContactForm()
	return render_template('index.html', form=form)
# contact section 
@app.route('/#contact', methods=['GET','POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
    	if form.validate() == False:
      		
      		return render_template('webScraping.html', form=form)
    	else:

        	name = form.name.data
        	email = form.email.data
        	message = form.message.data
        	subject = form.subject.data
        	msg= Message(subject, sender=email, recipients=['aouataf.djillani@gmail.com'] )
        	msg.body=f"Email through your website!\nFrom: {name} \nEmail: {email}\nSubject: {subject}\nMessage: {message}"
        	mail.send(msg)
        	return "Form posted"
    if request.method == 'GET':
        return render_template('index.html', form=form)
# Articles from the project section 
@app.route('/web-scraping')
def scrape():
	return render_template('webScraping.html')

@app.route('/book-management-system-with-tkinter-and-sqlite3')
def book():
	return render_template('bookmanagement.html')

@app.route('/sentiment-analysis-with-vader')
def sentiment():
	return render_template('sentimentanalysis.html')
# google verification file 
@app.route("/google7f3a92e1f8be07e8.html")
def google_site_verf():
    return render_template("google7f3a92e1f8be07e8.html")

if __name__=="__main__":
	app.run(debug=True)
	


