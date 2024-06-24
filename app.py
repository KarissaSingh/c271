from flask import Flask, request, jsonify, render_template
from faker import Faker
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import SyncGrant


app = Flask(__name__)
fake = Faker()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/token')
def generate_token():
    #add your twilio credentials 
    TWILIO_ACCOUNT_SID = 'AC404f7bbb2a8b4f40f282c957c5f8c477'
    TWILIO_SYNC_SERVICE_SID = 'IS3c04777aafcbc96ab285ed09e6d608fd'
    TWILIO_API_KEY = 'SKd132e020fbda4257b06f91f1a6abd9d6'
    TWILIO_API_SECRET = 'nhid4oTtz2C1KeiubAJ5Dj9dRjIEL1FN'


    username = request.args.get('username', fake.user_name())
    token = AccessToken(TWILIO_ACCOUNT_SID, TWILIO_API_KEY, TWILIO_API_SECRET, identity=username)
    sync_grant_access = SyncGrant(TWILIO_SYNC_SERVICE_SID)
    token.add_grant(sync_grant_access)
    return jsonify(identity=username, token=token.to_jwt().decode())

@app.route('/',methods=['POST'])

def download_text():
    textfromnotepad=request.form['text']
    with open('file.txt','w') as f:
        f.write(textfromnotepad)
    return send_file('file.txt',as_attachment=True)    

if __name__ == "__main__":
    app.run(port=5001)

