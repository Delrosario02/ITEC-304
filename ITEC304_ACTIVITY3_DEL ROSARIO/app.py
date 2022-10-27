from flask import Flask, request
from datetime import datetime

app= Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <body align='center' bgcolor='aquamarine'> 
        <br><h2>WELCOME TO THE GREETER</h2>
        <form action="/greet">
        What's your name?
        <input type='text' name='username'> is <br>
        What's your Characteristic?
        <input type='text' name='desc'> <br>
        <input type='submit' value='Continue'>
        </form>
        </html>
        </body>
        """
@app.route('/greeter')
def greeter():
    username = request.args.get('username')
    desc=request.args['desc']
    return """
    <html>
    <body align='center' bgcolor="pink"><br>
    <h2>Hello,{0} is {1}!</h2>
    </html>
    </body>
    """.format(username, desc) 

#launch the flask dev server

app.run(host="localhost",debug=True)