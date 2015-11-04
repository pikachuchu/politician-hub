from flask import Flask, render_template, jsonify, make_response, abort
from api import api

app = Flask(__name__)

app.register_blueprint(api, url_prefix='/api/v1')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/senate')
def senate():
    return render_template('senate.html')

@app.route('/house')
def house():
    return render_template('house.html')

@app.route('/committees')
def committees():
    return render_template('committees.html')

@app.route('/bills')
def bills():
    return render_template('bills.html')

@app.route('/about')
def about():
    return render_template('about.html')

# @app.route('/senator/id/<int:sen_id>')
# def senator(sen_id):
#     return render_template('senator.html', sen_id = sen_id)

@app.route('/legislator/id/<int:legislator_id>')
def legislator(legislator_id):
    return render_template('legislator.html', legislator_id = legislator_id)

@app.route('/committee/id/<int:committee_id>')
def committee(committee_id):
    return render_template('committee.html', committee_id = committee_id)

@app.route('/senator/id/1')
def senator1():
    return render_template('senator1.html')

@app.route('/senator/id/2')
def senator2():
    return render_template('senator2.html')

@app.route('/senator/id/3')
def senator3():
    return render_template('senator3.html')

@app.route('/representative/id/1')
def representative1():
    return render_template('representative1.html')

@app.route('/representative/id/2')
def representative2():
    return render_template('representative2.html')

@app.route('/representative/id/3')
def representative3():
    return render_template('representative3.html')

@app.route('/committee/id/1')
def committee1():
    return render_template('committee1.html')

@app.route('/committee/id/2')
def committee2():
    return render_template('committee2.html')

@app.route('/committee/id/3')
def committee3():
    return render_template('committee3.html')

@app.route('/bills/id/1')
def bills1():
    return render_template('bills1.html')

@app.route('/bills/id/2')
def bills2():
    return render_template('bills2.html')

@app.route('/bills/id/3')
def bills3():
    return render_template('bills3.html')

if __name__ == '__main__':
    app.run()
