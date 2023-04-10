from moviepy.editor import *

video_file = "./data/Irobot02-returnYourHome.mp4"
# 读取视频文件
clip = VideoFileClip(video_file)

name = video_file.split("/")[-1]
frame_size = clip.size
frame_size_width = clip.w
frame_size_height = clip.h
file_size = os.stat(video_file).st_size
file_size = file_size / 1024 ** 2

print("%s: %s %s * %s, %.4f MB" % (name, frame_size, frame_size_width, frame_size_height, file_size))
# 获取视频帧数
frame_rate = clip.fps
# 获取视频帧间隔
duration = clip.duration
# 获取视频持续时间
frames = int(frame_rate * duration)


print(("%.2f fps, %.2f Length, %d Amont of fps. \n")  % (frame_rate, duration, frames))