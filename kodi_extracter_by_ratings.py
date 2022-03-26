#!/usr/bin/env python3

import xml.etree.cElementTree as et
import re, sys
from functools import reduce

def xml_extracter(xml_file, ratings):
    result = []
    parser = et.parse(xml_file)
    root = parser.getroot()
    for movie in root.findall("movie"):
        if(movie.find("userrating").text == str(ratings)):
            video_path = movie.find("filenameandpath").text
            if(re.match('^stack:///.*',video_path)):
                for stack_element in video_path[8:].split(","):
                    result.append(stack_element.strip())
            else:
                result.append(video_path)
    return result

def metadata_name_generator(video_list):
    result = []
    for video in video_list:
        filename = video.split("/")[-1]
        base_path = '/'+ reduce(lambda x,y:x+y+'/',video.split("/")[:-1])
        result.append(base_path+filename.split(".")[0]+"-fanart.jpg")
        result.append(base_path+filename.split(".")[0]+"-poster.jpg")
        result.append(base_path+filename.split(".")[0]+".nfo")
    return result

def special_character_process(xml_file):
    """ delete all the lines with character of &#, which will raise error while parsing"""
    file = open(xml_file, 'r', encoding = "UTF-8")
    result = []
    match_pattern = re.compile(r'&#')
    while True:
        line = file.readline()
        if not line:
            break
        elif match_pattern.search(line):
            pass
        else:
            result.append(line)
    file.close()
    file = open(xml_file, "w", encoding = "UTF-8")
    for line in result:
        file.write(line)
    file.close()

if __name__=="__main__":
    target = sys.argv[1]
    target_rating = sys.argv[2]
    special_character_process(target)
    video_list = xml_extracter(target, target_rating)
    metadata_name_list = metadata_name_generator(video_list)
    for v in video_list:
        print(v)
    for m in metadata_name_list:
        print(m)
