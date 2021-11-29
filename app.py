from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail
#import pandas as pd

app = Flask(__name__)
app.secret_key = 'development key'

#Para el envio de mail
mail = Mail()
app.config.update(dict(
	MAIL_SERVER = 'smtp.googlemail.com',
	MAIL_PORT = 465,
	MAIL_USE_TLS = False,
	MAIL_USE_SSL = True,
	MAIL_USERNAME = 'TestFernando',
	MAIL_PASSWORD = '[password]'
))

@app.route("/")
def home():
	return render_template("index.html")

# @app.route('/contact')
# def contact():
#     return render_template("contact.html")

@app.route('/about/')
def about():
	return render_template("about.html")

@app.route('/contact', methods=["GET","POST"])
def contact():
	if request.method == 'POST':
#		data =  request.form.to_dict() #Pasa a un Diccionario
#		print(data)
		name =  request.form["name"]  
		email = request.form["email"] #tiene que estar la proiedada name="email" en el Form html
		subject = request.form["subject"]
		message = request.form["message"]
		return 'Form posted.'
	elif request.method == 'GET':
		return render_template('contact.html')

# Gestionar 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
	app.run(debug=True)
