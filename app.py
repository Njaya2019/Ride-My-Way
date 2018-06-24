from flask import Flask, render_template

app=Flask(__name__)

@app.route('/', methods=["GET","POST"])
def index():
    return render_template('index.html')

@app.route('/login',methods=["GET"])
def login():
    return render_template('login.html')

@app.route('/signup',methods=["GET"])
def signup():
    return render_template('signup.html')

@app.route('/driver',methods=["GET"])
def driver():
    return render_template('driver.html')

@app.route('/rides')
def rides():
    return render_template('rides.html')

@app.route('/passengers', methods=["GET"])
def passengers():
    return render_template('passengers.html')


if __name__=='__main__':
    app.run()