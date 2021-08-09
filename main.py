from MySQLdb.cursors import Cursor
from flask import Flask, render_template, request, redirect
from boto3 import session
from boto3.s3.transfer import S3Transfer
import mysql.connector


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


app = Flask(__name__,template_folder='template')

conn = mysql.connector.connect(host='127.0.0.1',
                              database='gimizogames',
                              user='gimizodata',
                              password='King04@2021!',
                              auth_plugin='mysql_native_password')

cursor=conn.cursor()
@app.route('/')
def index():
    cursor.execute('''SELECT * from games WHERE category="Popular"''')
    
    result=cursor.fetchall()

    
    cursor.execute('''SELECT DISTINCT category from games''')
    a=cursor.fetchall()
  

    return render_template('index.html', list=result, cat=a)


@app.route('/<string:cat>')
def index1(cat):
    cursor.execute('''SELECT * from games WHERE category=%s''',(cat))
    result=cursor.fetchall()


    cursor.execute('''SELECT DISTINCT category from games''')
    a=cursor.fetchall()

    return render_template('index.html', cat=a,list=result)





@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/about')
def about():
    return render_template('About-us.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy-policy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/report', methods=['GET', 'POST'])
def report():
    # if request.method == "POST":
    #     option = request.form['report']
    #     gamename = request.form['gamename']
    #     category = request.form['category']

    # db = firestore.client()
    # doc_ref = db.collection('Report').document(gamename)
    # docs = db.collection('Report').document(gamename).get()
    # doc = docs.to_dict()
    # if doc:
    #     num = doc['number']
    #     nums = int(num)
    #     nums = nums+1
    #     doc_ref.update({
    #         'number': f'{nums}',
    #         f'{nums}': option

    #     })
    # else:
    #     doc_ref.set({
    #         'number': '1',
    #         '1': option
    #     })

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, port=8000)
