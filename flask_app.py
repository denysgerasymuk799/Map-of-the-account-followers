"""module to generate flask app"""
from flask import Flask, render_template, request
from map_followers import create_followers_map

app = Flask(__name__)


@app.route('/', methods=['GET'])
def start():
    """

    :return: input_account.html - form to enter an account
    """
    return render_template('input_account.html')


@app.route('/input_account', methods=['POST'])
def input_account():
    """

    :return: Account follower\' locations.html - if an account exists, else -  input_account.html
    """
    try:
        if len(request.form["account"]) >= 1:
            create_followers_map(request.form["account"])
            return render_template('Account follower\' locations.html')

        else:
            error = 'Enter right account'
            print("error")
            return render_template('input_account.html', error=error)

    except NameError:
        print('input_account error flask_app.py ')


if __name__ == '__main__':
    app.run(debug=True)
