from MySQLdb.cursors import Cursor
from flask import Flask, render_template, request, redirect
from boto3 import session
from boto3.s3.transfer import S3Transfer
import mysql.connector
from datetime import datetime

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

conn = mysql.connector.connect(host='165.232.184.154',
                              database='gimizo2',
                              user='root',
                              password='Gimizo@04!2021810',
                              auth_plugin='mysql_native_password')

cursor=conn.cursor()
@app.route('/')
def index():
    cursor.execute('''SELECT * from gamesdata''')
    
    result=cursor.fetchall()

    
    cursor.execute('''SELECT DISTINCT category from gamesdata''')
    a=cursor.fetchall()
  

    return render_template('index.html', list=result, cat=a)


@app.route('/<string:cat>')
def index1(cat):
    cursor.execute('''SELECT * from gamesdata WHERE category=%s''',(cat,))
    result=cursor.fetchall()


    cursor.execute('''SELECT DISTINCT category from gamesdata''')
    a=cursor.fetchall()

    return render_template('index.html', cat=a,list=result)

@app.route('/share/<string:sharestr>')
def sharepage(sharestr):
    category=''
    gamename=''

    i=0
    while sharestr[i]!='_':
        category=category+sharestr[i]
        i=i+1

    i=i+1
    while i<=len(sharestr):
        gamename=gamename+sharestr[i]
        i=i+1

    cursor.execute('''SELECT * from gamesdata WHERE category=%s and gamename=%s''',(category,gamename))

    sp=cursor.fetchall()


    cursor.execute('''SELECT DISTINCT category from gamesdata''')
    a=cursor.fetchall()

    cursor.execute('''SELECT * from where category="Popular" ''')
    result=cursor.fetchall()

    return render_template('share-hidden.html', sp=sp,cat=a,list=result)





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
    if request.method == "POST":
        option = request.form['report']
        gamename = request.form['gamename']
        category = request.form['category']
    
    now = datetime.now()
    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
    
    cursor.execute('''INSERT INTO report(Gamename,Issue,reportdate) VALUES(%s,%s,%s)''',
    (gamename,option,formatted_date))
    
    conn.commit()


    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, port=8000)
