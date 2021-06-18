from flask import Flask,redirect,url_for

app=Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to my Youtube Channel'

@app.route('/success')
def success():
    return "<html><body><h1>The Reult is passed</h1></body></html>"


@app.route('/fail')
def fail():
    return "The Person has failed and the marks is "

### Result checker
@app.route('/results/<int:marks>')
def results(marks):
    result=""
    if marks<50:
        result='fail'
    else:
        result='success'
    return redirect(url_for(result))


if __name__=='__main__':
    app.run(debug=True)