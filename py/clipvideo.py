# https://www.jb51.net/article/256331.htm
# https://zhuanlan.zhihu.com/p/196388776?utm_id=0
from moviepy import editor

ori_video_files = "T300.mp4"
video_clip = editor.VideoFileClip(ori_video_files)
video_clip.subclip(1, 5)
