from RSAD import db
from RSAD.com.vo.UploadvideoVO import VideoVO
from RSAD.com.vo.CrossroadVO import CrossroadVO



class VideoDAO:

    def insertVideo(self, videoVo):
        db.session.add(videoVo)
        db.session.commit()

    def viewVideo(self):
#        VideoList = db.session.query(VideoVO, CrossroadVO).join(CrossroadVO,VideoVO.Video_CrossroadId == CrossroadVO.categoryId).all()

        videoList=db.session.query(VideoVO,CrossroadVO).join(CrossroadVO,VideoVO.Video_CrossroadId == CrossroadVO.CrossroadId).all()

        return videoList

    def deleteVideo(self,videoVO):

        videoList = VideoVO.query.get(videoVO.VideoId)

        db.session.delete(videoList)

        db.session.commit()

    def editVideo(self,videoVO):

        # categoryList = CrossroadVO.query.get(categoryVO.categoryId)

        # categoryList = CrossroadVO.query.filter_by(categoryId=categoryVO.categoryId)

        videoList = VideoVO.query.filter_by(VideoId=videoVO.VideoId).all()

        return videoList

    def updateVideo(self,videoVO):

        db.session.merge(videoVO)

        db.session.commit()


    def ajaxVideoProduct(self, videoVO):
        ajaxProductvideoList = videoVO.query.filter_by(Video_CrossroadId=VideoVO.Video_CrossroadId).all()
        return ajaxProductvideoList
