from flask import Flask, jsonify
from flask import *
import pymongo
from pymongo import MongoClient
app = Flask(__name__)

#CONNECTION_STRING = "mongodb+srv://divya:divyakapil@cluster0-cyu9f.mongodb.net/test?retryWrites=true&w=majority"
#client = pymongo.MongoClient(CONNECTION_STRING)
#db = client.get_database('log')
#user_collection = pymongo.collection.Collection(db, 'logs1')

cluster = MongoClient("mongodb+srv://divya:divyakapil@cluster0-cyu9f.mongodb.net/test?retryWrites=true&w=majority")
db = cluster['log']
col = db['collection']

@app.route('/')
def home():
    return render_template('index.html')

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
            if(x['password']==password):   #password match
                return redirect(url_for('home'))
            else:
                print("Wrong Password")
                return redirect(url_for('login'))
        else:
            print("User not found")
    return render_template('login.html')



@app.route('/logout')    
def logout():
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
            return render_template("index.html")
        else:                                   #if unsuccesful send to register page
            print("Unsuccessful register")
            return render_template("signup.html")
    return render_template("signup.html")    
    
@app.route('/house1')
def house1():
    return render_template('house1.html')

@app.route('/menu')
def menu():
    return render_template('index.html')    
@app.route('/pay1')
def pay1():
    return render_template('pay1.html')


if __name__ == '__main__':
    app.run(debug=True)
