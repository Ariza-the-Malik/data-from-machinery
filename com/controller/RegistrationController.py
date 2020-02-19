
from flask import request, render_template, redirect, url_for
from RSAD import app
from RSAD.com.dao.RegistrationDAO import RegistrationDAO
from RSAD.com.vo.RegistrationVO import RegistrationVO
from RSAD.com.dao.LoginDAO import LoginDAO
from RSAD.com.vo.LoginVO import LoginVO
from RSAD.com.controller.LoginController import LoginSession,LogoutSession


#@app.route('/', methods=['GET'])
#def userLoadLogin():
#    try:
#
#        return render_template('User/login.html')
#    except Exception as ex:
#        print(ex)


@app.route('/registration', methods=['GET'])
def userLoadRegistration():
    try:

        return render_template('User/Registration.html')
    except Exception as ex:
        print(ex)
#    return render_template('Admin/ManageUsers.html')


@app.route('/User/insertRegistration', methods=['POST'])
def userInsertRegistration():
    try:
        policestationname = request.form['policestationname']
        policestationcode= request.form['policestationcode']
        policestationaddress= request.form['policestationaddress']
        username= request.form['username']
        password= request.form['password']


        registrationVO = RegistrationVO()
        registrationDAO = RegistrationDAO()
        loginVO = LoginVO()
        loginDAO = LoginDAO()

        registrationVO.PolicestationName= policestationname
        registrationVO.PolicestationCode= policestationcode
        registrationVO.PolicestationAddress= policestationaddress
        registrationVO.Username= username
        registrationVO.Password= password
        registrationDAO.insertRegistration(registrationVO)

        loginVO.LoginUsername = username
        loginVO.LoginPassword = password
        loginVO.LoginRole = 'user'
        loginVO.LoginStatus = 'active'
        registrationList = RegistrationVO.query.filter_by(Username=username).first()
        loginVO.Login_RegistrationId = registrationList.RegistrationId

        loginDAO.insertLogin(loginVO)


        return render_template('User/Login.html')
#        return redirect(url_for('adminViewRegistration'))
    except Exception as ex:
        print(ex)


@app.route('/Admin/ViewUsers', methods=['GET'])
def adminViewRegistration():
    try:
        if LoginSession() == 'admin':
            registrationDAO = RegistrationDAO()
            registrationVOList = registrationDAO.viewRegistration()
            print("__________________", registrationVOList)
            return render_template('Admin/ViewUsers.html', registrationVOList=registrationVOList)
        else:
            return redirect(url_for('LogoutSession'))
    except Exception as ex:
        print(ex)


@app.route('/Admin/deleteUser', methods=['GET'])
def adminDeleteRegistration():
    try:
        if LoginSession() == 'admin':
            registrationVO = RegistrationVO()

            registrationDAO = RegistrationDAO()

            registrationId = request.args.get('RegistrationId')

            loginDAO = LoginDAO()
            loginVO = LoginVO()

            loginVO.Login_RegistrationId = registrationId
            loginDAO.deletelogin(loginVO)

            registrationVO.RegistrationId = registrationId

            registrationDAO.deleteRegistration(registrationVO)

            return redirect(url_for('adminViewRegistration'))
        else:
            return redirect(url_for('LogoutSession'))
    except Exception as ex:
        print(ex)


@app.route('/Admin/editUser', methods=['GET'])
def adminEditRegistration():
    try:
        if LoginSession() == 'admin':
            registrationVO = RegistrationVO()
            registrationDAO = RegistrationDAO()

            registrationId = request.args.get('RegistrationId')
            registrationVO.RegistrationId = registrationId

            registrationVOList = registrationDAO.editRegistration(registrationVO)


            print("=======registrationVOList=======", registrationVOList)

            print("=======type of registrationVOList=======", type(registrationVOList))

            return render_template('Admin/EditUser.html', registrationVOList=registrationVOList)
        else:
            return redirect(url_for('LogoutSession'))
    except Exception as ex:
        print(ex)


@app.route('/Admin/updateUser', methods=['POST'])
def adminUpdateRegistration():
    try:
        if LoginSession() == 'admin':
            registrationId = request.form['RegistrationId']
            policestationname = request.form['policestationname']
            policestationcode= request.form['policestationcode']
            policestationaddress= request.form['policestationaddress']
            username= request.form['username']
            password= request.form['password']
            registrationVO = RegistrationVO()
            registrationDAO = RegistrationDAO()

            registrationVO.RegistrationId = registrationId
            registrationVO.PolicestationName= policestationname
            registrationVO.PolicestationCode= policestationcode
            registrationVO.PolicestationAddress= policestationaddress
            registrationVO.Username= username
            registrationVO.Password= password

            registrationDAO.updateRegistration(registrationVO)

            loginDAO = LoginDAO()
            loginVO = LoginVO()
            loginVO.Login_RegistrationId = registrationId
            loginVO.LoginUsername = username
            loginVO.LoginPassword = password
            loginDAO.updatelogin(loginVO)

            return redirect(url_for('adminViewRegistration'))
        else:
            return redirect(url_for('LogoutSession'))
    except Exception as ex:
        print(ex)

@app.route('/Admin/blockUser', methods=['GET'])
def adminblockUser():
    try:
        if LoginSession() == 'admin':
            login_registrationId = request.args.get('RegistrationId')

            loginDAO = LoginDAO()
            loginVO = LoginVO()
            loginVO.Login_RegistrationId = login_registrationId
            loginDAO.blockLogin(loginVO)
            return redirect(url_for('adminViewRegistration'))
        else:
            return redirect(url_for('LogoutSession'))
    except Exception as ex:
        print(ex)

@app.route('/Admin/unblockUser', methods=['GET'])
def adminunblockUser():
    try:
        if LoginSession() == 'admin':
            login_registrationId = request.args.get('RegistrationId')
            loginDAO = LoginDAO()
            loginVO = LoginVO()
            loginVO.Login_RegistrationId = login_registrationId
            loginDAO.unblockLogin(loginVO)
            return redirect(url_for('adminViewRegistration'))
        else:
            return redirect(url_for('LogoutSession'))
    except Exception as ex:
        print(ex)

