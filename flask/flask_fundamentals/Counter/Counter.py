from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key='layth'
@app.route('/')
def visit():
    if 'counter' in session:
        session['counter']=session.get('counter')+1
    else:
        session['counter']=1
    return f"The Number of visit :{session.get('counter')}  times"
@app.route('/delete_visits/')
def delete_visite():
    session.clear()
    return 'visits deleted'

if __name__ == "__main__":
    app.run(debug=True)