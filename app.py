from flask import Flask, render_template, redirect, url_for, request, flash
import os
import hashlib
    
app = Flask(__name__)

@app.route("/")
def main():
    return redirect(url_for('login'))

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user_pw = request.form['password']
        result = hashlib.sha256(user_pw.encode()) 
        user_pw = result.hexdigest()
        with open ("pw.txt", "r") as myfile:
            data=myfile.readlines()
        stored_pw = data[0]
        if user_pw != stored_pw:
            error = 'Invalid Credentials. Please try again.'
            return render_template('login.html', error=error)
        else:
            return redirect(url_for('executing'))
    else:
        return render_template('login.html')
    

@app.route('/execute', methods=['GET'])
def executing():
    if request.referrer == 'http://127.0.0.1:5000/login':
        file = r"C:\Users\AC\Desktop\PW\samples1.exe"
        os.startfile(file)
        str = 'executed'
        return str
    else:
        str = 'manual access not allowed'
        return str
    
if __name__ == "__main__":
    app.run()