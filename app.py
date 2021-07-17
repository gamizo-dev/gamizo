from bs4 import BeautifulSoup
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


def takeinput(url):

    r = requests.get(url)
    htmlContent = r.content

    soup = BeautifulSoup(htmlContent, 'html.parser')

    title = soup.title
    category = soup.find("a", {"itemprop": "genre"}).text
    # print(title.string)
    s = title.string
    s = s[:-22]

    imageLink = soup.find("div", {"class": "xSyT2c"})
    for item in imageLink:
        icon = item['src']

    spans = soup.find_all("span", {"class": "htlgb"})
    appSize = spans[2].text
    Downloads = spans[4].text

    stars = soup.find("div", {"class": "pf5lIe"})
    for item2 in stars:
        rating = item2['aria-label']

    rating = rating.replace('Rated ', '')
    rating = rating.replace('stars out of five stars', '')

    b = Downloads


    str = ''
    for char in b:
        if not char == ',' or char == '+':
            str += char

    l = len(str)-1
    c = str[0:l]
    a = int(c)

    if a < 1000:
        smallDownload=str(a)

    elif a >= 1000 and a < 5000:
        smallDownload='1T+'

    elif a >= 5000 and a < 10000:
        smallDownload='5T+'

    elif a >= 10000 and a < 50000:
        smallDownload='10T+'

    elif a >= 50000 and a < 100000:
        smallDownload='50T+'

    elif a >= 100000 and a < 500000:
        smallDownload='100T+'

    elif a >= 500000 and a < 1000000:
        smallDownload='500T+'

    elif a >= 1000000 and a < 5000000:
       smallDownload='1M+'

    elif a >= 5000000 and a < 10000000:
       smallDownload='5M+'

    elif a >= 10000000 and a < 50000000:
        smallDownload='10M+'

    elif a >= 50000000 and a < 100000000:
        smallDownload='50M+'

    elif a >= 100000000 and a < 500000000:
       smallDownload='100M+'

    else:
        smallDownload='500M+'

    cat = {'name': s, 'category': category, 'icon': icon,
           'appSize': appSize, 'Downloads': Downloads, 'rating': rating,'smallDownload':smallDownload}
    return cat

app = Flask(__name__)
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
    s = takeinput(linkText)
    # print(s)

 # transfer.ALLOWED_UPLOAD_ARGS.append('ContentType')
    transfer.upload_file(f.filename, 'gamizo', s['category']+'/'+s['name'], extra_args={
                         'ContentType': 'video/mp4', 'ACL': 'public-read'})
    str = s['name']
    doc_ref = db.collection('apps').document(
        'apps').collection(s['category']).document(s['name'])
    s['name'].strip()
    url_take = f"https://gamizo.sgp1.digitaloceanspaces.com/{s['category']}/{s['name']}"
    doc_ref.set({
        'name': str,
        'link': linkText,
        'videoUrl': url_take,
        'imageLink': s['icon'],
        'Downloads': s['Downloads'],
        'AppSize': s['appSize'],
        'Rating': s['rating'],
        'Category': s['category']
        # 'imageLink':imageLink
    })
    category_ref = db.collection('category').document('apps')
    list1 = []
    cat_refget = db.collection('category').get()

    for c in cat_refget:
        list1.append(c.to_dict())
    print(list1)

    for i in list1:
        if s['category'] != i.values():
            category_ref.update({
                f"{s['category']}": s['category']
            })
    # if s['category'] not in cat:
    #

    # print(set)
    return render_template('upload.html')


@app.route('/contact.html')
def contact():
    return render_template('contact.html')


@app.route('/report', methods=['GET', 'POST'])
def report():
    if request.method == "POST":
        option = request.form['Report']
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
