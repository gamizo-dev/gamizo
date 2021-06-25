import os
import boto3
from flask import Flask, render_template, request
import main
import firebase_admin
from firebase_admin import credentials, firestore, initialize_app
from boto3 import session
from botocore.client import Config
from boto3.s3.transfer import S3Transfer

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

app = Flask(__name__)
# upload_path = 'static/asset/Videos/'
# app.config['UPLOAD_FOLDER'] = upload_path


@app.route('/')
def index():
    db = firestore.client()
    docs = db.collection('apps').document('apps').collection('Action').get()
    
    l=[]
    for doc in docs:
        l.append(doc.to_dict())
    return render_template('index.html', list=l)


@app.route('/upload.html')
def new():
    return render_template('upload.html')


@app.route('/getlink', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        linkText = request.form['linkText']
        f = request.files['mp4video']
        f.save(f.filename)

    db = firestore.client()
    s = main.takeinput(linkText)
    # print(s)

 # transfer.ALLOWED_UPLOAD_ARGS.append('ContentType')
    transfer.upload_file(f.filename, 'gamizo', s['category']+'/'+s['name'], extra_args={'ContentType': 'video/mp4', 'ACL': 'public-read'})
    str = s['name']
    doc_ref = db.collection('apps').document(
        'apps').collection(s['category']).document(s['name'])
    s['name'].strip()
    url_take = f"https://gamizo.sgp1.digitaloceanspaces.com/{s['category']}/{s['name']}"
    doc_ref.set({
        'name': str,
        'link': linkText,
        'videoUrl': url_take
    })
    category_ref=db.collection('category').document('apps')
    
    list1=[]
    cat_refget=db.collection('category').get()

    for c in cat_refget:
        list1.append(c.to_dict())
    
    for i in list1:
        if s['category'] != i.values():
             category_ref.set({
              f"{s['category']}": s['category']
            })
    
    # if s['category'] not in cat:
    #    
        
    # print(set)
    return render_template('upload.html')


@app.route('/contact.html')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
