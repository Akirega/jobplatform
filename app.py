from flask import Flask
from linkedin_auth import auth_linkedin, auth_callback, profile, index
from job_handler import post_job, update_job, delete_job

app = Flask(__name__)

# Routes for LinkedIn authentication
app.add_url_rule('/auth/linkedin', 'auth_linkedin', auth_linkedin)
app.add_url_rule('/auth/linkedin/callback', 'auth_callback', auth_callback)

# Route for retrieving user profile data
app.add_url_rule('/profile', 'profile', profile)

# Route for the root URL
app.add_url_rule('/', 'index', index)

# Routes for job handling
app.add_url_rule('/postJob', 'post_job', post_job, methods=['POST'])
app.add_url_rule('/updateJob/<int:job_id>', 'update_job', update_job, methods=['PUT'])
app.add_url_rule('/deleteJob/<int:job_id>', 'delete_job', delete_job, methods=['DELETE'])

if __name__ == '__main__':
    app.run(debug=True)
