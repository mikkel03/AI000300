# cut returnYourHome.mp4  by giving the path to the original file and the start and end time of the cut in seconds.
# The output file will be named cutYourHome.mp4 and will contain the part of the original file between the two times.
# For example, cut('/path/to/original.mp4', 0.5, 2.5) will make a new file called 'cut
# YourHome.mp4' where the part that is in the middle of the original file will be called 'YourHome.mp4'.
# The two times should be given as floating point numbers.
# The first time is always the value of seconds from the beginning of the file.
# The second time is always the value of seconds after the end of the file.
# If the original file only contained seconds, the second time would be ignored and the function would return the original file.
# If the start time is after the end time, the function would return an empty string.
# If the file doesn't exist or the times aren't in seconds, the function would return an empty string.
# If the file can't be read, the function would return an empty string.
# If the function does not work for whatever reason, it would return an empty string.
# For extra credit, allow the user to specify the output file name and path.
# For extra credit, allow the user to specify the time units.
# For extra credit, allow the user to specify the time units to be used.
# For extra credit, make it so that the time unit used is always seconds. This way, the user can always specify the time units in any order.
# For extra credit, make it so that the user can specify the time units in any order. This way, the user can specify the time units in any
# order. If the user specifies a time unit that doesn't exist, it would return an empty string. If the user specifies a time unit that doesn't
# exist, the function would return an empty string. If the user specifies a time unit that doesn't work for whatever reason, it would return an empty string
# if the user specifies a time unit that doesn't work for whatever reason, it would return an empty string.

from typing import List
from moviepy.editor import * #import the library for the cut function. It is a library, not a function. The function is called "cut" and it is in the moviepy namespace.
import numpy as np

def read_video_info(video_file):
    '''
    读取视频信息
    :param video_file: 视频文件路径
    :return: 视频信息
    '''
    load_video = VideoFileClip(video_file)
    duration = load_video.duration  # read duration of loadclip
    video_info = (duration,)
    load_video.reader.close()
    load_video.audio.reader.close_proc()
    print("%s Duration is: %.2f seconds" %(video_file.split("/")[-1], duration))
    return video_info

def clip_video_by_timeline(video_file, start_time, end_time, write_file):
    """
    the start time in seconds. The time must be in seconds. If it isn't, it would return an empty string.
    the end time in seconds. The time must be in seconds. If it isn't, it would return an empty string.
    The program would return an empty string if the start time isn't after the end time. 
    The program would return an empty string if the file doesn't exist or the times aren't in seconds.

    """
    #如果开始时间大于结束时间，则返回空字符串
    if start_time >= end_time:
        return ""
    #加载视频文件
    load_video = VideoFileClip(video_file)
    #裁剪视频文件
    cut_clip = load_video.subclip(start_time, end_time) #the file to be cut. 
    #写入视频文件
    cut_clip.write_videofile(write_file)

def concatenate_videos(*videos):
    '''
    将多个视频合并成一个视频
    a function with python moviepy that combines multiple video files as arguments
    '''
    clips = []
    # 遍历videos列表，将每一个视频添加到clips列表中
    for v in videos:
        clips.append(VideoFileClip(v))
    # 将clips列表中的视频合并到一起，并返回一个新的视频
    final_clip = concatenate_videoclips(clips)
    return final_clip

def composite_videos(*videos):
    '''
    将多个视频合成一个视频, 叠在一起,覆盖
    '''
    clips = []
    # 遍历videos列表，将每一个元素转换为VideoFileClip对象
    for v in videos:
        clips.append(VideoFileClip(v))
    # 将每一帧的宽度缩放到1/i+1    
    for i in range(len(clips)):
        print(1.0 / (i + 1))
        ########clips[i].resize( 1.0 / (i + 1))
    # 将clips列表中的元素拼接到final_video中
    final_clip = CompositeVideoClip(clips)
    # 返回拼接后的final_video
    return final_clip

def array_videos(row, line, *videos):
    '''
    将多个视频合并成一个视频, 叠在一起,铺开
    '''
    n = len(videos)
    clips = []
    # 遍历视频列表
    for v in videos:
        # 将视频转换为VideoFileClip
        clips.append(VideoFileClip(v).margin(20))
    clips[1] = clips[1].fx(vfx.mirror_y)
    clips[0] = clips[0].resize(0.5)
    clips = np.array(clips).reshape(row, line)
    clips = clips.tolist()
    # 将视频列表转换为clips_array
    final_clip = clips_array(clips)
    # 返回clips_array
    return final_clip


    

if __name__ == "__main__":
    file = "./data/Irobot02-returnYourHome.mp4" #the file to be cut. 
    read_video_info(file)
    
    # cut video file
    start = 3 
    end = 6.5
    write_file01 = './output/Irobot02_0300-0615.mp4'
    #clip_video_by_timeline(file, start, end, write_file01)
    write_file02 = './output/Irobot02_1700-2900.mp4'
    #clip_video_by_timeline(file, 17, 29, write_file02)

    # cut video file
    file = "./data/T300.mp4" 
    read_video_info(file)    
    start = 0.7 
    end = 1
    write_file03 = './output/T300_0020-0100.mp4'
    #clip_video_by_timeline(file, start, end, write_file03)

    # combine videos by function
    concatenated_video_file = "./output/concatenated01.mp4"  
    # 将write_file01、write_file02、write_file03中的视频合并成一个视频
    final_video = concatenate_videos(write_file01, write_file02, write_file03)
    # 将视频缩放到270像素
    final_video = vfx.resize(final_video, width = 270)
    # 将视频写入concatenated_video_file
    #final_video.write_videofile(concatenated_video_file)   

    # composite video by function
    composite_video_file = "./output/composite05.mp4"
    final_video = composite_videos(write_file01, write_file02, write_file03)
    #final_video = vfx.resize(final_video, width = 540)
    # 将视频写入concatenated_video_file
    final_video.write_videofile(composite_video_file)

    # array video by function
    array_video_file_1 = "./output/array22-02.mp4"
    final_video = array_videos(2, 2, write_file01, write_file03, write_file02, "./output/T300_0020-0100.mp4")
    final_video.write_videofile(array_video_file_1)
    
    
    # 给视频加高斯模糊
    # Add Gaussian blur to the video

#Git Repo: https://github.com/mikkel03/AI000300