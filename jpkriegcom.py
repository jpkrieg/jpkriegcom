from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'John Paul Krieg',
        'title': 'Blog Post 1',
        'content': 'First post content.',
        'date_posted': 'January 8, 2021'
    },
    {
        'author': 'Lori Bower',
        'title': 'Blog Post 2',
        'content': 'Second post content.',
        'date_posted': 'January 19, 2021'
    }
]

@app.route("/")
@app.route("/home")
def hello():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title='About')

# __name__ is only ever __main__ when you run from python direcrly
# if we import this modeule somewhere else it will not be __main__ and we will not run in debug mode
if __name__ == "__main__":
    app.run(debug=True)