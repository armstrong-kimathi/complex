from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def home():
    cities = ["Nairobi","Mombasa","Kampala","Abuja","New York","London"]
    return render_template("index.html",cities=cities)


if __name__ == '__main__':
    app.run()
