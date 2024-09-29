// Simple script for logging message when page is loaded
document.addEventListener('DOMContentLoaded', () => {
    console.log('Welcome to the CRLF Vulnerable App!');
});

document.addEventListener('DOMContentLoaded', () => {
    console.log('Login page loaded.');
    const form = document.querySelector('form');

    form.addEventListener('submit', (event) => {
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        if (username === '' || password === '') {
            alert('Both fields are required!');
            event.preventDefault();
        }
    });
});

document.addEventListener('DOMContentLoaded', () => {
    console.log('Logout page loaded.');
});

document.addEventListener('DOMContentLoaded', () => {
    console.log('Register page loaded.');
});

document.addEventListener('DOMContentLoaded', () => {
    console.log('Dashboard page loaded.');
});
