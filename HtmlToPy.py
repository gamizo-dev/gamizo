import os
from flask import Flask, render_template, request
import main
import firebase_admin
from firebase_admin import credentials, firestore, initialize_app


cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred)

app = Flask(__name__)
@app.route('/')
def index():
    db= firestore.client()
    docs = db.collection('apps').where('category','==','Action').stream()
    print(docs)
    return render_template('index.html',doc=docs)
@app.route('/upload.html')
def new():
    return render_template('upload.html')
@app.route('/getlink',methods=['GET','POST'])
def upload():
    if request.method=='POST':
        linkText=request.form['linkText']
    db= firestore.client()
    s=main.takeinput(linkText)
    # print(s)
    doc_ref = db.collection('apps').document('apps').collection(s['category']).document(s['name'])
    doc_ref.set({
        'name': s['name'],
        'link': linkText
    })

    return render_template('upload.html')

if __name__ =='__main__':
    app.run(debug=True)