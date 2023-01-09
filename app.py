from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    real = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.id


@app.route('/')
@app.route('/home')
def index():
    return render_template("home.html")


@app.route('/reg', methods=['POST', 'GET'])
def create_article():
    if request.method == "POST":
        name = request.form['name']
        real = request.form['real']
        password = request.form['password']

        user = User(name=name, real=real, password=password)

        try:
            db.session.add(user)
            db.session.commit()
            return redirect('/home')
        except:
            return "При добавлении пользователя произошла ошибка"
    else:
        return render_template("reg.html")


@app.route('/reg', methods=['POST', 'GET'])
def reg():
    if request.method == "POST":
        name = request.form['name']
        real = request.form['real']
        password = request.form['password']

        user = User(name=name, real=real, password=password)

        try:
            db.session.add(user)
            db.session.commit()
            return redirect('/yes')
        except:
            return "При добавлении пользователя произошла ошибка"
    else:
        return render_template("reg.html")


@app.route('/log', methods=['POST', 'GET'])
def log():
    if request.method == "POST":
        return redirect('/rootpage')
    else:
        return render_template("log.html")


@app.route('/yes')
def yes():
    return render_template("yes.html")


@app.route('/rootpage')
def rootpage():
    users = User.query.order_by(User.date.desc()).all()
    return render_template("rootpage.html", users=users)

@app.route('/rootpage/<int:id>')
def active(id):
    user = User.query.get(id)
    return render_template("active.html", user=user)


@app.route('/rootpage/<int:id>/delete')
def post_delete(id):
    user = User.query.get_or_404(id)
    try:
        db.session.delete(user)
        db.session.commit()
        return redirect('/rootpage')
    except:
        return "При удалении пользователя произошла ошибка"


@app.route('/rootpage/<int:id>/info')
def info(id):
    user = User.query.get(id)
    return render_template("info.html", user=user)

@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)