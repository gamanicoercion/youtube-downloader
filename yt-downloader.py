from youtube_search import YoutubeSearch
import json
import os
import random
import os.path
import subprocess
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

def done(name):
    print(color(f"Done!\nFile name is {name}.", g))


def main(link_or_search):
    if link_or_search not in ['link', '2']:
        query_or_link = input(color("Input search query: ", x)) 
        choice = True
    else:
        query_or_link = input(color("Paste link: ", x)) 
        choice = False

    results = YoutubeSearch(f'{query_or_link}', max_results=5).to_json()
    results_dict = json.loads(results)
    in_dict = results_dict['videos']
    if len(in_dict) == 0:
        print(color('No input, Or no result.\nClosing...', 91))
        exit()
    url = in_dict[0]['url_suffix']  
    print(color("Video Details:\nTitle:", f), in_dict[0]['title'],
        color("\nChannel:", f), in_dict[0]['channel'],
        color("\nViews:", f), in_dict[0]['views'],
        color("\nVideo Duration:", f), in_dict[0]['duration'],
        color("\nDate Published:", f), in_dict[0]['publish_time']) 

    if choice:
        does_choose = input(color("Do you want more options for results?\n(y/Y or any input for no): ", e))
        if does_choose in ["y", "Y"]:
            clear_screen()
            for i in range(5):
                print(color(f"Video Details (#{i+1}):\nTitle:", f), in_dict[i]['title'],
                    color("\nChannel:", f), in_dict[i]['channel'],
                    color("\nViews:", f), in_dict[i]['views'], 
                    color("\nVideo Duration:", f), in_dict[i]['duration'],
                    color("\nDate Published:", f), in_dict[i]['publish_time'], "\n")
            choose_vid = int(input(color("Which video do you want to choose?\n(options: 1-5) ", d))) - 1
            if choose_vid not in range(5):
                print(color("Not a viable input.\nClosing...",91))
                exit()
            url = in_dict[choose_vid]['url_suffix']
        else:
            print(color("Showing only 1 result...", "91"))
            pass

    inp_name = input(color("Input a filename for the video: ", y))
    if len(inp_name) == 0:
        print(color("Defaulting to randomly generated numbers", g))
        inp_name = random.randint(1,10000)
    file_type = input(color("Choose format (mp3, webm, mp4): ", z))
    if file_type not in ["mp3", "mp4", "webm"]:
        print(color("Not a viable input!\nClosing...", "91"))
        exit()

    elif file_type in ["mp3"]:
        inp_aud_quality = input(color("Do you want to choose the audio quality?\ny/n: ", a))
        if inp_aud_quality in ["y", "Y"]:
            aud_quality = input(color('Input quality of audio:\n("worst", "best", "average", "avg"): ', b))
            if aud_quality in ['best', 'bet', 'bset', 'b']:
                aud_quality = 0
            elif aud_quality == "worst":
                aud_quality = 10
            elif aud_quality in ["average", "avg"]:
                aud_quality = 5
        elif inp_aud_quality in ["n", "N", ""]:
            aud_quality = 5
        if file_type in ["mp3"]:
                os.chdir(f"yt-dlp-py/{file_type}")
                os.system(f'yt-dlp -o "{inp_name}, {aud_quality}" -x --audio-format mp3 --audio-quality {aud_quality} "https://www.youtube.com{url}"')
                done(inp_name)

        
    elif file_type not in ['mp3']:
        inp_vid_quality = input(color("Do you want to choose the video quality?\n(y/n) ", x))
        if inp_vid_quality in ["y", "yes", "ye", "Y"]:
            vid_quality = input(color('Input quality of video...\n(input video quality in pixels, will round the number if not a correct value): ', b))
            if int(vid_quality) not in range(144, 4321):
                color("Not a viable input. Defualting to best video.", z)
            elif vid_quality in range(144, 4321):
                print(color("Will use the highest resolution closest to your input...", x))
                qualities = [144, 240, 360, 480, 720, 1080, 1440]
                closest_quality = qualities[0]
                for quality in qualities:
                    dist = abs(vid_quality-quality)
                    if dist < closest_distance:
                        closest_distance = dist
                        closest_quality = quality
            vid_quality = str(closest_quality)
        elif inp_vid_quality in ['no', 'n', 'No', 'N', "nO", ""]:
            print(color("Defaulting to 720p", a))
            vid_quality = "720"
            pass
        else:
            print(color("Not a viable input!\nClosing...", "91"))
            exit()

        os.chdir(f"yt-dlp-py/{file_type}")
        os.system(f'yt-dlp -f bv+ba -o "{inp_name}" -S res:{vid_quality} --recode-video {file_type} "https://www.youtube.com{url}"')
        done(inp_name)

link_or_search = input(color('Do you want to download with a link or through searching YouTube?\n(1 or any input for search/2 or "link" for link) ', a))
main(link_or_search)
