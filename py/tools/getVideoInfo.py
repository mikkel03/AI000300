import ffmpeg
from moviepy.editor import * 	# import the libraries

def get_video_info(video_file: str):
    _probe = ffmpeg.probe(video_file)
    
    
    #probe_detail = _probe['streams'] # get all the information about the file, including the frames, fps, duration, etc. for each stream.
    #video_info = {'width': _probe[0]['width'], 'height': _probe[0]['height'], 'fps': _probe[0]['avg_frame_rate'], 'duration': _probe[0]['duration']}
    #return video_info

"""
def get_video_info_self(video_file):
     probe = ffmpeg.probe(video_file)
    print(probe)

    format = probe['format']
    print(format)

    bitrate = format['bit_rate']
    kbps = bitrate / 1000 
    print(int(bitrate))  # bitrate in kbps
    print(int(kbps))        # bitrate in kbps (as a string)


    duration = format['duration']
    duration = int(float(duration))

    print(int(format['size']))
    print(int(int(probe['streams'][0]['r_frame_rate'].split('/')[0]) / int(probe['streams'][0]['r_frame_rate'].split('/')[1])))

    file_size = kbps * duration / 8 	# kbps * seconds = file size in bytes
    print(file_size)
    print(file_size / 1024)
    print(int(float['size']) / 1024 ** 2) 
"""


if __name__ == '__main__':
    video_file = "./data/Irobot02-returnYourHome.mp4"
    #clip = VideoFileClip(video_file)
    #clip.reader.close() # close the reader first.
    #get_video_info_self(video_file)
    get_video_info(video_file)
