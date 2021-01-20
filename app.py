from flask import Flask, url_for, redirect, render_template
from forms import ContactForm, RegisterForm


app = Flask(__name__, instance_relative_config=False)
app.config.from_object('config.Config')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template('forms.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template('signup.html', form=form)


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/success')
def success():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)
