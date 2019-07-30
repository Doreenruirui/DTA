from os.path import join as pjoin
import requests
from bs4 import BeautifulSoup
from info import *
from common import books


def get_font_info():
    book_no = 0
    with open(pjoin(data_folder, 'list_font'),  'w', encoding='utf-8') as f_out:
        for century, book_title, text in books():
            book_no += 1
            print(book_no)
            cur_book_info_url = book_info_url % book_title
            content = requests.get(cur_book_info_url).text
            cur_html = BeautifulSoup(content, 'html')
            all_tds = cur_html.body.find_all('td')
            num_tds = len(all_tds)
            for i in range(num_tds):
                if all_tds[i].text == 'Schriftart:':
                    f_out.write(all_tds[i+1].text + '\n')
                    break


def get_page_count_info():
    book_no = 0
    with open(pjoin(data_folder, 'list_page_count_new'),  'w', encoding='utf-8') as f_out:
        for century, book_title, text in books():
            book_no += 1
            print(book_no)
            cur_book_info_url = book_info_url % book_title
            content = requests.get(cur_book_info_url).text
            cur_html = BeautifulSoup(content, 'html')
            all_tds = cur_html.body.find_all('td')
            num_tds = len(all_tds)
            for i in range(num_tds):
                if all_tds[i].text == 'Scans:':
                    f_out.write(century + '\t' + book_title + '\t' + all_tds[i+1].text + '\n')
                    break


def get_annotations():
    num_wiki = 0
    num_annot = 0
    with open(pjoin(data_folder, 'list_wiki_TEI'), 'w', encoding='utf-8') as f_out:
        for century, book_title, text in books():
            book_path = pjoin(data_folder, 'all_xml', century, '%s.TEI-P5.ling.xml' % book_title)
            if not os.path.exists(book_path):
                continue
            with open(book_path, encoding='utf-8') as f_:
                content = f_.read()
                if 'a href="http://de.wikisource.org/wiki/Wikisource' in content:
                    num_wiki += 1
                    print(book_path)
                    f_out.write(century + '\t' + book_title + '\n')
                else:
                    num_annot += 1

        print(num_wiki, num_annot)


def get_book_from_wiki():
    book_no = 0
    wiki_no = 0
    with open(pjoin(data_folder, 'list_wiki'),  'w', encoding='utf-8') as f_out:
        for century, book_title, text in books():
            book_no += 1
            print(book_no)
            cur_book_info_url = book_info_url % book_title
            content = requests.get(cur_book_info_url).text
            if 'Wikisource' in content:
                wiki_no += 1
                print(wiki_no, book_title)
                f_out.write(book_title + '\n')


def get_mix_font():
    file_path = pjoin(data_folder, 'all_xml', '19', 'heeren_staatensystem_1809' + xml_postfix)
    with open(file_path, encoding='utf-8') as f_:
        content = f_.read()
        cur_xml = BeautifulSoup(content, 'xml')
        fonts = cur_xml.body.find_all('hi')
        print(fonts)


def count_images():
    dict_book2count = {}
    with open(pjoin(data_folder, 'download_cmd_all'), encoding='utf-8') as f_:
        for line in f_:
            items = line.strip().split()
            book = items[2][len('/home/rui/Dataset/DTA/all_image/17/'):-len('/0001.png')]
            dict_book2count[book] = dict_book2count.get(book, 0) + 1
    with open(pjoin(data_folder, 'list_count'), 'w', encoding='utf-8') as f_:
        for book in dict_book2count:
            f_.write(book + '\t' + str(dict_book2count[book]) + '\n')



# def get_proportions_of_mix_language():
#

# def get_proportion_of_mix_font():
# count_images()
get_font_info()
# get_page_count_info()