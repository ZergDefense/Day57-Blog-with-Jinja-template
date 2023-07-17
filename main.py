import datetime
import random
import requests as requests
from flask import Flask, render_template

app = Flask(__name__)


def get_gender(entered_name):
    url = "https://api.genderize.io/"
    parameters = {
        "name": entered_name
    }
    response = requests.get(url=url, params=parameters).json()
    print(response)
    return response["gender"]


def get_age(entered_name):
    url = "https://api.agify.io/"
    parameters = {
        "name": entered_name
    }
    response = requests.get(url=url, params=parameters).json()
    print(response)
    return response["age"]


@app.route('/')
def home():
    random_number = random.randint(1, 1000)
    footer_year = datetime.date.today().year
    return render_template("index.html", random_number=random_number, footer_year=footer_year)


@app.route('/guess/<name>')
def guess(name):
    name = name.title()
    gender = get_gender(entered_name=name)
    age = get_age(entered_name=name)
    return render_template("guess.html", name=name, gender=gender, age=age)


@app.route('/blog/<int:num>')
def get_blog(num):
    all_posts = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("blog.html", posts=all_posts, blog_id=num)


if __name__ == "__main__":
    app.run(debug=True)

