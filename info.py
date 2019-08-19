import os

if os.path.exists('/Users/ruidong/Documents/Dataset/DTA'):
    data_folder = '/Users/ruidong/Documents/Dataset/DTA'
else:
    # data_folder = '/home/rui/Dataset/DTA'
    data_folder = '/scratch/dong.r/Dataset/DTA'

xml_url = 'http://www.deutschestextarchiv.de/book/download_xml/%s'
image_url = 'http://media.dwds.de/dta/images/%s/%s_%s_1600px.jpg'
book_page_url = 'http://www.deutschestextarchiv.de/book/view/%s?p=1'
book_info_url = 'http://www.deutschestextarchiv.de/book/show/%s'
xml_postfix = '.TEI-P5.ling.xml'

root_folder = '/scratch/dong.r/Dataset/DTA'
img_folder = root_folder + '/core_image'
align_folder = root_folder + '/out.json'
seg_folder = root_folder + '/core_segment'
book_info_folder = root_folder + '/book_info'