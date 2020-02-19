from RSAD import db
from RSAD.com.vo.LoginVO import LoginVO


class LoginDAO:

    def insertLogin(self, loginVO):
        db.session.add(loginVO)
        db.session.commit()

    def validateLogin(self,loginVO):

        loginList=LoginVO.query.filter_by(LoginUsername=loginVO.LoginUsername,LoginPassword=loginVO.LoginPassword,LoginStatus=loginVO.LoginStatus)
        return loginList

    def blockLogin(self,loginVO):
        block = LoginVO.query.filter_by(Login_RegistrationId=loginVO.Login_RegistrationId).first()
        print(block)
        block.LoginStatus = 'inactive'
        db.session.commit()

    def unblockLogin(self,loginVO):
        block = LoginVO.query.filter_by(Login_RegistrationId=loginVO.Login_RegistrationId).first()
        block.LoginStatus = 'active'
        db.session.commit()

    def deletelogin(self,loginVO):
        print(loginVO.Login_RegistrationId)
        loginList = LoginVO.query.filter_by(Login_RegistrationId=loginVO.Login_RegistrationId).first()
        print(loginList)
        db.session.delete(loginList)
        db.session.commit()

    def updatelogin(self,loginVO):
        loginList = LoginVO.query.filter_by(Login_RegistrationId=loginVO.Login_RegistrationId).first()
        loginList.LoginUsername = loginVO.LoginUsername
        loginList.LoginPassword= loginVO.LoginPassword
        db.session.commit()







