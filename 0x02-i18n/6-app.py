#!/usr/bin/env python3
"""
Adding the `getlocale` function to determine the best match language
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale():
    """The config class for flask application"""
    request_lang = request.args.get('locale', None)
    if request_lang and request_lang in app.config['LANGUAGES']:
        return request_lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


class Config:
    """The config class for flask application"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


def get_user():
    """Returns a user dictionary or None if the ID cannot be found or if
    login_as was not passed
    """
    user_id = request.args.get('login_as', None)
    if user_id is None or not user_id.isdigit():
        return None
    return users.get(int(user_id))


@app.before_request
def middleware():
    """find loged in user, and set it as a global on flask.g.user"""
    g.user = get_user()


@app.route('/', strict_slashes=False)
def hello_i18n():
    """single page using flask"""
    return render_template('5-index.html')


if __name__ == "__main__":
    """Main Function"""
    app.run(host='0.0.0.0', port=5000)
