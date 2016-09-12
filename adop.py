#!/usr/bin/env python

from flask import Flask, abort, render_template
from jinja2.exceptions import TemplateNotFound


app = Flask(__name__)
REGIONS = ('Rhône-Alpes',)


@app.route('/')
@app.route('/<page>')
@app.route('/region-<any{}:region>/'.format(REGIONS))
@app.route('/region-<any{}:region>/<page>'.format(REGIONS))
def page(page='home', region=None):
    try:
        return render_template(
            '{}.html'.format(page), page=page, region=region)
    except TemplateNotFound:
        abort(404)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    from sassutils.wsgi import SassMiddleware
    app.wsgi_app = SassMiddleware(
        app.wsgi_app, {'adop': ('static', 'static', '/static')})
    app.run(debug=True, host='0.0.0.0')
