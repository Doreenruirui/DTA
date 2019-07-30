from common import book2count, book2century
from info import *
import os
from os.path import join as pjoin


def check_count():
    dict_book2century = book2century()
    dict_book2count = book2count()
    list_files = os.listdir(pjoin(data_folder, 'dta_kernkorpus_2018-10-17'))
    for fn in list_files:
        book_title = fn.split('.')[0]
        if book_title in dict_book2century:
            century = dict_book2century[book_title]
            book_folder = pjoin(data_folder, 'core_image', century, book_title)
            cur_num = os.listdir(book_folder)
            if dict_book2count * 2 != len(cur_num):
                print(fn, dict_book2count - len(cur_num) / 2)


