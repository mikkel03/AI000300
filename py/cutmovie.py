import numpy
import imageio
import decorator
import tqdm
from moviepy import editor

videofile = "./T300.mp4"
videoinfo = editor.VideoFileClip(videofile).subclip(3, 10)
videoinfo.write_videofile("new_video_1.mp4")


#F_col_new = ['video_1.mp4', 'video_2.mp4', 'video_3.mp4']
#s_colum = "video_out.mp4"
#size = (1920, 1080)
#for j in F_col_new:
#    clip2 = VideoFileClip(j).resize(size).setposition((0, 0))
#    video.append(clip2)

#concatenate_videoclips(video, method="chain").write_videofile(s_colum)
