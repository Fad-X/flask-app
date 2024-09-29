from flask import Flask, request, render_template, redirect, url_for, session
import re

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# In-memory database for users (for demo purposes)
users = {}
login_attempts = []

# Simple function to simulate logging (vulnerable to CRLF injection)
def log_login_attempt(username, ip):
    with open('access.log', 'a') as log_file:
        # Vulnerable log function where unsanitized username is written to the log
        log_file.write(f"Login attempt: username={username} from {ip}\n")

# Read flag (only accessible from localhost)
def get_flag():
    with open('flag.txt', 'r') as flag_file:
        return flag_file.read()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            return "Username already exists. Please choose another one."
        else:
            users[username] = password
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Log the login attempt (vulnerable to CRLF injection)
        log_login_attempt(username, request.remote_addr)

        # Check if the user exists and password matches
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            return "Login failed. Check your username and password."
    return render_template('login.html')

'''@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))

    # Read the log file to check if the request was forged as from localhost
    with open('access.log', 'r') as log_file:
        log_content = log_file.read()

    if re.search(r'from 100\.0\.0\.1', log_content):
        # If there's a fake localhost access, display the flag
        flag = get_flag()
        return f"<h1>Flag: {flag}</h1>"
    else:
        return "<h1>Welcome to your dashboard</h1><p>You must be localhost to get the flag.</p>"'''


'''@app.route('/dashboard', methods=['GET', 'POST'])

def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))

    # Check if the request is a POST request
    if request.method == 'POST':
        user_input = request.form.get('user_input')

        # Check the log file to see if there was a forged request from localhost
        with open('access.log', 'r') as log_file:
            log_content = log_file.read()

        # Right question to check against
        right_question = "flag"

        if user_input == re.search(r'from 100\.0\.0\.1', log_content):
            # If the user asks the right question and the request was forged from localhost, display the flag
            flag = get_flag()
            return render_template('dashboard.html', message=f"Flag: {flag}")
        elif user_input == right_question:
            # User asked the right question but the request was not from localhost
            return render_template('dashboard.html', message="Wrong question. Try again.")
        else:
            # User asked the wrong question
            return render_template('dashboard.html', message="Wrong question.")
    
    # Default GET request, show the input form
    return render_template('dashboard.html')'''

from flask import Flask, request, render_template, redirect, url_for, session
import re

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# In-memory database for users (for demo purposes)
users = {}
login_attempts = []

# Simple function to simulate logging (vulnerable to CRLF injection)
def log_login_attempt(username, ip):
    with open('access.log', 'a') as log_file:
        # Vulnerable log function where unsanitized username is written to the log
        log_file.write(f"Login attempt: username={username} from {ip}\n")

# Read flag (only accessible from localhost)
def get_flag():
    with open('flag.txt', 'r') as flag_file:
        return flag_file.read()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            return "Username already exists. Please choose another one."
        else:
            users[username] = password
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Log the login attempt (vulnerable to CRLF injection)
        log_login_attempt(username, request.remote_addr)

        # Check if the user exists and password matches
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            return "Login failed. Check your username and password."
    return render_template('login.html')

'''@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))

    # Read the log file to check if the request was forged as from localhost
    with open('access.log', 'r') as log_file:
        log_content = log_file.read()

    if re.search(r'from 100\.0\.0\.1', log_content):
        # If there's a fake localhost access, display the flag
        flag = get_flag()
        return f"<h1>Flag: {flag}</h1>"
    else:
        return "<h1>Welcome to your dashboard</h1><p>You must be localhost to get the flag.</p>"'''


'''@app.route('/dashboard', methods=['GET', 'POST'])

def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))

    # Check if the request is a POST request
    if request.method == 'POST':
        user_input = request.form.get('user_input')

        # Check the log file to see if there was a forged request from localhost
        with open('access.log', 'r') as log_file:
            log_content = log_file.read()

        # Right question to check against
        right_question = "flag"

        if user_input == re.search(r'from 100\.0\.0\.1', log_content):
            # If the user asks the right question and the request was forged from localhost, display the flag
            flag = get_flag()
            return render_template('dashboard.html', message=f"Flag: {flag}")
        elif user_input == right_question:
            # User asked the right question but the request was not from localhost
            return render_template('dashboard.html', message="Wrong question. Try again.")
        else:
            # User asked the wrong question
            return render_template('dashboard.html', message="Wrong question.")
    
    # Default GET request, show the input form
    return render_template('dashboard.html')'''

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        user_input = request.form.get('user_input')

        # Check if the current request comes from 100.0.0.1
        if request.remote_addr == '100.0.0.1':
            # Read the flag if the request is from 100.0.0.1
            flag = get_flag()
            return render_template('dashboard.html', message=f"Welcome, {user_input}! Flag: {flag}")
        
        # Respond with a welcome message if no flag access
        return render_template('dashboard.html', message=f"Welcome, {user_input}!")

    # Default GET request, show the input form
    return render_template('dashboard.html')


@app.route('/logout')
def logout():
    # Clear the session (logout the user)
    session.clear()
    return render_template('logout.html')



if __name__ == '__main__':
    # Create an access log file and flag.txt for testing purposes
    open('access.log', 'w').close()  # Clear log on every run
    with open('flag.txt', 'w') as flag_file:
        flag_file.write('HTB{crlf_injection_success}')

    app.run(debug=True)
                           


@app.route('/logout')
def logout():
    # Clear the session (logout the user)
    session.clear()
    return render_template('logout.html')



if __name__ == '__main__':
    # Create an access log file and flag.txt for testing purposes
    open('access.log', 'w').close()  # Clear log on every run
    with open('flag.txt', 'w') as flag_file:
        flag_file.write('HTB{crlf_injection_success}')

    app.run(debug=True)
                           