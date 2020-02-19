from RSAD import db
from RSAD.com.vo.RegistrationVO import RegistrationVO
from RSAD.com.vo.LoginVO import LoginVO


class RegistrationDAO:

    def insertRegistration(self, RegistrationVo):
        db.session.add(RegistrationVo)
        db.session.commit()

    def viewRegistration(self):
#        RegistrationList=RegistrationVO.query.all()
        RegistrationList=db.session.query(RegistrationVO,LoginVO).join(RegistrationVO,LoginVO.Login_RegistrationId == RegistrationVO.RegistrationId).all()

        return RegistrationList

    def deleteRegistration(self,registrationVO):

        registrationList = RegistrationVO.query.get(registrationVO.RegistrationId)

        db.session.delete(registrationList)

        db.session.commit()

    def editRegistration(self,registrationVO):

        # categoryList = CategoryVO.query.get(categoryVO.categoryId)

        # categoryList = CategoryVO.query.filter_by(categoryId=categoryVO.categoryId)

        registrationList = RegistrationVO.query.filter_by(RegistrationId=registrationVO.RegistrationId).all()

        return registrationList

    def updateRegistration(self,registrationVO):

        db.session.merge(registrationVO)

        db.session.commit()
