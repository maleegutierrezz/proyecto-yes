from flask import Flask

app= Flask(__name__)

@app.route('/prueba')
def prueba():
    return render_template("prueba.html")
