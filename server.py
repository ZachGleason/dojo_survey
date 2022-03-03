from flask import Flask,  render_template,  redirect, request, session
app = Flask(__name__)
app.secret_key = "SECRET"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process_user():
    session["your_name"] = request.form['your_name']
    session["location"]= request.form['location']
    session["language"] = request.form['language']
    session["comment"] = request.form['comment']
    return redirect("/results")

@app.route('/results')
def sucess():
    return render_template("results.html")

if __name__ == "__main__":
    app.run(debug=True)