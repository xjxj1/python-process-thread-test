import utils
from modules.downloader import Downloader
class Schedule:
    def __init__(self):
        self.downloader = Downloader()


    def process(self):
        # 1 add image url
        url_list = utils.get_image_urls()
        # 2 download image
        self.downloader.process(url_list)

if __name__ == '__main__':
    schedule = Schedule()
    schedule.process()