from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class TracklistFormatter:
    """
    A class to format tracklists from 1001tracklists.com into YouTube comments.
    Includes error handling and optimizations.
    """
    def __init__(self, timeout=10):
        """
        Initialize the TracklistFormatter.

        Args:
            timeout (int): Maximum wait time for page elements to load (default: 10 seconds).
        """
        self.service = Service()
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')  # Run in headless mode for better performance
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--no-sandbox')
        self.timeout = timeout

    def tracklist1001_url_to_youtube_comment(self, url: str) -> str:
        """
        Convert a 1001tracklists.com URL to a formatted YouTube comment.

        Args:
            url (str): The URL of the tracklist on 1001tracklists.com.

        Returns:
            str: A formatted string suitable for a YouTube comment.

        Raises:
            Exception: If there's an error during the process.
        """
        try:
            driver = webdriver.Chrome(service=self.service, options=self.options)
            driver.get(url)

            # Wait for the essential elements to load
            wait = WebDriverWait(driver, self.timeout)
            timestamps_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='bPlay']")))
            artist_song_label_elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'fontL')))

            timestamps = self.__process_timestamps(timestamps_elements)
            clear_artist_song_label = self.__process_artist_song_labels(artist_song_label_elements)

            formatted_output = self.__format_output(timestamps, clear_artist_song_label)
            
            driver.quit()
            return '\n'.join(formatted_output)

        except TimeoutException:
            raise Exception("Timed out waiting for page elements to load")
        except NoSuchElementException:
            raise Exception("Required elements not found on the page")
        except Exception as e:
            raise Exception(f"An error occurred: {str(e)}")

    def __process_timestamps(self, timestamps_elements):
        """
        Process timestamp elements.

        Args:
            timestamps_elements (list): List of Selenium elements containing timestamps.

        Returns:
            list: Processed timestamps.
        """
        return [self.__format_timestamp(ele.text) for ele in timestamps_elements if ele.text]

    def __format_timestamp(self, text):
        """Format a single timestamp."""
        return text[3:] + ' w/' if text[0] == 'w' else text[3:]

    def __process_artist_song_labels(self, artist_song_label_elements):
        """
        Process artist/song label elements.

        Args:
            artist_song_label_elements (list): List of Selenium elements containing artist/song labels.

        Returns:
            list: Processed artist/song labels.
        """
        return [ele.text for ele in artist_song_label_elements if ele.text]

    def __format_output(self, timestamps, clear_artist_song_label):
        """
        Format the final output.

        Args:
            timestamps (list): List of processed timestamps.
            clear_artist_song_label (list): List of processed artist/song labels.

        Returns:
            list: Formatted output lines.
        """
        formatted_output = ['0:00 ' + clear_artist_song_label[0]]
        formatted_output.extend(
            self.__format_tracklist_output(timestamps[i], clear_artist_song_label[i])
            for i in range(1, len(timestamps))
        )
        return formatted_output

    def __format_tracklist_output(self, timestamp, artist_song):
        """
        Format a single track entry.

        Args:
            timestamp (str): The timestamp for the track.
            artist_song (str): The artist and song information.

        Returns:
            str: A formatted string for the track entry.
        """
        if not timestamp:
            return artist_song
        elif timestamp[0] == ' ' or timestamp[1] == 'w':
            return f' {timestamp} {artist_song}'
        else:
            return f'{timestamp} {artist_song}'

url = "https://1001.tl/rn1qu9t"         
try:
    formatter = TracklistFormatter(timeout=10)  # Increase timeout if needed
    formatted_comment = formatter.tracklist1001_url_to_youtube_comment(url)
    print(formatted_comment)
except Exception as e:
    print(f"Error: {str(e)}")