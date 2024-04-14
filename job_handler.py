from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy job data (replace with actual data storage mechanism)
jobs = []

# Endpoint to post a new job
@app.route('/postJob', methods=['POST'])
def post_job():
    job_data = request.json
    
    # Validate job data (e.g., ensure all required fields are present)
    if 'title' not in job_data or 'description' not in job_data:
        return jsonify({'error': 'Title and description are required.'}), 400
    
    # Add the job to the list of jobs (replace with actual data storage logic)
    jobs.append(job_data)
    
    return jsonify({'message': 'Job posted successfully.'}), 201

# Endpoint to update an existing job
@app.route('/updateJob/<int:job_id>', methods=['PUT'])
def update_job(job_id):
    job_data = request.json
    
    # Find the job by its ID (replace with actual data retrieval logic)
    job = next((job for job in jobs if job.get('id') == job_id), None)
    if job is None:
        return jsonify({'error': 'Job not found.'}), 404
    
    # Update job data (replace with actual data update logic)
    job.update(job_data)
    
    return jsonify({'message': 'Job updated successfully.'}), 200

# Endpoint to delete a job
@app.route('/deleteJob/<int:job_id>', methods=['DELETE'])
def delete_job(job_id):
    # Find the job by its ID (replace with actual data retrieval logic)
    job = next((job for job in jobs if job.get('id') == job_id), None)
    if job is None:
        return jsonify({'error': 'Job not found.'}), 404
    
    # Remove the job from the list of jobs (replace with actual data deletion logic)
    jobs.remove(job)
    
    return jsonify({'message': 'Job deleted successfully.'}), 200

if __name__ == '__main__':
    app.run(debug=True)
