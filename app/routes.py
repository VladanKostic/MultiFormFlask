from flask import render_template, request
from app import app

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
            city = request.form.get('city')
            postalcode = request.form.get('postalcode')
            print(street, ' ', city,' ',postalcode)
            return render_template('result_form2.html', street=street, city=city, postalcode=postalcode )
        else:
            print('Post method!!!')
    return render_template('multiform.html')
