from flask import Flask, render_template
from mocks import Post

app = Flask(__name__)


@app.context_processor
def utility_processor():
    def pluralise(count, singular, plural=None):
        if not isinstance(count, int):
            raise ValueError('{} must be an integer'.format(count))
        if plural is None:
            plural = singular + 's'

        if count == 1:
            result = singular
        else:
            result = plural
        return "{} {}".format(count, result)

    return dict(pluralise=pluralise)


@app.route('/')
def home():
    posts = Post.all()
    return render_template('pages/home.html', posts=posts)


@app.route('/map/<int:id>')
def blog(id):
    post = Post.find(id)
    return render_template('blogs/blog.html', post=post)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('pages/404.html', error=error), 404


if __name__ == '__main__':
    app.run()
