from flask import Flask, render_template, request
from contact_model import Contact
from google.cloud import ndb


app = Flask(__name__)


@app.route(r'/', methods=['GET'])
def hello_world():
	return render_template('contact_book.html')


@app.route(r'/add', methods=['GET', 'POST'])
def add_contact():
	client = ndb.Client()
	if request.form:
		with client.context():
			contact = Contact(
				name=request.form.get('name'),
				phone=request.form.get('phone'),
				email=request.form.get('email')
			)
			contact.put()

	return render_template('add_contact.html')


if __name__ == '__main__':
	app.run()
