
import requests
from os import replace
import os
import boto3
from flask import Flask, render_template, request, redirect
import firebase_admin
from firebase_admin import credentials, firestore, initialize_app
from boto3 import session
from botocore.client import Config
from boto3.s3.transfer import S3Transfer
from requests.api import options

ACCESS_ID = '5GFF7YOAHZWTV5VKP7Q6'
SECRET_KEY = '3mPgnLrUXGhLSb+0JHFElxP0HICyv7LSaEw0hsLWs5c'

# Initiate session
session = session.Session()
client = session.client('s3',
                        region_name='sgp1',
                        endpoint_url='https://sgp1.digitaloceanspaces.com',
                        aws_access_key_id=ACCESS_ID,
                        aws_secret_access_key=SECRET_KEY)
transfer = S3Transfer(client)
# Upload a file to your Space

cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred)



app = Flask(__name__,template_folder='template')
# upload_path = 'static/asset/Videos/'
# app.config['UPLOAD_FOLDER'] = upload_path


@app.route('/')
def index():
    db = firestore.client()
    docs = db.collection('apps').document('apps').collection('Popular').get()

    l = []
    for doc in docs:
        l.append(doc.to_dict())

    list1 = []
    cat_refget = db.collection('category').get()

    for c in cat_refget:

        list1.append(c.to_dict())
    
    a = []
    for i in list1:
        for j in i.values():
            a.append(j)
    
    return render_template('index.html', list=l, cat=a)


@app.route('/<string:cat>')
def index1(cat):
    db = firestore.client()
    docs = db.collection('apps').document('apps').collection(cat).get()

    l = []
    for doc in docs:
        l.append(doc.to_dict())

    list1 = []
    cat_refget = db.collection('category').get()

    for c in cat_refget:

        list1.append(c.to_dict())
    print(list1)
    a = []
    for i in list1:
        for j in i.values():
            a.append(j)
    print(a)
    return render_template('index.html', list=l, cat=a)


@app.route('/share/<string:sharestr>')
def share(sharestr):
    db = firestore.client()
    cat = ''
    name = ''
    i = 0
    while sharestr[i] != '_':
        cat += sharestr[i]
        i = i+1
    i = i+1
    while i < len(sharestr):
        name += sharestr[i]
        i = i+1

    # docs = db.collection('apps').document('apps').collection(cat).get()

    docs = db.collection('apps').document('apps').collection(cat).document(name).get()
    sp=docs.to_dict()

    list1 = []

    cat_refget = db.collection('category').get()

    for c in cat_refget:

        list1.append(c.to_dict())
    a = []
    for i in list1:
        for j in i.values():
            a.append(j)
    
    return render_template('share.html', cat=a,sp=sp)





@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/report', methods=['GET', 'POST'])
def report():
    if request.method == "POST":
        option = request.form['report']
        gamename = request.form['gamename']

    db = firestore.client()
    doc_ref = db.collection('Report').document(gamename)
    docs = db.collection('Report').document(gamename).get()
    doc = docs.to_dict()
    if doc:
        num = doc['number']
        nums = int(num)
        nums = nums+1
        doc_ref.update({
            'number': f'{nums}',
            f'{nums}': option

        })
    else:
        doc_ref.set({
            'number': '1',
            '1': option
        })

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, port=8000)
