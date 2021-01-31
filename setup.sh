## Usage: `source ./setup_environment.sh`
##
## Copyright (c) 2021 John Paul Krieg

# support the following environment variables
# - EMAIL_USER              google account username - used for automated emails
# - EMAIL_PASS              google account passname - used for automated emails
# - SQLALCHEMY_DATABASE_URI URI for database
# - SECRET_KEY              secret key for security purposes

printf "Enter your google account credentials for automated emails:\n"
printf "(note: you'll need to enable 'Less secure app access' for the account)\n"
printf "username: "
read var_email_username
export EMAIL_USER=$var_email_username
printf "password: "
read var_email_password
export EMAIL_PASS=$var_email_password
printf "\n"

printf "Database URI: "
read var_sqlalchemy_database_uri
export SQLALCHEMY_DATABASE_URI=$var_sqlalchemy_database_uri

function getSecretKey {
python3 - <<END
import secrets
print(secrets.token_hex(16))
END
}

var_secret_key=$(getSecretKey)
export SECRET_KEY=$var_secret_key

printf "\nSUMMARY:\n"
printf "> EMAIL_USER =                $var_email_username\n"
printf "> EMAIL_PASS =                $var_email_password\n"
printf "> SQLALCHEMY_DATABASE_URI =   $var_sqlalchemy_database_uri\n"
printf "> SECRET_KEY =                $var_secret_key\n"