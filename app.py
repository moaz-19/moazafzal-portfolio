from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = "your-secret-key"

# === Configure Flask-Mail (example for Gmail SMTP, change for your provider) ===
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your.email@gmail.com'       # Change!
app.config['MAIL_PASSWORD'] = 'your-gmail-app-password'     # Change!
app.config['MAIL_DEFAULT_SENDER'] = 'your.email@gmail.com'  # Change!

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/experience')
def experience():
    return render_template('experience.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        try:
            msg = Message(
                subject=f"New Portfolio Message from {name}",
                sender=email,
                recipients=['your.email@gmail.com'],  # Change to your receiving address
                body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            )
            mail.send(msg)
            flash("Thank you, your message has been sent!")
        except Exception as e:
            flash("Sorry, something went wrong. Please try again later.")
        return redirect(url_for('contact'))
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)