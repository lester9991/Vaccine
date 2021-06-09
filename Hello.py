from flask import Flask, redirect, url_for, request
from data import *
app = Flask(__name__)
START = "\033[1m"
END = "\033[0;0m"
@app.route('/success/<name>')
def success(name):
   return  name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form

   else:
      user = request.args.get
   a = user['a']
   p = user['p']
   user = (a, int(p))
   if check_user(user):
      data = get_info(user)
      user = f"<b>Name: <b style='font-weight: normal;'>{data['Name']},<br><b>Co-WIN REF ID: <b style='font-weight: normal;'>{int(data['Co-WIN REF ID (13 or 14 digit ID on cowin.gov.in portal)'])},<br>" \
             f"<b>Building: <b style='font-weight: normal;'>{data['Apex Body / Housing Complex ']},<br><b>Aadhar No.: <b style='font-weight: normal;'>{a},<br><b>Phone No.: <b style='font-weight: normal;'>{p}"
   return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(debug = True)