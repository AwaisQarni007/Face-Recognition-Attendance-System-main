from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == 'your_username' and password == 'your_password':
        try:
            # Execute the Python script
            subprocess.run(['python', 'AMS_Run.py'], check=True)
            return 'Python file executed successfully.'
        except subprocess.CalledProcessError:
            return 'Error executing Python file.'
    else:
        return 'Invalid username or password'

if __name__ == '__main__':
    app.debug()
    app.run()
