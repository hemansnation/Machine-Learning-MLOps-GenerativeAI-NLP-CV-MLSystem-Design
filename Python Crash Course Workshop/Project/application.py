from flask import Flask, render_template

app = Flask(__name__)   # __name__ => __main__

@app.route('/')
def home():
    return "Welcome to the first API"

@app.route('/profile')
def profile():
    return "<h1>Welcome User to the profile</h1>"

@app.route('/index')
def indore():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)













#       https://github.com/hemansnation
#    scheme     dns                /route
# http,       domain name system
# https, 
# ftp, 
# file

