from flask import Flask,render_template,request,redirect,flash
from wtforms import StringField,SubmitField,TextAreaField,PasswordField,validators,Form,BooleanField,DateTimeField
from wtforms.validators import DataRequired,required,Length,Email
from flask_sqlalchemy import SQLAlchemy
import os

app=Flask(__name__)
db_path = os.path.join(os.path.dirname(__file__), 'app.db')
db_uri = 'sqlite:///{}'.format(db_path)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.secret_key='xyz'
db=SQLAlchemy(app)



class Register(Form):
	name=StringField('Name',[validators.Length(min=10,max=20),validators.required('Please Enter Your Name')])
	mobile=StringField('Mobile',[validators.Length(max=10,min=10),validators.required('Please Enter Your Number')])
	email=StringField('Email',[validators.Length(min=6,max=30),validators.Email('Invalid Email')])
	Course=StringField('Course',[validators.required('*')])
	source=StringField('Source',[validators.required('*')])
	leadstatus=StringField('LeadStatus',[validators.required("*")])
	dm_coulg_cb=StringField('dm_coulg_cb',[validators.required('Please provide the required details')])
	counselor=StringField('Counsellor',[validators.required('*')])
	remark=StringField('Remarks',[validators.required('*')])

@app.route('/register',methods=['GET','POST'])

def register():
	form=Register(request.form)
	if(request.method=='POST' and form.validate()):


		reg=User(name=form.name.data,mobile=form.mobile.data,email=form.email.data,Course=form.Course.data,source=form.source.data,leadstatus=form.leadstatus.data,dm_coulg_cb=form.dm_coulg_cb.data,counselor=form.counselor.data,remark=form.remark.data )
		db.session.add(reg)
		db.session.commit()

		return '<h1>Registered</h1>'
	return render_template('register.html',form=form)	



if __name__=='__main__':
	app.run(debug=True)	