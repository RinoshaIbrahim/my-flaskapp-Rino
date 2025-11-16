from platform import uname
from flask import Flask, render_template_string, request, render_template,redirect,url_for

# Create Flask instance
VALID_USERNAME="Rinosha"
VALID_PASSWORD="12345"

app = Flask(__name__)
@app.route('/', methods=['GET'])
def show_login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
   uname = request.form.get('uname')
   upass = request.form.get('upass')
    
   if uname == VALID_USERNAME and upass == VALID_PASSWORD:
              return redirect(url_for("success", username=uname, password=upass))
   else:
              return redirect(url_for("invalidd", username=uname))
   
                           

@app.route('/invalidd')
def invalidd():
     return render_template('err.html', username=request.args.get('username'))


@app.route("/success")
def success():
  return render_template("wel.html", username=request.args.get('username'), password=request.args.get('password'))

@app.route('/page1')
def page1():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)




