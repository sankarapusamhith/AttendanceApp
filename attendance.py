from flask import Flask , redirect, url_for ,request,render_template
import pyrebase
import datetime

config = {
  "apiKey":"AIzaSyBx57UaFMBPjnuTJZoW34ZvzaxgC1pPKq4",
  "authDomain": "samhith-a9fb1.firebaseapp.com",
  "databaseURL": "https://samhith-a9fb1.firebaseio.com",
  "storageBucket": "samhith-a9fb1.appspot.com"
}
firebase = pyrebase.initialize_app(config)
db=firebase.database()

x=datetime.datetime.now()
x=x.strftime("%y-%m-%d %H:%M:%S")

app=Flask(__name__)
@app.route('/',methods=['POST','GET'])
def login():
    if request.method=='POST':
        un=request.form['nam']
        uu=request.form['uni']
        ur=request.form['rn']
        uc=request.form['ph']
        data={'time':x,
            'name':un,
            'university':uu,
            'rollno':ur,
            "contact":uc 
            }
        return redirect(url_for('details',nam=un,uni=uu,rn=ur,ph=uc))
    return render_template("login.html")
@app.route('/details/<nam>/<uni>/<int:rn>/<int:ph>')
def details(nam,uni,rn,ph):
    all_details={
            'name':nam,
            'uni':uni,
            'rollno':rn,
            "pno":ph,
            "time":x
        }
    db.child("attendance").push(all_details)
    return render_template("display.html",det=all_details)

if __name__=='__main__':
    app.run(debug=True)    