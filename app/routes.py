from flask import Blueprint, request, redirect, render_template, url_for, flash
from .models import URL
from . import db
import string
import random
import validators

main = Blueprint('main', __name__)

def generate_short_url():
    characters = string.ascii_letters + string.digits
    while True:
        short_url = ''.join(random.choice(characters) for _ in range(6))
        if not URL.query.filter_by(short_url=short_url).first():
            break
    return short_url

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        long_url = request.form['long_url']
        if not validators.url(long_url):
            flash('Invalid URL. Please enter a valid URL.')
            return redirect(url_for('main.index'))

        if not long_url.startswith('http://') and not long_url.startswith('https://'):
            long_url = 'http://' + long_url

        short_url = generate_short_url()
        new_url = URL(long_url=long_url, short_url=short_url)
        db.session.add(new_url)
        db.session.commit()

        flash(f'Short URL created: {request.url_root}{short_url}')
        return redirect(url_for('main.index'))

    urls = URL.query.all()
    return render_template('index.html', urls=urls)

@main.route('/<short_url>')
def redirect_to_long_url(short_url):
    url = URL.query.filter_by(short_url=short_url).first()
    if url:
        url.clicks += 1
        db.session.commit()
        return redirect(url.long_url)
    else:
        flash('Short URL not found.')
        return redirect(url_for('main.index'))
