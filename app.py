from flask import Flask, jsonify
from flask import *
import pymongo
from pymongo import MongoClient
app = Flask(__name__)
app.secret_key = "abc"  

#CONNECTION_STRING = "mongodb+srv://divya:divyakapil@cluster0-cyu9f.mongodb.net/test?retryWrites=true&w=majority"
#client = pymongo.MongoClient(CONNECTION_STRING)
#db = client.get_database('log')
#user_collection = pymongo.collection.Collection(db, 'logs1')

cluster = MongoClient("mongodb+srv://divya:divyakapil@cluster0-cyu9f.mongodb.net/test?retryWrites=true&w=majority")
db = cluster['log']
col = db['collection']

@app.route('/')
def home():
    if(session['logged_in']):
        return render_template('index.html',uname=session['name'])
    else:
        return render_template('index.html',uname='Login')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login1',methods=['POST','GET'])
def login1():
    if request.method == 'POST':            #to check if form contains smthing or not
        username=request.form['username']   #extract username and password from form to local variables
        password=request.form['pswd']
        x=col.find_one({'username':username}) #this finds data of that username
        if(x):
            if(x['password']==password):
                #password match, here i will put two things in session
                session['logged_in']=True;
                session['name']=username;
                return redirect(url_for('home'))
            else:
                print("Wrong Password")
                return redirect(url_for('login'))
        else:
            print("User not found")
    return render_template('login.html')



@app.route('/logout')    
def logout():
    session['logged_in']=False
    return render_template('logout.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/payment')
def payment():
    return render_template('payment.html')    

@app.route("/test")
def test():
    db.db.collection.insert_one({"name": "divya"}) #here collection is the name of record
    return "Connected to the data base!"

@app.route('/signup')
def signup():   
    return render_template('signup.html')

@app.route("/successreg",methods=['POST','GET'])  #the route /successred here is used in action field of HTML form tag
def successreg():
    if request.method == 'POST':            #to check if form contains smthing or not
        username=request.form['username']   #extract username and password from form to local variables
        password=request.form['password']
        address=request.form['address']
        contact=request.form['contact']
        emailid=request.form['emailid']
        print("\n Data received:")
        print(username)
        print(password)
        x = col.insert_one({'username':username,'password':password,'address':address,'contact':contact,'emailid':emailid})   #insert that username and password to database
        if(x):                                  #if successful send to home page
            print("Successfully registered")    
            return redirect(url_for('home'))
        else:                                   #if unsuccesful send to register page
            print("Unsuccessful register")
            return render_template("signup.html")
    return render_template("signup.html")    
    
@app.route('/house1')
def house1():#this shud be restricted ok
    if(session['logged_in']==True):
        return render_template('house1.html')
    else:
        return redirect(url_for('login'))

@app.route('/menu')
def menu():
    return redirect(url_for('home'))
@app.route('/pay1')
def pay1():
    return render_template('pay1.html')


if __name__ == '__main__':
    app.run(debug=True)
