from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

def elements_to_formatted_lists(timestamps_elements, artist_song_label_elements):
    timestamps =  []
    for ele in timestamps_elements:
        if ele.text == '':
            pass
        elif ele.text[0] == 'w':
            timestamps.append(ele.text[3:] + ' w/')
        else:
            timestamps.append(ele.text[3:])
    artist_song_label = [ele.text for ele in artist_song_label_elements]
    clear_artist_song_label = list(filter(None, artist_song_label))
    return timestamps, clear_artist_song_label

def format_tracklist_output(timestamp, artist_song):
    if timestamp == '':
        return artist_song
    elif timestamp[0] == ' ':
        return f' {timestamp} {artist_song}'
    elif timestamp[1] == 'w':
        return f' {timestamp} {artist_song}'
    else:
        return f'{timestamp} {artist_song}'

def tracklist1001_url_to_youtube_comment(Url: str):
    service = Service()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(Url)
    time.sleep(5)
    
    timestamps_elements = driver.find_elements(by=By.XPATH, value="//div[@class='bPlay']")
    artist_song_label_elements = driver.find_elements(by=By.CLASS_NAME, value='fontL')

    timestamps, clear_artist_song_label = elements_to_formatted_lists(timestamps_elements, artist_song_label_elements)
    formatted_output = []
    for i in range(len(timestamps)):
        if i == 0:
            formatted_output.append('0:00 ' + clear_artist_song_label[i])
        else:
            formatted_output.append(format_tracklist_output(timestamps[i], clear_artist_song_label[i]))
    driver.close()
    return '\n'.join(formatted_output)