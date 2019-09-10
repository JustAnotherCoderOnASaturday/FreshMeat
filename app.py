from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/reads')
def reads():
    """Documentations that I have written, like reverse engi, or instructions"""
    return render_template('Writing.html')


@app.route('/projects')
def fun():
    """Downloads and stuff"""
    return render_template('projects.html')


@app.route('/experiments')
def experiment():
    """You Shouldn't be on this page my dude"""
    return 'You Shouldnt be here Sir.'


if __name__ == '__main__':
    """This Project Was created Sept. 9 2018"""
    app.run()
