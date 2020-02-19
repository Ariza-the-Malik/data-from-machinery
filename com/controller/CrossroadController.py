from flask import request, render_template, redirect, url_for
from RSAD import app
from RSAD.com.dao.AreaDAO import AreaDAO
from RSAD.com.dao.CrossroadDAO import CrossroadDAO
from RSAD.com.vo.CrossroadVO import CrossroadVO
from RSAD.com.controller.LoginController import LoginSession,LogoutSession


@app.route('/Admin/loadCrossroad', methods=['GET'])
def AdminLoadCrossroad():
    try:
        if LoginSession() == 'admin':
            areaDAO = AreaDAO()
            areaVOList = areaDAO.viewArea()
            return render_template('Admin/AddCrossroad.html', areaVOList=areaVOList)
        else:
            return redirect(url_for('LogoutSession'))

    except Exception as ex:
        print(ex)



@app.route('/Admin/insertCrossroad', methods=['POST'])
def adminInsertCrossroad():
    try:
        if LoginSession() == 'admin':
            crossroadname = request.form['crossroadname']
            crossroad_areaId= request.form['crossroad_areaId']

            crossroadVO = CrossroadVO()
            crossroadDAO = CrossroadDAO()

            crossroadVO.CrossroadName= crossroadname
            crossroadVO.Crossroad_AreaId= crossroad_areaId

            crossroadDAO.insertCrossroad(crossroadVO)
    #        return render_template('User/login.html')
            return redirect(url_for('adminViewCrossroad'))
        else:
            return redirect(url_for('LogoutSession'))
    except Exception as ex:
        print(ex)


@app.route('/Admin/viewCrossroad', methods=['GET'])
def adminViewCrossroad():
    try:
        if LoginSession() == 'admin':
            crossroadDAO = CrossroadDAO()
            crossroadVOList = crossroadDAO.viewCrossroad()
            print("__________________", crossroadVOList)
            return render_template('Admin/ViewCrossroad.html', crossroadVOList=crossroadVOList)
        else:
            return redirect(url_for('LogoutSession'))
    except Exception as ex:
        print(ex)


@app.route('/Admin/deleteCrossroad', methods=['GET'])
def adminDeleteCrossroad():
    try:
        if LoginSession() == 'admin':
            crossroadVO = CrossroadVO()

            crossroadDAO = CrossroadDAO()

            crossroadId = request.args.get('CrossroadId')

            crossroadVO.CrossroadId = crossroadId

            crossroadDAO.deleteCrossroad(crossroadVO)

            return redirect(url_for('adminViewCrossroad'))
        else:
            return redirect(url_for('LogoutSession'))
    except Exception as ex:
        print(ex)


@app.route('/Admin/editCrossroad', methods=['GET'])
def adminEditCrossroad():
    try:
        if LoginSession() == 'admin':
            areaDAO = AreaDAO()
            areaVOList = areaDAO.viewArea()
            crossroadVO = CrossroadVO()

            crossroadDAO = CrossroadDAO()

            crossroadId = request.args.get('CrossroadId')

            crossroadVO.CrossroadId = crossroadId

            crossroadVOList = crossroadDAO.editCrossroad(crossroadVO)

            print("=======crossroadVOList=======", crossroadVOList)

            print("=======type of crossroadVOList=======", type(crossroadVOList))

            return render_template('Admin/AddCrossroad.html', crossroadVOList=crossroadVOList,areaVOList=areaVOList)
        else:
            return redirect(url_for('LogoutSession'))
    except Exception as ex:
        print(ex)


@app.route('/Admin/updateCrossroad', methods=['POST'])
def adminUpdateCrossroad():
    try:
        if LoginSession() == 'admin':
            crossroadId = request.form['CrossroadId']
            crossroadname = request.form['crossroadname']
            crossroad_areaId= request.form['crossroad_areaId']

            crossroadVO = CrossroadVO()
            crossroadDAO = CrossroadDAO()

            crossroadVO.CrossroadId = crossroadId
            crossroadVO.CrossroadName= crossroadname
            crossroadVO.Crossroad_AreaId= crossroad_areaId

            crossroadDAO.updateCrossroad(crossroadVO)

            return redirect(url_for('adminViewCrossroad'))
        else:
            return redirect(url_for('LogoutSession'))
    except Exception as ex:
        print(ex)
