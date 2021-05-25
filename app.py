from flask import Flask, redirect, render_template, request, url_for
from flask import session
app = Flask(__name__)
app.secret_key = '123'


@app.route('/')
def home():
    return render_template('cv.html')


@app.route('/assignment8')
def assignment8():
    return render_template("assignment8.html", hobbies=['gym', 'tennis', 'travel', 'cooking'])


@app.route('/list')
def list1():
    return render_template('list.html')


@app.route('/assignment9', methods=['get', 'post'])
def assignment9():
    users_list = [{"firstName": "Michael", "lastName": "Lawson", "Email": "michael.lawson@reqres.in"},
                  {"firstName": "Lindsay", "lastName": "Ferguson", "Email": "indsay.ferguson@reqres.in"},
                  {"firstName": "Tobias", "lastName": "Funke", "Email": "tobias.funke@reqres.in"},
                  {"firstName": "Byron", "lastName": "Fields", "Email": "byron.fields@reqres.in"},
                  {"firstName": "George", "lastName": "Edwards", "Email": "george.edwards@reqres.in"},
                  {"firstName": "Rachel", "lastName": "Howell", "Email": "rachel.howell@reqres.in"}]
    result = ""
    the_method = request.method
    nickname = ""

    if 'search' in request.args:
        for user in users_list:
            if request.args['search'] == user['firstName'] \
                    or request.args['search'] == user['lastName'] \
                    or request.args['search'] == user['Email']:
                result = [user['firstName'], user['lastName'], user['Email']]
    else:
        result = ""


    if nickname in session:
        nickname = session['nicknameA']
    else:
        if 'nicknameA' in request.form:
            nickname = request.form['nicknameA']
            session['nicknameA'] = nickname

    return render_template('assignment9.html',
                           users_list=users_list,
                           result=result,
                           the_method=the_method,
                           nickname=nickname)

@app.route('/logout')
def logout():
    session['nicknameA'] = ""
    return redirect(url_for('assignment9'))

if __name__ == '__main__':
        app.run(debug=True)
