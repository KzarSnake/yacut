from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, Regexp

from settings import PATTERN


class URLForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[
            DataRequired(message='Обязательное поле'),
        ],
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[Length(max=16), Optional(), Regexp(PATTERN)],
    )
    submit = SubmitField('Создать')
