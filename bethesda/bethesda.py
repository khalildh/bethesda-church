from flask import Flask, render_template, url_for

app=Flask(__name__)


@app.route('/')
def home():
    context = {
        'title': 'HOME',
        'stylesheet': url_for('static', filename='css/cover.css')
    }
    return render_template("home.html", context=context)

@app.route('/info')
def info():
    context = {
        'title': 'LANDING',
        'stylesheet': url_for('static', filename='css/carousel.css')
    }
    return render_template("info.html", context=context)



if __name__=="__main__":
    app.run(debug=True)
