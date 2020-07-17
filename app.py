from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index() : 
    name = ""
    if request.method == 'POST' :
        if request.form['displayName'] != "" : 
            name = request.form['displayName']
            return render_template('home.html', name = name)
        if request.form['name'] != "":
            channelname = request.form['name']
            return render_template('home.html', channelname = channelname)
    return render_template('displayName.html')



if __name__=='__main__' :
    app.run(debug=True)