from bs4 import BeautifulSoup
from os.path import join as pjoin
import subprocess
from shutil import move
import requests
from multiprocessing import Pool
from DTA.info import *
from DTA.common import books


def get_urls():
    with open(pjoin(data_folder, 'list_urls'), 'w', encoding='utf-8') as f_out:
        book_info_prefix = 'http://www.deutschestextarchiv.de/book/show/'
        html_files = ['century_%d' % i for i in range(17, 21)]
        for fn in html_files:
            with open(pjoin(data_folder, fn), encoding='utf-8') as f_:
                content = f_.read()
                cur_html = BeautifulSoup(content, 'html')
                list_refs = [ele for ele in cur_html.body.find_all('a') if book_info_prefix in ele['href']]
                for ele in list_refs:
                    f_out.write('%s\t%s\t%s\n' % (fn[-2:],
                                                  ele['href'][len(book_info_prefix):],
                                                  ele.text))


def download_xml():
    with open(pjoin(data_folder, 'list_urls'), encoding='utf-8') as f_:
        for century, book_title, text in books():
            cur_xml_name = book_title + '.TEI-P5.ling.xml'
            if not os.path.exists(pjoin(data_folder, 'dta-lingattr-tei_2019-02-06', cur_xml_name)):
                print(book_title)
                cur_xml_url = xml_url % book_title
                subprocess.run('wget -O %s \'%s\'' % (pjoin(data_folder, 'all_xml', century, cur_xml_name), cur_xml_url), shell=True)
            else:
                move(pjoin(data_folder, 'dta-lingattr-tei_2019-02-06', cur_xml_name), pjoin(data_folder, 'all_xml', century, cur_xml_name))


def get_cmds():
    i = 0
    with open(pjoin(data_folder, 'download_cmd'), 'w', encoding='utf-8') as f_out:
        for century, book_title, text in books():
            print(i)
            i += 1
            book_folder = pjoin(data_folder, 'all_image', century, book_title)
            cur_book_page_url = book_page_url % book_title
            content = requests.get(cur_book_page_url).text
            cur_html = BeautifulSoup(content, 'html')
            cur_pages = [ele.text[:4] for ele in cur_html.body.find_all('option')]
            for page in cur_pages:
                cur_image_url = image_url % (book_title, book_title, page)
                download_cmd = 'wget -O %s \'%s\'' % (pjoin(book_folder, page + '.png'), cur_image_url)
                f_out.write(download_cmd + '\n')


def download_image(download_cmd):
    subprocess.run(download_cmd, shell=True)


def make_book_folder():
    for century, url, text in books():
        book_title = url[len('http://www.deutschestextarchiv.de/book/show/'):]
        book_folder = pjoin(data_folder, 'all_image', century, book_title)
        if not os.path.exists(book_folder):
            os.makedirs(book_folder)


def batch_download_image():
    pool = Pool(10)
    cmd_list = []
    with open(pjoin(data_folder, 'download_cmd'), encoding='utf-8') as f_:
        for line in f_:
            cmd_list.append(line.strip())
    pool.map(download_image, cmd_list)


# get_urls()
# download_xml()
# get_cmds()
# make_book_folder()
# batch_download_image()



