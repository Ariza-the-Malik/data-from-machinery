from RSAD.static.Dataset.Model.Detect import detector
from flask import request, render_template, redirect, url_for,Response
from RSAD import app

VIDEO = None
#@app.route("/User/startdetection",methods=['GET'])
#def loadvideo():
#    globals()['video'] = request.form['video']
#    print(globals()['video'])


@app.route("/User/video_feed")
def video_feed():
    #video  = "RSAD/static/Dataset/Model/road.mp4"
    video = globals()['VIDEO']
    d = detector(video)
	# return the response generated along with the specific media
	# type (mime type)
    return Response(d.main(),mimetype = "multipart/x-mixed-replace; boundary=frame")
