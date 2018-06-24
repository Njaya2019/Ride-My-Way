from flask import Flask, render_template

app=Flask(__name__)

@app.route('/', methods=["GET","POST"])
def index():
    return render_template('index.html',methods=["GET","POST"])

@app.route('/login')
def login():
    return render_template('login.html',methods=["GET","POST"])

@app.route('/signup')
def signup():
    return render_template('signup.html',methods=["GET","POST"])

@app.route('/driver')
def driver():
    return render_template('driver.html', methods=["GET","POST"])

@app.route('/rides')
def rides():
    return render_template('rides.html', methods=["GET","POST"])

@app.route('/passengers', methods=["GET","POST"])
def passengers():
    return render_template('passengers.html')


if __name__=='__main__':
    app.run()