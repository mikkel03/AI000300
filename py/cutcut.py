# cut a movie file that name is Irobot01-returnYourHome.mp4, cut head 2 second 10-20, and cut tail 7-10. The resulting videos should be named Irobot01-head2-tail10.mp4 and Irobot
import re, os, sys, time, subprocess, glob, argparse, textwrap, itertools, collections, random

def main():
    parser = argparse.ArgumentParser(description='cut a movie file that name is Irobot01-returnYourHome.mp4, cut head 2 second 10-20, and cut tail 7-10.')
    parser.add_argument('-i', '--input', help='input file path', required=True)
    parser.add_argument('-o', '--output', help='output file path', required=True)
    parser.add_argument('-s', '--start', help='start time', required=True)
    parser.add_argument('-e', '--end', help='end time', required=True)
    args = parser.parse_args()    # parse command line arguments and store them in variables.
    input = args.input            # input file path. (required)
    output = args.output           # output file path. (required)    # output file path. (required)    # output file path. (required)
    start = args.start            # start time. (required)    # start time. (required)    # start time. (required)    # start
    end = args.end            # end time. (required)    # end time. (required)    # end time. (required)    # end
    inputPath, inputFile = os.path.split(input)    # input file path and name. (required)    # input file path and name
    outputPath, outputFile = os.path.split(output)    # output file path and name. (required)    # output file path and name
    if not os.path.isfile(input):    # check if input file path and name is valid. (required)    # check if input file
    	print("Error: input file path and name is invalid.")    # input file path and name is invalid. (required)    # print error message.
sys.exit()    # exit program. (required)    # exit program. (required)    # exit program. (required)    # exit program. (required)    # exit program.
        # print error message. (required)    # exit program. (required)    # exit program. (required)    # exit program. (required)

