from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/home", methods=["GET"])
def home_Page():
    print("Request reached server")
    if request.method == "GET":
        return render_template("home.html", data="")

if __name__ == '__main__':
    app.run(debug=False)