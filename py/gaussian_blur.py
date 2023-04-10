# 模糊视频中的所有帧

from skimage.filter import gaussian_filter
from moviepy.editor import VideoFileClip

def blur(image):
    """ Returns a blurred (radius=2 pixels) version of the image """
    return gaussian_filter(image.astype(float), sigma=2)

clip = VideoFileClip("./data/Irobot02-returnYourHome.mp4")
clip_blurred = clip.fl_image( blur )
clip_blurred.write_videofile("./output/blurred_video.mp4")