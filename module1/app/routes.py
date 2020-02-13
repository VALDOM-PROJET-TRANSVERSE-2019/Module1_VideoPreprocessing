from app import app

# from https://medium.com/@iKhushPatel/convert-video-to-images-images-to-video-using-opencv-python-db27a128a481
# for frames to video look in this tutorial
import cv2

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route("/frames/<int:video_id>", methods=['GET'])
def generateFrames(video_id):
    # get video from mongoDB (using video_id)

    def getFrame(sec):
        vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
        hasFrames,image = vidcap.read()
        if hasFrames:
            cv2.imwrite("image"+str(count)+".jpg", image) # save frame as JPG file
        return hasFrames

    vidcap = cv2.VideoCapture('in.mp4')
    sec = 0
    frameRate = 0.5 # it will capture image in each 0.5 second
    count=1
    success = getFrame(sec)
    while success:
        count = count + 1
        sec = sec + frameRate
        sec = round(sec, 2)
        success = getFrame(sec)

    # create a collection in mongoDB and add image files
    # return the new frames collection id
    return "frames collection id! " + str(video_id)
