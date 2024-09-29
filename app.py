from flask import Flask, request, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# In-memory database for users (for demo purposes)
users = {}
login_attempts = []

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

        # Check if the user exists and password matches
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            return "Login failed. Check your username and password."
    return render_template('login.html')


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == 'GET':
        user_input = request.args.get('user_input', '')

        # Intentionally do not sanitize or validate input
        x_forwarded_for = request.headers.get('X-Forwarded-For')

        if x_forwarded_for and '100.0.0.1' in x_forwarded_for:
            flag = get_flag()
            return render_template('dashboard.html', message=f"Welcome, {user_input}! Flag: {flag}")

        return render_template('dashboard.html', message=f"Welcome, {user_input}!")

    return render_template('dashboard.html')



if __name__ == '__main__':
    # Create an access log file and flag.txt for testing purposes
    with open('flag.txt', 'w') as flag_file:
        flag_file.write('HTB{crlf_injection_success}')

    app.run(debug=True)
