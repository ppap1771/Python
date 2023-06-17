import requests
from bs4 import BeautifulSoup

# specify the url of the course page
url = 'https://ugcmoocs.inflibnet.ac.in/index.php/courses/MOOCs/2019-20_Cycle_II/English/SOCIAL_MEDIA_AND_TEENAGERS'

# send a GET request to the url and parse the html content
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# find all the video duration elements and extract their text content
duration_elements = soup.find_all('span', {'class': 'time'})
durations = [e.text.strip() for e in duration_elements]

# convert the duration strings to time in seconds and sum them up
total_duration = sum([int(d.split(':')[0])*3600 + int(d.split(':')[1])*60 + int(d.split(':')[2]) for d in durations])

# print the total duration in seconds
print(total_duration)
