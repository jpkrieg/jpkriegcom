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
TODO add information about how to set up nginx and gunicorn here


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