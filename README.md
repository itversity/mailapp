# Mail Application

## Setup Project

Here are the steps involved in setup project.
* Clone the Git Repository.
* Ensure Python 3.11 is setup. It might work Python 3.9 as well as 3.10.
* Create Python Virtual Environment and activate it.
* Install required dependencies using `requirements.txt`.

```shell
git clone https://github.com/itversity/mailapp.git
python -m venv ma-venv
source ma-venv/bin/activate # On Windows ma-venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Generate Test Data

Here are the steps involved in generating test data. The test data will be populated in Mongodb Collection.
* Make sure Python Virtual Environment is activated and dependencies are installed.
* Make sure Mongo DB is up and running.
* Set Environment Variables to connect to the database.
* Run `gen_data.py`.

```shell
export MONGO_HOST=localhost
export MONGO_PORT=27017

python gen_data.py
```

## Validate Sending Emails

Here are the steps involved to validate sending emails using the test data.
* Make sure Python Virtual Environment is activated and dependencies are installed.
* Make sure Mongo DB is up and running.
* Set Environment Variables to connect to the database.
* Set Environment Variables for Sendgrid API Key and from email.
* Run `app.py`.

```shell
export MONGO_HOST=localhost
export MONGO_PORT=27017
export SENDGRID_API_KEY=<SENDGRID_API_KEY>
export FROM_EMAIL=<VERIFIED_SENDGRID_EMAIL>
python app.py
```
