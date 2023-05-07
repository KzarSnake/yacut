import random
import string

from flask import flash, redirect, render_template

from . import app, db
from .forms import URLForm
from .models import URLMap


def get_unique_short_id():
    collection = string.ascii_letters + string.digits
    generated_link = ''.join(random.sample(collection, 6))
    return generated_link


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLForm()
    if form.validate_on_submit():
        short_url = form.custom_id.data
        if not short_url:
            short_url = get_unique_short_id()
        elif URLMap.query.filter_by(short=short_url).first():
            flash(f'Имя {short_url} уже занято!')
            return render_template('index.html', form=form)
        urlmap = URLMap(
            original=form.original_link.data,
            short=short_url,
        )
        db.session.add(urlmap)
        db.session.commit()
        return render_template('index.html', form=form, short=short_url)
    return render_template('index.html', form=form)


@app.route('/<string:custom_id>')
def redirect_view(custom_id):
    urlmap = URLMap.query.filter_by(short=custom_id).first_or_404()
    return redirect(urlmap.original)
