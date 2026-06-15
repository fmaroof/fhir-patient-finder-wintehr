# fhir-patient-finder-wintehr

This is a FHIR web application written in Python and using Flask as the backend.

## 1. Clone the repository

```bash
git clone https://github.com/fmaroof/fhir-patient-finder-wintehr.git
cd fhir-patient-finder-wintehr
``` 

## 2. Before running the app

We use environment variables to configure the app. 

1. Copy the template configuration file by running this command in your terminal:
   ```bash
   cp .env.example .env
   ```
2. Open your new `.env` file and fill in the missing values.
3. Assign yourself a unique 4 or 5-digit `FHIR_PORT` (e.g., 8080) so you don't conflict with other students on the OSCAR cluster. 
*(Note: Authentication is currently disabled, so you can leave username/password blank for now).*

## 3. Running the App

We begin by creating a Python virtual environment using the `venv` module. This is done by running the command below from the "root" of this repo. 

```
/usr/bin/python3 -m venv venv        # create a virtual environment called venv

source venv/bin/activate             # activate our virtual environment

pip3 install -r requirements.txt     # install all our dependencies into the virtual environment
```


After the above steps, we should be able to launch our app using the following command.

```
python3 src/app.py
```


This will start the app on the port you set in the `FHIR_PORT` environment variable (default: `5000` if not set). For example, if you set `FHIR_PORT=5000` in your `.env` you can open:

```
http://localhost:5000
```

The exact URL and port are also printed in the terminal output when the app starts.


