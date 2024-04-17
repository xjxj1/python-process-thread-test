import requests
from PIL import ImageFile
import numpy as np

from const import CalcType
class Downloader:
    '''
    Class to download files from the internet
    '''
    def __init__(self):
        '''
        Initialize the class
        '''
        self.calc_type = CalcType.SingleThread

    def set_calc_type(self, calc_type):
        '''
        Set the calculation type
        '''
        self.calc_type = calc_type
    def _download(self, url):
        '''
        Process the URL to download the file
        '''
        print('downloading url is:', url)
        response = requests.get(url)
        content = response.content
        # transform image to numpy array
        parser = ImageFile.Parser()
        parser.feed(content)
        image = parser.close()
        image = np.array(image)
        return image

    def _process_singlethread(self, list_of_urls):
        '''
        Process the list of URLs to download the files
        '''
        response_list = []
        for url in list_of_urls:
            img = self._download(url)
            response_list.append(img)
        return response_list

    def process(self, list_of_urls):
        '''
        Process the list of URLs to download the files
        '''
        return self._process_singlethread(list_of_urls)