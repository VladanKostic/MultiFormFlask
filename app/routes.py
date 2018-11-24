from flask import render_template, request
from app import app

from flask import jsonify

class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

@app.route('/foo')
def get_foo():
    raise InvalidUsage('This view is gone', status_code=410)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/multiform', methods=['GET','POST'])
def multiform():
    print('Start')
    print(request)
    if request.method == 'POST':
        print('Post method!!!')

        if request.form['submit'] == 'Submit1':
            firstname = request.form.get('firstname')
            lastname = request.form.get('lastname')
            print(firstname,' ', lastname)
            return render_template('result_form1.html',firstname = firstname, lastname = lastname)
        elif request.form['submit'] == 'Submit2':
            street = request.form.get('street')
            if street == "":
                raise InvalidUsage('You mast enter a street address',status_code=510)
            city = request.form.get('city')
            postalcode = request.form.get('postalcode')
            print(street, ' ', city,' ',postalcode)
            return render_template('result_form2.html', street=street, city=city, postalcode=postalcode )
        else:
            print('Post method!!!')
    return render_template('multiform.html')
