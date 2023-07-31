from youtube_search import YoutubeSearch
import json
import os
import random
import os.path
os.system("")

chooser = random.randint(1,2)
if chooser == 1:
    [x, y, z, a, b, c, d, e, f, g] = [random.randint(92,96) for _ in range(10)]
elif chooser == 2:
    [x, y, z, a, b, c, d, e, f, g] = [random.randint(32,36) for _ in range(10)]

def color(string, color):
    return f"\x1b[{color};40m{string}\x1b[0m"

def clear_screen():
    print("\x1b[2J\x1b[H", end='')

if not os.path.isdir("yt-dlp-py"):
    os.mkdir("yt-dlp-py")
    for folder in ["mp4", "mp3", "webm"]:
        os.mkdir(f"yt-dlp-py/{folder}")
query_inp = input(color("Input search query: ", x)) # input for video search

results = YoutubeSearch(f'{query_inp}', max_results=5).to_json()
results_dict = json.loads(results)
in_dict = results_dict['videos']
url = in_dict[0]['url_suffix'] # grabs video url
duration = in_dict[0]['duration']
print(color("Video Details:\nTitle:", f), in_dict[0]['title'],
      color("\nChannel:", f), in_dict[0]['channel'],
      color("\nViews:", f), in_dict[0]['views'],
      color("\nVideo Duration:", f), in_dict[0]['duration'],"\n") # shows the title, channel and view count

does_choose = input(color("Do you want more options for results?\n(y/Y or any input for no): ", e))
if does_choose in ["y", "Y"]:
    clear_screen()
    for i in range(5):
        print(color(f"Video Details (#{i+1}):\nTitle:", f), in_dict[i]['title'],
              color("\nChannel:", f), in_dict[i]['channel'],
              color("\nViews:", f), in_dict[i]['views'], 
              color("\nVideo Duration:", f), in_dict[i]['duration'], "\n") # shows the title, channel and view count
    
    choose_vid = int(input(color("Which video do you want to choose?\n(options: 1-5) ", d)))
    url = in_dict[choose_vid-1]['url_suffix']
    duration = in_dict[choose_vid]['duration']
else:
    print(color("Showing only 1 result...", "91"))
    pass

inp_name = input(color("Input a filename for the video: ", y))
file_type = input(color("Choose format (mp3, webm, mp4): ", z))
if file_type == "mp3":
    inp_quality = input(color("Do you want to choose the audio quality?\ny/n: ", a))
    if inp_quality in ["y", "Y"]:
        aud_quality = input(color('Input quality of audio:\n("worst", "best", "average", "avg"): ', b))
        if aud_quality == "best":
            aud_quality = 0
        elif aud_quality == "worst":
            aud_quality = 10
        elif aud_quality in ["average", "avg"]:
            aud_quality = 5
    elif inp_quality in ["n", "N"]:
        aud_quality = 5
  
    else:
        print(color("Not a viable input!\nClosing...", "91"))
        exit()
elif file_type not in ["mp4", "webm"]:
    print(color("Not a viable input!\nClosing...", "91"))
    exit()

if file_type == "mp3":
    os.chdir("yt-dlp-py/mp3")
    os.system(f'yt-dlp -o "{inp_name}, {duration}, {aud_quality}" -x --audio-format mp3 --audio-quality {aud_quality} "https://www.youtube.com{url}"')
elif file_type == "mp4":
    os.chdir("yt-dlp-py/mp4")
    os.system(f'yt-dlp -f bv+ba -o "{inp_name}, {duration}" --recode-video mp4 "https://www.youtube.com{url}"')
    
elif file_type == "webm":
    os.chdir("yt-dlp-py/webm")
    os.system(f'yt-dlp -f bv+ba -o "{inp_name}, {duration}" "https://www.youtube.com{url}"')
    
