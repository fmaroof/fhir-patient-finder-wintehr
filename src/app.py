import requests
import os
import urllib3
from flask import Flask, request, render_template
from dotenv import load_dotenv


app = Flask(__name__)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

load_dotenv()

FHIR_SERVER_BASE_URL=os.getenv("FHIR_SERVER_BASE_URL")
username = os.getenv("FHIR_USERNAME")
password = os.getenv("FHIR_PASSWORD")

def request_patient(patient_id, credentials):

    req = requests.get(FHIR_SERVER_BASE_URL + "/Patient/" + str(patient_id), auth = credentials, verify=False)

    print(f"Requests status: {req.status_code}")

    response = req.json()
    print(response.keys())

    return response



@app.route('/', methods=['GET', 'POST'])
def index():

    result = None
    credentials = (username, password)

    if request.method == 'POST':
        number = request.form.get('number', '').strip()
        if not number:
            result = 'Invalid input. Please enter a patient ID.'
        else:
            result = request_patient(number, credentials=credentials)

    return render_template('index.html', result=result)

if __name__ == '__main__':
    port = int(os.environ.get('FHIR_PORT', 5001))
    app.run(debug=True, port=port)