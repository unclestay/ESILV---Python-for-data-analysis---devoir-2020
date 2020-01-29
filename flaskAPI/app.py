from flask import Flask, render_template, request, redirect, url_for, Blueprint, flash

from function import get_hyperparametres, get_algorithm, get_score, X_train, X_test, Y_train, Y_test

from flask_wtf import Form
'''
from flask_login import LoginManager, login_user, logout_user, current_user, login_required'''

from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import os

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


class MyForm(Form):
    n_estimators = StringField(label="n_estimators")
    #max_features = StringField(label="max_features")
    #max_depth = StringField(label="max_depth")
    random_forest = SubmitField(label="random_forest",validators=[DataRequired()])



@app.route('/index', methods=['POST', 'GET'])
def inputParameters():
    form = MyForm()
    if request.method == "POST":
        print('345')
        if form.validate_on_submit():
            if form.random_forest.data:
                n_estimators = request.form['n_estimators']
                #max_features = request.form["max_features"]
                #max_depth = request.form["max_depth"]
                print("678")
                return redirect(url_for('getNewModel', n_estimators=n_estimators))
    print("123")
    return render_template("index.html", form=form)


@app.route('/accuracy', methods=["POST", "GET"])
def getAccuracy():
    algorithm = get_algorithm(n_estimators=10,max_features=9,max_depth=10)
    accuracy = get_score(algorithm, X_train, X_test, Y_train, Y_test)
    return render_template('accuracy.html', accuracy=accuracy)


@app.route('/getNewModel/<int:n_estimators>', methods=["POST", "GET"])
def getNewModel(n_estimators):
    algorithm = get_algorithm(n_estimators, 9, 10)
    return render_template('getNewModel.html', algorithm=algorithm)


if __name__ == '__main__':
    app.run(debug=True, port=3000)
