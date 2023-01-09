from flask import *

import smtplib

app = Flask(__name__)
# key sec
app.config['SECRET_KEY'] = "testAdmin@123456"
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'myemail@gmail.com'
app.config['MAIL_PASSWORD'] = 'none'
app.config['MAIL_USE_SSL'] = True
app.config['authentication'] = True


@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def send():
    name = request.values['fullname']
    time = request.values['datecheck']
    email = 'test email'
    message = 'test msg'
    splitName = name.split(': ')
    eName = splitName[1]

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        # region Login
        smtp.login('kimlong101020@gmail.com', 'mllzkciveobxklbw')
        # endregion
        subject = name
        body = "Employee name: " + eName + "\nTime check in: " + time + "\n"
        # body = u' '.join((name, email, message)).encode('utf-8').strip()
        # body = r.join((name, '\n', email, '\n', message)).encode('utf-8').strip()
        msg = f'Subject: {subject}\n\n{body}'.encode('utf-8').strip()
        smtp.sendmail('kimlong101020@gmail.com', 'longdnk@ziot.vn', msg)
    return redirect(url_for('success'))

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.jinja_env.cache = {}
    app.run(debug=True, threaded=True)
