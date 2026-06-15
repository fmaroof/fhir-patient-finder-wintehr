# fhir-patient-finder-wintehr

This is a FHIR web application written in Python and using Flask as the backend.

## 1. Dependencies
This app depends on Python 3 and a few Python packages outlined in the `requirements.txt` file. 

## 2. Before running the app

We use environment variables to configure the app. 

1. Duplicate the `.env.example` file and rename the copy to exactly `.env`.
2. Open your new `.env` file and fill in the missing values. 
3. Assign yourself a unique 4 or 5-digit `FHIR_PORT` (e.g., 8080) so you don't conflict with other students on the OSCAR cluster. 
*(Note: Authentication is currently disabled, so you can leave username/password blank for now).*

## 3. Running the App

We begin by creating a Python virtual environment using the `venv` module. This is done by running the command below from the "root" of this repo. 

```
/usr/bin/python3 -m venv venv                 # create a virtual environment called venv

source venv/bin/activate             # activate our virtual environment

pip3 install -r requirements.txt     # install all our dependencies into the virtual environment
```


After the above steps, we should be able to launch our app using the following command.

```
python3 src/app.py
```


This will start the app on port "FHIR_PORT". You can open your preferred browser and see the app running on `http://localhost:FHIR_PORT` replace the FHIR_PORT with the actual port number assigned to you. 
The exact URL to the app can also be found on the terminal output after running the app.


