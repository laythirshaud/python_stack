from flask import Flask, render_template
app = Flask(__name__)
@app.route('/play')
def play1():
    return render_template("index.html", times=3,client_color='lightskyblue')

@app.route('/play/<num>')
def play_num(num):
    return render_template("index.html", times=int(num))

@app.route('/play/<num>/<coler>')
def play_num_coler(num,coler):
    return render_template("index.html", times=int(num), client_color=coler)
if __name__=="__main__":
    app.run(debug=True)
