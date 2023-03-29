import os
from urllib import request
from flask import Flask, render_template, request, redirect,session
from db import DB
import api
dbo = DB()
app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    # return "Hello Hello ! "
    # return "<h1 style='color:orange;' > Yoo Wassup ? </h1> "
    return render_template('login.html')

@app.route("/register")
def register():
    # return "Registration Page: "
   return render_template('register.html')


@app.route('/perform_registration',methods=['post'])
def perform_registration():
    name = request.form.get('user_name')
    email = request.form.get('user_email')
    password = request.form.get('user_password')
    response=dbo.insert(name,email,password)
    if response:
        return render_template('login.html',message="Registration Successfull. Kindly login to proceed")
    else:
        # return "email already Exist !"
        return render_template('register.html',message='email already exist')
    # return f"{name}  ... email : {email}smthng..."

@app.route('/perform_login',methods=['post'])
def perform_login():
    email = request.form.get('user_email')
    password = request.form.get('user_password')
    response = dbo.search(email,password)
    if response:
        session['logged_in'] = 1
        return redirect('/profile')
    else:
        return render_template('login.html',message='incorrect email password !')

@app.route('/profile')
def profile():
    if session:
        return render_template('profile.html')
    else:
        return redirect('/')

@app.route('/ner')
def ner():
    if session:
        return render_template('ner.html')
    else:
        return redirect('/')

# iskepass data aayega & then yeah perform karega
@app.route('/perform_ner',methods=['post'])
def perform_ner():
    if session:
       text = request.form.get('ner_text')
       response= api.ner(text)
       print(response)
       return render_template('ner.html',response=response)
    else:
        return redirect('/')



@app.route('/abuse')
def abuse():
    if session:
        return render_template('abuse.html')
    else:
        return redirect('/')

# iskepass data aayega & then yeah perform karega
@app.route('/perform_abuse',methods=['post'])
def perform_abuse():
    if session:
       text = request.form.get('abuse_text')
       response= api.abuse(text)
       # print(response)
       # print(response['abusive'])
       if response['abusive']>0.60:
           ab = f" {response['abusive']*100} %  Strongly Abusive !"
       else:
           ab = "Not Abusive"

       return render_template('abuse.html',response=ab)

    else:
        return redirect('/')



@app.route('/emotion')
def emotion():
    if session:
        return render_template('emotion.html')
    else:
        return redirect('/')

# iskepass data aayega & then yeah perform karega
@app.route('/perform_emotion',methods=['post'])
def perform_emotion():
    if session:
       text = request.form.get('emotion_text')
       response= api.emotion(text)
       print(response)
       response = response['emotion']
       maxemotion = max(response,key=response.get)
       print(maxemotion)
       return render_template('emotion.html',maxemotion=maxemotion)

    else:
        return redirect('/')


@app.route('/keyword_detection')
def keyword_detection():
    if session:
        return render_template('keywordDetection.html')
    else:
        return redirect('/')

# iskepass data aayega & then yeah perform karega
@app.route('/perform_keyword_detection',methods=['post'])
def perform_keyword_detection():
    if session:
       text = request.form.get('keyword_text')
       response= api.keywords(text)
       print(response)
       response =response['keywords']

       return render_template('keywordDetection.html',response = response)

    else:
        return redirect('/')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

app.run(debug=True)

