#!/usr/bin/env python3
"""
Adding the `getlocale` function to determine the best match language
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


app = Flask(__name__)
babel = Babel(app)


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


@app.route('/', strict_slashes=False)
def hello_i18n():
    """single page using flask"""
    return render_template('3-index.html')


if __name__ == "__main__":
    """Main Function"""
    app.run(host='0.0.0.0', port=5000)
