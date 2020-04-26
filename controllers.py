from flask import render_template
from aplicacao import app

@app.route('/teste')
def index():
    return render_template('index.html')

app.run(debug=True)