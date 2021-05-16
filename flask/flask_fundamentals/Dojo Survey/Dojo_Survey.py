from types import MethodType
from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key='name'
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    print(request.form)
    session['name']=request.form['name']
    session['location']=request.form['locationn']
    session['fav']=request.form['fav']
    session['comment']=request.form['comment']
    return redirect("/show")

@app.route('/show')
def show1():
    print (request.form)
    return render_template('index2.html')


if __name__ == "__main__":
    app.run(debug=True)
