from app.main import app
from flask import url_for, redirect


@app.route("/image/icon.png")
def icon_png():
    return redirect(url_for("static", filename='img/png/icon.png'))


@app.route("/image/gold.png")
def gold_png():
    return redirect(url_for("static", filename='img/png/gold.png'))


@app.route("/image/user.png")
def user_png():
    return redirect(url_for("static", filename='img/png/user.png'))


@app.route("/image/article.png")
def article_png():
    return redirect(url_for("static", filename='img/png/article.png'))
