from flask import request, render_template, redirect, url_for
from RSAD import app
from RSAD.com.dao.AreaDAO import AreaDAO
from RSAD.com.vo.AreaVO import AreaVO
from RSAD.com.controller.LoginController import LoginSession,LogoutSession

@app.route('/Admin/loadArea', methods=['GET'])
def AdminLoadArea():
    try:
        if LoginSession() == 'admin':
            return render_template('Admin/AddArea.html')
        else:
            return redirect(url_for('LogoutSession'))
    except Exception as ex:
        print(ex)



@app.route('/Admin/insertArea', methods=['POST'])
def adminInsertArea():
    try:
        if LoginSession() == 'admin':
            areaname = request.form['areaname']
            pincode= request.form['pincode']

            areaVO = AreaVO()
            areaDAO = AreaDAO()

            areaVO.AreaName= areaname
            areaVO.PinCode= pincode

            areaDAO.insertArea(areaVO)
    #        return render_template('User/login.html')
            return redirect(url_for('adminViewArea'))
        else:
            return redirect(url_for('LogoutSession'))
    except Exception as ex:
        print(ex)


@app.route('/Admin/viewArea', methods=['GET'])
def adminViewArea():
    try:
        if LoginSession() == 'admin':
            areaDAO = AreaDAO()
            areaVOList = areaDAO.viewArea()
            print("__________________", areaVOList)
            return render_template('Admin/ViewArea.html', areaVOList=areaVOList)
        else :
            return redirect(url_for('LogoutSession'))
    except Exception as ex:
        print(ex)


@app.route('/Admin/deleteArea', methods=['GET'])
def adminDeleteArea():
    try:
        if LoginSession() == 'admin':
            areaVO = AreaVO()

            areaDAO = AreaDAO()

            areaId = request.args.get('AreaId')

            areaVO.AreaId = areaId

            areaDAO.deleteArea(areaVO)

            return redirect(url_for('adminViewArea'))
        else:
            return redirect(url_for('LogoutSession'))
    except Exception as ex:
        print(ex)


@app.route('/admin/editArea', methods=['GET'])
def adminEditArea():
    try:
        if LoginSession() == 'admin':
            print()
            areaVO = AreaVO()

            areaDAO = AreaDAO()

            areaId = request.args.get('AreaId')

            areaVO.AreaId = areaId

            areaVOList = areaDAO.editArea(areaVO)

            print("=======areaVOList=======", areaVOList)

            print("=======type of areaVOList=======", type(areaVOList))

            return render_template('Admin/AddArea.html', areaVOList=areaVOList)
        else:
            return redirect(url_for('LogoutSession'))
    except Exception as ex:
        print(ex)


@app.route('/Admin/updateArea', methods=['POST'])
def adminUpdateArea():
    try:
        if LoginSession() == 'admin':
            areaId = request.form['AreaId']
            areaname = request.form['areaname']
            pincode= request.form['pincode']

            areaVO = AreaVO()
            areaDAO = AreaDAO()

            areaVO.AreaId = areaId
            areaVO.AreaName= areaname
            areaVO.PinCode= pincode

            areaDAO.updateArea(areaVO)

            return redirect(url_for('adminViewArea'))
        else:
            return redirect(url_for('LogoutSession'))
    except Exception as ex:
        print(ex)
