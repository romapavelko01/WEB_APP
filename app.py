from flask import Flask, request, render_template, redirect, url_for
from Lab_3_3.main import main_func


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def opening_page():
    if request.method == 'GET':
        return render_template('initial.html')
    elif request.method == 'POST':
        acc_got = request.form['Enter']
        main_func(acc_got)
        return redirect(url_for('get_data'))


@app.route('/MyMap', methods=['GET'])
def get_data():
    return render_template('MyMap.html')


if __name__ == "__main__":
    app.run()


