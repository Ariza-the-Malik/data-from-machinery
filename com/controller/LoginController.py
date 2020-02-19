from flask import request, render_template, redirect, url_for,session
from RSAD import app
from RSAD.com.vo.LoginVO import LoginVO
from RSAD.com.dao.LoginDAO import LoginDAO


@app.route('/', methods=['GET'])
def UserLoadLogin():
    print("in login")

    return render_template('User/Login.html')

@app.route('/Admin', methods=['GET'])
def AdminLoadLogin():
    print("in login")
    return render_template('Admin/Login.html')

@app.route("/validateLogin", methods=['POST'])
def ValidateLogin():
    loginUsername = request.form['loginUsername']
    loginPassword = request.form['loginPassword']
    role = request.form['role']
    print(loginPassword,loginUsername)

    loginVO = LoginVO()
    loginDAO = LoginDAO()

    loginVO.LoginUsername = loginUsername
    loginVO.LoginPassword = loginPassword
    loginVO.LoginStatus = "active"

    loginVOList = loginDAO.validateLogin(loginVO)
    print(loginVOList)
    loginDictList = [i.as_dict() for i in loginVOList]

    print(loginDictList)
    lenLoginDictList = len(loginDictList)

    if lenLoginDictList == 0:
        if(role == "user"):

            msg = 'Username Or Password is Incorrect !'
            return render_template('User/Login.html', error=msg)
        elif(role=="admin"):

            msg = 'Username Or Password is Incorrect !'
            return render_template('Admin/Login.html', error=msg)


    else:

        for row1 in loginDictList:

            loginId = row1['LoginId']

            loginUsername = row1['LoginUsername']

            loginRole = row1['LoginRole']

            session['session_loginId'] = loginId

            session['session_loginUsername'] = loginUsername

            session['session_loginRole'] = loginRole

            session.permanent = True

            if loginRole == 'admin' :
                return redirect(url_for('adminLoadDashboard'))
            elif loginRole == 'user':
                return redirect(url_for('userLoadDashboard'))


@app.route('/Admin/loadDashboard', methods=['GET'])
def adminLoadDashboard():
    return render_template('Admin/index.html')

@app.route('/User/loadDashboard', methods=['GET'])
def userLoadDashboard():
    return redirect('/User/UploadVideo')



@app.route('/admin/loginSession')
def LoginSession():
    if 'session_loginId' and 'session_loginRole' in session:

        if session['session_loginRole'] == 'admin':

            return 'admin'

        elif session['session_loginRole'] == 'user':

            return 'user'

        print("<<<<<<<<<<<<<<<<True>>>>>>>>>>>>>>>>>>>>")

    else:

        print("<<<<<<<<<<<<<<<<False>>>>>>>>>>>>>>>>>>>>")

        return False


@app.route("/admin/logoutSession")
def LogoutSession():
    session.clear()

    return redirect(url_for('UserLoadLogin'))