# from flask import Flask, render_template, request, redirect
# from flask_sqlalchemy import SQLAlchemy
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
#
#
# сlass User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     relname = db.Column(db.String(100), nullable=False)
#     password = db.Column(db.String(100), nullable=False)
#
#     def __repr__(self):
#         return '<User %r>' % self.id
#
#
# @app.route('/')
# @app.route('/home')
# def index():
#     return render_template("home.html")
#
#
# @app.route('/log')
# def log():
#     return render_template("log.html")
#
#
# @app.route('/reg', methods=['POST', 'GET'])
# def reg():
#     if request.method == "POST":
#         name = request.form['name']
#         relname = request.form['relname']
#         password = request.form['password']
#         user = User(name=name, relname=relname, password=password)
#         try:
#             db.session.add(User)
#             db.session.commit()
#             return redirect('/home')
#         except:
#             return "При добавлении пользователя произошла ошибка"
#     else:
#         return render_template("reg.html")
#
#
# @app.route('/about')
# def about():
#     return render_template("about.html")
#
#
# if __name__ == "__main__":
#     app.run(debug=True)