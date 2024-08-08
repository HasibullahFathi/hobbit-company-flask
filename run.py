import os
import json
from flask import Flask, render_template, request, flash

# import env if the system finds a env.py file
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    data = []
    with open('data/company.json', 'r') as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title = 'About', company = data)


@app.route('/about/<member_name>')
def about_about(member_name):
    member = {}
    with open('data/company.json', 'r') as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj['url'] == member_name:
                member = obj
    return render_template('member.html', member=member)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        flash('Thanks {}, Your message has been sent!'.format(
            request.form.get("name")))
        # print(request.form.get('name')) # if name doesn't exist it shows NON 
        # print(request.form["email"]) # if we don't have an email address then it throws an exception
    return render_template("contact.html", page_title = 'Contact')


@app.route('/careers')
def careers():
    return render_template("careers.html", page_title = 'Careers')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0', 
        port=int(os.environ.get('PORT', 5000)),
        debug=True,  # Enable debugging mode for easier development
        )