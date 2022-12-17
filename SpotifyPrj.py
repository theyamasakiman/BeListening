from flask import Flask, request, redirect, render_template


from wtforms import Form, StringField, SelectField, validators, SubmitField

class SpotifyAccess(Form):
    artistname = StringField('artist name', [validators.Length(min=4, max=25)])
    year = StringField('year', [validators.NumberRange(min=1980, max=2022)])
    genre_list = ('Hip Hop','Pop','Rock','Rhythm and Blues','Jazz','Classical','Dance','Soul','Disco','Rap','Blues','Drill')
    genre = SelectField(label = 'genre', choices = genre_list)
    submit = SubmitField('submit')



app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    form = SpotifyAccess(request.form)
    if request.method == 'GET' and form.validate():
        artist = form.artistname.data
        year = form.year.data,
        data = form.genre.data
        # return redirect(url_for('login'))
    #return render_template('register.html', form=form)
        return '<p>successful</p>'
    else:
        return '<p>Not Successful</p>'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)