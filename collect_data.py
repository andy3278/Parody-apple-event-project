from youtube_transcript_api import YouTubeTranscriptApi
import os

# starting from 2019 march event
list_of_video_ids = ['TZmBoMZFC8g', 'psL_5RIBqnY', '-rAeqN-Q7x4', 'GEZhD3J89ZE', 
                    'b13xnFp_LJs', 'KR0g-1hnQPA', '5AwdkGKmZ0I', 'JdBYVNuky1M', 
                    '0TD96VTf0Xs', 'EvGOlAkLSLw', 'exM1uajp--A', 'CUwg_JoNHpo',
                    'q5D55G7Ejs8', 'ux6zXguiqxM', 'GYkq9Rgoj8E', 'ZiP1l7jlIIA', 'ctkW3V0Mh-k']


# get transcript for each video
def get_transcript(id : str) -> str:

    trans = YouTubeTranscriptApi.get_transcript(id, languages=['en'])
    # concat all text to one string
    text = ''
    for i in range(len(trans)):
        text += trans[i]['text'] + ' '
    return text

def transcript_to_list(list_of_video_ids : list) -> list:
    list_of_trans = []
    for i in range(len(list_of_video_ids)):
        temp_text = get_transcript(list_of_video_ids[i])
        list_of_trans.append(temp_text)
        print(len(temp_text))
    return list_of_trans


def save_to_txt(list_of_trans):
    # save to one txt file
    if os.path.exists('./data/all_text_apple_event.txt'):
        os.remove('./data/all_text_apple_event.txt')
    for trans in list_of_trans:
        f = open('./data/all_text_apple_event.txt', 'a')
        for line in trans:
            f.write(line)
        f.close()
    return None

if __name__ == '__main__':
    list_of_trans = transcript_to_list(list_of_video_ids)
    
    # uncomment if need to save to txt
    # save_to_txt(list_of_trans)
    print('Done')

