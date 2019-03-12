from flask import Flask,render_template       # import flask and flask application for web


# Adding Comments To This File Which Needed For This Situation

app = Flask(__name__)          # defining App

@app.route('/')                # giving route to the app for home page
def home():
    return render_template('home.html')

@app.route('/about/')          # giving reference for about page 
def About():
    return render_template('about.html')

if __name__ == "__main__":    # running app
    app.run(debug= True)
