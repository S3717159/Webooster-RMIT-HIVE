from flask import Flask
from flask import Flask , redirect , url_for, render_template , request, session, flash, jsonify
app = Flask(__name__)

app.secret_key="webooster"


@app.route('/')
def mainPage():
    return render_template('launchPage.html')




app.config['TEMPLATES_AUTO_RELOAD'] = True
if app == "__main__":
    app.run()