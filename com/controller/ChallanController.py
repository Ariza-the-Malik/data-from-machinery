from flask import request, render_template, redirect, url_for
from werkzeug import secure_filename
import os
from RSAD import app
from RSAD.com.dao.VideoDAO import VideoDAO
from RSAD.com.dao.ChallanDAO import ChallanDAO
from RSAD.com.vo.ChallanVO import ChallanVO


#@app.route('/User/UploadChallan', methods=['GET'])
#def UserLoadaddChallan():
#    try:
#        videoDAO = VideoDAO()
#        videoVOList = videoDAO.viewVideo()
#        return render_template('User/UploadChallan.html', videoVOList=videoVOList)
#    except Exception as ex:
#        print(ex)



@app.route('/User/insertChallan', methods=['POST'])
def userInsertChallan():
    try:
        policestationname = request.form['ownername']
        policestationcode= request.form['vehnumber']
        policestationaddress= request.form['vehtype']
        username= request.form['image']
        password= request.form['video']

        registrationVO = RegistrationVO()
        registrationDAO = RegistrationDAO()

        registrationVO.PolicestationName= policestationname
        registrationVO.PolicestationCode= policestationcode
        registrationVO.PolicestationAddress= policestationaddress
        registrationVO.Username= username
        registrationVO.Password= password

        registrationDAO.insertRegistration(registrationVO)
        return render_template('User/login.html')
#        return redirect(url_for('adminViewRegistration'))
    except Exception as ex:
        print(ex)

@app.route('/User/viewChallan', methods=['GET'])
def adminViewChallan():
    try:
        challanDAO = ChallanDAO()
        challanVOList = challanDAO.viewChallan()
        print("__________________", challanVOList)
        return render_template('Admin/ManageChallan.html', challanVOList=challanVOList)
    except Exception as ex:
        print(ex)


@app.route('/Admin/deleteChallan', methods=['GET'])
def adminDeleteChallan():
    try:
        challanVO = ChallanVO()

        challanDAO = ChallanDAO()

        challanId = request.args.get('ChallanId')
        challanpath = request.args.get('Challanpath')
        os.remove(challanpath)
        challanVO.ChallanId = challanId

        challanDAO.deleteChallan(challanVO)

        return redirect(url_for('adminViewChallan'))
    except Exception as ex:
        print(ex)


#@app.route('/Admin/editChallan', methods=['GET'])
#def adminEditChallan():
#    try:
#        videoDAO = VideoDAO()
#        videoVOList = videoDAO.viewVideo()
#        challanVO = ChallanVO()
#
#        challanDAO = ChallanDAO()
#
#        challanId = request.args.get('ChallanId')
#
#        challanVO.ChallanId = challanId
#
#        challanVOList = challanDAO.editChallan(challanVO)
#
#        print("=======challanVOList=======", challanVOList)
#
#        print("=======type of challanVOList=======", type(challanVOList))
#
#        return render_template('Admin/AddChallan.html', challanVOList=challanVOList,videoVOList=videoVOList)
#    except Exception as ex:
#        print(ex)
#
#
#@app.route('/Admin/updateChallan', methods=['POST'])
#def adminUpdateChallan():
#    try:
#        challanId = request.form['ChallanId']
#        challan = request.form['challan']
#        challan_videoId= request.form['challan_videoId']
#
#        challanVO = ChallanVO()
#        challanDAO = ChallanDAO()
#
#        challanVO.ChallanId = challanId
#        challanVO.ChallanName= challanname
#        challanVO.Challan_VideoId= challan_videoId
#
#        challanDAO.updateChallan(challanVO)
#
#        return redirect(url_for('adminViewChallan'))
#    except Exception as ex:
#        print(ex)
