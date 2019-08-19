import os
from os.path import join as pjoin
import numpy as np
from bs4 import BeautifulSoup


img_folder = '/scratch/dong.r/Dataset/DTA/core_image'
data_folder = '/scratch/dong.r/Dataset/DTA'

with open(pjoin(data_folder, 'list_lang'), 'w', encoding='utf-8') as f_out:
    books = os.listdir(img_folder)
    for bn in books:
        with open(pjoin(data_folder, 'core_xml', bn + '.TEI-P5.xml'), encoding='utf-8') as f_:
            content = f_.read()
            cur_xml = BeautifulSoup(content, 'xml')
            lang_list = cur_xml.find_all('language')
            cur_lang = lang_list[0]["ident"]
            f_out.write('%s\t%s\n' % (bn, cur_lang))