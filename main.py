from flask import Flask, render_template, request, redirect


import mysql.connector
from datetime import datetime
import random






app = Flask(__name__,template_folder='template')

conn = mysql.connector.connect(host='165.232.184.154',
                              database='gimizo2',
                              user='root',
                              password='Gimizo@04!2021810',
                              auth_plugin='mysql_native_password')


@app.route('/')
def index():
    cursor=conn.cursor()
    category='Popular'
    cursor.execute('''SELECT * from gamesdata where category=%s ''',(category,))
    
    result=cursor.fetchall()

    
    cursor.execute('''SELECT DISTINCT category from gamesdata''')
    a=cursor.fetchall()
    
    random.shuffle(result)
    random.shuffle(a)

    cursor.close()
    return render_template('index.html', list=result, cat=a)



@app.route('/<string:cat>')
def index1(cat):
    cursor=conn.cursor()
    cursor.execute('''SELECT * from gamesdata WHERE category=%s''',(cat,))
    result=cursor.fetchall()


    cursor.execute('''SELECT DISTINCT category from gamesdata''')
    a=cursor.fetchall()

    random.shuffle(result)
    random.shuffle(a)

  

    
    category='Popular'
    cursor.execute('''SELECT * from gamesdata where category=%s ''',(category,))
    result1=cursor.fetchall()
    

    cursor.close()
    return render_template('index.html', cat=a,list=result,list1=result1)

@app.route('/share/<string:sharestr>')
def sharepage(sharestr):
    cursor=conn.cursor()
    category=''
    gamename=''

    i=0
    while sharestr[i]!='_':
        category=category+sharestr[i]
        i=i+1

    i=i+1
    while i<len(sharestr):
        gamename=gamename+sharestr[i]
        i=i+1

    cursor.execute('''SELECT * from gamesdata WHERE category=%s and gamename=%s''',(category,gamename))

    sp=cursor.fetchall()


    cursor.execute('''SELECT DISTINCT category from gamesdata''')
    a=cursor.fetchall()

    category='Popular'
    cursor.execute('''SELECT * from gamesdata where category=%s and gamename!=%s ''',(category,gamename))
    result=cursor.fetchall()

    random.shuffle(result)
    random.shuffle(a)

    cursor.close()
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
    cursor=conn.cursor()
    if request.method == "POST":
        option = request.form['report']
        gamename = request.form['gamename']
        category = request.form['category']
    
    now = datetime.now()
    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
    
    cursor.execute('''INSERT INTO report(Gamename,Issue,reportdate) VALUES(%s,%s,%s)''',
    (gamename,option,formatted_date))
    
    conn.commit()

    cursor.close()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True,port=8000)
