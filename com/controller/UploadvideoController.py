from flask import request, render_template, redirect, url_for
# from werkzeug import secure_filename
import os
from RSAD import app
from RSAD.com.dao.CrossroadDAO import CrossroadDAO
from RSAD.com.dao.UploadvideoDAO import VideoDAO
from RSAD.com.vo.UploadvideoVO import VideoVO
import RSAD.com.controller.DetectionController as dc
from RSAD.com.controller.LoginController import LoginSession,LogoutSession



@app.route('/User/UploadVideo', methods=['GET'])
def UserLoadVideo():
    try:
        if LoginSession() == 'user':
            crossroadDAO = CrossroadDAO()
            crossroadVOList = crossroadDAO.viewCrossroad()
            return render_template('User/UploadVideo.html', crossroadVOList=crossroadVOList)
        else:
            return redirect(url_for('LogoutSession'))
    except Exception as ex:
        print(ex)



@app.route('/User/insertVideo', methods=['POST'])
def UserInsertVideo():
    try:
        if LoginSession() == 'user':
            video = request.files['video']
            video_crossroadId= request.form['video_crossroadId']
            videoname = secure_filename(video.filename)
            videopath="RSAD/static/Dataset/Videos/"
            video.save(videopath+videoname)
            videoVO = VideoVO()
            videoDAO = VideoDAO()
            videoVO.VideoName = videoname
            videoVO.VideoPath= videopath
            videoVO.Video_CrossroadId = video_crossroadId
            videoDAO.insertVideo(videoVO)
            dc.VIDEO = videopath+videoname
            return render_template('User/Detection.html')
        else:
            return redirect(url_for('LogoutSession'))
#    return redirect("/User/startdetection?video="+videopath)
    except :
        video_crossroadId= request.form['video_crossroadId']
        videopath="RSAD/static/Dataset/Videos/"+secure_filename(video.filename)
        dc.VIDEO = videopath
        return render_template('User/Detection.html')
@app.route('/Admin/ViewVideo', methods=['GET'])
def adminViewVideo():
    try:
        if LoginSession() == 'admin':
            videoDAO = VideoDAO()
            videoVOList = videoDAO.viewVideo()
            print("__________________", videoVOList)
            return render_template('Admin/ViewVideo.html', videoVOList=videoVOList)
        else:
            return redirect(url_for('LogoutSession'))
    except Exception as ex:
        print(ex)


@app.route('/Admin/deleteVideo', methods=['GET'])
def adminDeleteVideo():
    try:
        if LoginSession() == 'user':
            videoVO = VideoVO()

            videoDAO = VideoDAO()

            videoId = request.args.get('VideoId')
            videopath = request.args.get('Videopath')
            os.remove(videopath)
            videoVO.VideoId = videoId
            videoDAO.deleteVideo(videoVO)

            return redirect(url_for('adminViewVideo'))
        else:
            return redirect(url_for('LogoutSession'))
    except Exception as ex:
        print(ex)


#@app.route('/Admin/editVideo', methods=['GET'])
#def adminEditVideo():
#    try:
#        crossroadDAO = CrossroadDAO()
#        crossroadVOList = crossroadDAO.viewCrossroad()
#        videoVO = VideoVO()
#
#        videoDAO = VideoDAO()
#
#        videoId = request.args.get('VideoId')
#
#        videoVO.VideoId = videoId
#
#        videoVOList = videoDAO.editVideo(videoVO)
#
#        print("=======videoVOList=======", videoVOList)
#
#        print("=======type of videoVOList=======", type(videoVOList))
#
#        return render_template('Admin/AddVideo.html', videoVOList=videoVOList,crossroadVOList=crossroadVOList)
#    except Exception as ex:
#        print(ex)
#
#
#@app.route('/Admin/updateVideo', methods=['POST'])
#def adminUpdateVideo():
#    try:
#        videoId = request.form['VideoId']
#        video = request.form['video']
#        video_crossroadId= request.form['video_crossroadId']
#
#        videoVO = VideoVO()
#        videoDAO = VideoDAO()
#
#        videoVO.VideoId = videoId
#        videoVO.VideoName= videoname
#        videoVO.Video_CrossroadId= video_crossroadId
#
#        videoDAO.updateVideo(videoVO)
#
#        return redirect(url_for('adminViewVideo'))
#    except Exception as ex:
#        print(ex)
