from flask import Flask, render_template
app= Flask(__name__)
@app.route('/')
def home():
    return "<h1>Hello, Flask!</h1>"

@app.route("/about")
def about():
    return render_template("about.html")

def bad_func():
    print("this will fail flake8 test :()")
if __name__ == "__main__":
    app.run(debug=True)