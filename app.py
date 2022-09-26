from flask import Flask, render_template, redirect, url_for, request
from flask_mysqldb import MySQL


app=Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'form'

mysql = MySQL(app)
  
@app.route('/',methods=['GET','POST'])
def login():
    error = None
    text="invalid user"
    if request.method == 'POST':
        if request.form['username']=='admin' and request.form['password']=='admin':
            return render_template('dashboardtrial.html')
        else:
            return redirect(url_for('login'))
            
            
    return render_template('login.html')

@app.route('/for',methods=['GET','POST'])
def login1():
    return render_template('dashboardtrial.html')

@app.route('/form', methods=['GET', 'POST'])
def task():
       if request.method == "POST":
        client=request.form.get('client')
        details = request.form
        client=details['client']
        job=details['job']
        assign_to=details['assign_to']
        priority=details['priority']
        status=details['status']
        date=details['date']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO formdata(client,job,assign_to,priority,status,date) VALUES (%s,%s,%s,%s,%s,%s)", (client,job,assign_to,priority,status,date))
        mysql.connection.commit()
        cur.close()
       return render_template('home.html')
   
   
@app.route('/showdata',methods=['GET','POST'])
def showdata():
    cur=mysql.connection.cursor()
    cur.execute("select * from formdata")
    data=cur.fetchall()
    cur.close()
    return render_template('show.html',formdata=data)


    
if __name__=='__main__':
    app.run(debug='true')