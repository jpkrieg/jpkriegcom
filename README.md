# jpkrieg.com
Copyright (c) 2021 John Paul Krieg

## setup
### debugging
```
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
source setup.sh
python run.py
```

Set up your google account to allow "Less secure app access" so the application can send password reset emails on your behalf via gmail

### production deployment
#### get and set up the app
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
source setup.sh

##### make sure nginx is installed
sudo apt install nginx

#### remove the default nginx configuration
sudo rm /etc/nginx/sites-enabled/default

#### create a custom nginx configuration for the site
sudo nano /etc/nginx/sites-enabled/jpkriegcom
```
server {
	listen 80;
        server_name jpkrieg.com;

        location /static {
		alias /home/john/jpkriegcom/jpkriegcom/static;
        }

        location / {
                proxy_pass http://localhost:8000;
                include /etc/nginx/proxy_params;
                proxy_redirect off;
	}
}
```

#### set up ufw
TODO - add documentation

#### set up supervisor to monitor the gunicorn process
sudo apt install supervisor
sudo nano /etc/supervisor/conf.d/jpkriegcom.conf
```
[program:jpkriegcom]
directory=/home/john/jpkriegcom
command=/home/john/jpkriegcom/venv/bin/gunicorn -w 9 run:app
user=john
autostart=true
autorestart=true
stopasgroup=true
killasgroup=true
stderr_logfile=/var/log/jpkriegcom/jpkriegcom.err.log
stdout_logfile=/var/log/jpkriegcom/jpkriegcom.out.log
```
#### set up supervisor's log files
```
sudo mkdir -p /var/log/jpkriegcom
sudo touch /var/log/jpkriegcom/jpkriegcom.err.log
sudo touch /var/log/jpkriegcom/jpkriegcom.out.log
sudo supervisorctl reload
```

####(optional) Increase nginx default upload file size limit from 2MB to 5MB
sudo nano /etc/nginx/nginx.conf
add `client_max_body_size 5M;` below the `types_hash_max_size` attribute.

Production Deployment logs:
| Filename					| Contents					|
| ---------------------------------------------	| ---------------------------------------------	|
| /var/log/jpkriegcom/jpkriegcom.err.log	| stderr from supervisor running gunicorn	|
| /var/log/jpkriegcom/jpkriegcom.out.log	| stdout from supervisor running gunicorn	|


## TODOs
- update readme to include production deployment instructions
- add unit tests
- I should add the following to the code that handles saving pictures to remove the user's old picture (but I'll also need to add a check to see if the user's photo was the default photo)
```
prev_picture = os.path.join(app.root_path, 'static/profile_pics', current_user.image_file)
    if os.path.exists(prev_picture):
        os.remove(prev_picture)
```

## ideas
- host wiki

## acknowledgements
Corey Schafer's FlaskBlog tutorial helped me relearn Flask [GitHub](https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Flask_Blog) [YouTube](https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=1)
