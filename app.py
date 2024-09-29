from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>CRLF Injection Demo</h1>
    <form action="/setcookie" method="GET">
        <label for="username">Enter your username:</label>
        <input type="text" id="username" name="username">
        <input type="submit" value="Set Cookie">
    </form>
    '''

@app.route('/setcookie')
def set_cookie():
    # Get the 'username' parameter from the URL (potentially malicious input)
    username = request.args.get('username', '')
    
    # Create a response object
    response = make_response(f"Hello, {username}!")
    
    # Set the username in the cookie without sanitization (vulnerable to CRLF injection)
    response.headers['Set-Cookie'] = f"user={username}"
    
    return response

if __name__ == '__main__':
    app.run(debug=True)
