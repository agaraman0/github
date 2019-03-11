from flask import Flask,render_template


# Adding Comments To This File Which Needed For This Situation

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about/')
def About():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug= True)
