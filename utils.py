import os

def get_image_urls():
    '''
    Get the list of image URLs from the file
    '''
    image_file = os.path.join('imageslist/baidu.txt')
    url_list = []
    with open(image_file, 'r') as file:
        for line in file:
            url_list.append(line.strip())
    return url_list