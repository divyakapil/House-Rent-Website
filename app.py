from flask import Flask, jsonify
from flask import *
import pymongo 
from pymongo import MongoClient

cluster=MongoClient("mongodb+srv://divya:divya123@cluster0-2ipxk.gcp.mongodb.net/test?retryWrites=true&w=majority")
app = Flask(__name__)
app.secret_key="abc"
db=cluster["cportal"]
student=db["student"]



@app.route('/Register')
def register():
    return render_template('reg.html')

@app.route('/')
def start():
    return render_template('log.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/success1',methods=["POST"]) 
def success1():
    if request.method=="POST":
        result=request.form
        n=result["name"]
        rn=result["rollno"]
        pwd=result["psw"]
        p=student.insert_one({"name":n,"rollno":rn,"psw":pwd})
        if(p):
            return redirect(url_for("start"))
        else:
            return("unsuccessful")
    else:
        return redirect(url_for("register"))
    
@app.route('/test',methods=['POST','GET'])
def test():
    if request.method=='POST':
        result=request.form
        rollno=result["rollno"]
        psw=result["psw"]
        q=student.find_one({"rollno":rollno})
        if(q):
            ppsw=q["psw"]
            if(ppsw==psw):
                return redirect(url_for("home"))
            else:
                return redirect(url_for("start"))
        else:
            return redirect(url_for("start"))
    else:
        return redirect(url_for("start"))
    
    
if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    
#db_name=cportal
#collectn_name=student