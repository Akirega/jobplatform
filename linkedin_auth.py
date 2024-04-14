import requests
from flask import Flask, redirect, request, session, jsonify

app = Flask(__name__)
app.secret_key = 'Tc_D9vfg2OYAP_3TE5k6Hvnjyuvsg9tk'  # Replace 'your_secret_key' with your actual secret key

# LinkedIn API credentials
CLIENT_ID = '86vd9gvdutpb1m'
CLIENT_SECRET = 'Gh7yG8Et8D30kbXv'
REDIRECT_URI = 'https://akirega.github.io/jobplatform/'  # Replace with your new redirect URI

# Endpoint to initiate the OAuth 2.0 authorization flow
@app.route('/auth/linkedin')
def auth_linkedin():
    # Redirect the user to the LinkedIn authorization URL
    authorization_url = f'https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope=r_liteprofile'
    return redirect(authorization_url)

# Callback endpoint to handle the authorization code and exchange it for an access token
@app.route('/auth/linkedin/callback')
def auth_callback():
    # Exchange the authorization code for an access token
    code = request.args.get('code')
    token_url = 'https://www.linkedin.com/oauth/v2/accessToken'
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }
    response = requests.post(token_url, data=data)
    access_token = response.json()['access_token']

    # Store the access token in the session
    session['access_token'] = access_token

    return redirect('/profile')

# Endpoint to retrieve user profile data
@app.route('/profile')
def profile():
    # Retrieve user profile data using the access token
    access_token = session.get('access_token')
    headers = {'Authorization': f'Bearer {access_token}'}
    profile_url = 'https://api.linkedin.com/v2/me'
    response = requests.get(profile_url, headers=headers)
    profile_data = response.json()

    return jsonify(profile_data)

from flask import send_file

# Route for the root URL
@app.route('/')
def index():
    return send_file('index.html')


if __name__ == '__main__':
    app.run(debug=True)
