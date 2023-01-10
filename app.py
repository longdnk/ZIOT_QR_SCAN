from flask import *
import requests

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
app.config["CACHE_TYPE"] = "null"
key = '3254-WRG5EUSZNQJH2K2R75LAAREVLMQK7FE6CVZH94KBH2RY3QVB2RKNU829QLVP2CTQ-SRRR74XCR3U7AALPAXRND5TPTA6Y3B2HDEFSUL84LACQS9SADDTCDWERQJGTWSHW'
passkey = 'wvvjumsfoylhuvlg'
constants = (1 << 1) + (1 << 3)


@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    return render_template('index.html')


def encrypt(text, s):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result


@app.route('/contact', methods=['POST'])
def send():
    name = request.values['fullname']
    time = request.values['datecheck']
    splitName = name.split(': ')
    eName = splitName[1]
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        # region Login
        smtp.login('kimlong101020@gmail.com', encrypt(passkey, -1 * constants))
        # endregion
        subject = name
        body = "Employee name: " + eName + "\nTime check in: " + time + "\n"
        # body = u' '.join((name, email, message)).encode('utf-8').strip()
        # body = r.join((name, '\n', email, '\n', message)).encode('utf-8').strip()
        msg = f'Subject: {subject}\n\n{body}'.encode('utf-8').strip()
        smtp.sendmail('kimlong101020@gmail.com', ['longdnk@ziot.vn', 'thanhdd@ziot.vn', 'vinhlt@ziot.vn'], msg)
    # data = {
    #     'access_token': key,
    #     'username': 'longdnk',
    #     'name': 'Test request',
    #     'approvers': 'vinhlt',
    #     'followers': '',
    #     'content': "Test content",
    # }
    # response = requests.get(urlDomain('https://request.base.vn/'))
    # print(response)
    return redirect(url_for('success'))


# def urlDomain(domain):
#     url = f"https://request." + domain + "/extapi/v1/request/direct/create"
#     return url


@app.route('/success')
def success():
    return render_template('success.html')


if __name__ == '__main__':
    app.jinja_env.cache = {}
    app.run(debug=True, threaded=True, port=3000)
