## usage: python setup_wizard.py
##
## Copyright (c) John PauL Krieg
##
## Setup Wizard for jpkrieg.com

import secrets, json, os

# get configuration items from user
config = {}
print("Enter your google account credentials for automated emails:")
config["EMAIL_USER"] = input("username: ")
config["EMAIL_PASS"] = input("password: ")
config["SQLALCHEMY_DATABASE_URI"] = input("Database URI: ")
config["SECRET_KEY"] = secrets.token_hex(16)

# dump json to /tmp/jpkriegcom_config.json
with open("/tmp/jpkriegcom_config.json", "w") as outfile:
	json.dump(config, outfile)

# sudo copy into /etc/
os.system('sudo mv /tmp/jpkriegcom_config.json /etc/jpkriegcom_config.json')

# set up database
from jpkriegcom import db, create_app
db.create_all(app=create_app())
