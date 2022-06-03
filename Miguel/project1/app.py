from flask import Flask, request, render_template, redirect, url_for
from repository.database import check_user_info

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login' , methods=['GET'])
def confirm_user():
    if check_user_info(request.form):
        return render_template('account.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)