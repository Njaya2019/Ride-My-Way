from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/driver')
def driver():
    return render_template('driver.html')

@app.route('/rides')
def rides():
    return render_template('rides.html')

@app.route('/passengers')
def passengers():
    return render_template('passengers.html')


if __name__=='__main__':
    app.run()