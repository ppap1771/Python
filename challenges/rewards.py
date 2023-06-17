import subprocess
import time
import webbrowser
import pyautogui

# set the path to msedge.exe
msedge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

word_array = [
    "excitement", "adventure", "blossom", "celebrate", "harmony",
    "freedom", "champion", "discover", "elegance", "serenity",
    "prosperity", "kindness", "illuminate", "magnificent", "refresh",
    "wanderlust", "imagination", "enchanted", "blissful", "enlighten",
    "forgiveness", "tranquil", "harvest", "inspire", "sapphire",
    "lavender", "sparkling", "majestic", "reflection", "radiant",
    "glittering", "serenade", "nostalgia", "moonlight", "rhapsody",
    "whimsical", "enthusiasm", "spectacular", "grateful", "fantasia",
    "ecstasy", "playful", "caress", "integrity", "glistening",
    "courageous", "heavenly", "celestial", "eternity", "delightful",
    "tranquility", "serendipity", "scrumptious", "parad", "fascinate",
    "resilient", "euphoria", "vivacious", "whimsical", "jovial", 
    "luminous", "exquisite", "veracity", "serendipity", "idyllic", 
    "benevolent", "blissful", "incandescent", "plethora", "gracious", 
    "ethereal", "nostalgic", "radiant", "harmonious", "frenzy", "ecstatic", 
    "exhilarating", "solitude", "wanderlust", "exuberance", "tranquility", 
    "enchanting", "melancholy", "enlightenment", "ephemeral", "surreal", 
    "bewitched", "elegance", "grateful", "innovative", "magnificent", 
    "miraculous", "paradise", "passionate", "rejuvenate", "sensational", 
    "serenity", "spectacular", "spontaneous", "stupendous", "supreme", 
    "tranquil", "unforgettable", "wholesome", "wondrous", "profound", 
    "renaissance", "charismatic", "inspirational", "phenomenal", 
    "extraordinary", "majestic", "transcendent"
]


cmd = f'"{msedge_path}" --profile-directory=Default'
subprocess.run(cmd, shell=True)
time.sleep (2)

incr = 12
i =0
for k in range (0,7):
    #print(k, end=" ")
    if k == 4:
        print("mobile view" , end = " ")
        incr = 9 
        time.sleep (2)
        pyautogui.hotkey("ctrl", "m")
    print(k, end=" ")
    for i in range (i , i+incr ):
        url = "https://www.bing.com/search?q=define+" + word_array[i]
        webbrowser.open_new_tab(url)
        time.sleep(1.1)
    time.sleep (1.5)
    for j in range (0, incr):
        pyautogui.hotkey("ctrl", "w")
        time.sleep (0.4)
time.sleep (2)
pyautogui.hotkey("ctrl", "m")
print()