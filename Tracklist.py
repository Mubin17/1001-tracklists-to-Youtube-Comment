from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
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

def print_formatted_youtube_comment(timestamps, clear_artist_song_label):
    for i in range(len(timestamps)):
        if i == 0: 
            print('0:00',clear_artist_song_label[i])
        elif timestamps[i] == '':
            print(timestamps[i], clear_artist_song_label[i])
        elif timestamps[i][1] == 'w':
            print(' ', timestamps[i], clear_artist_song_label[i])
        else:
            print(timestamps[i], clear_artist_song_label[i])

def tracklist1001_url_to_youtube_comment(Chrome_driver_path: str, Url: str):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(Url)

    timestamps_elements = driver.find_elements(by=By.XPATH, value="//div[@class='bPlay']")
    artist_song_label_elements = driver.find_elements(by=By.CLASS_NAME, value='fontL')

    time.sleep(5)
    timestamps, clear_artist_song_label = elements_to_formatted_lists(timestamps_elements, artist_song_label_elements)
    
    print_formatted_youtube_comment(timestamps, clear_artist_song_label)
    driver.close()
