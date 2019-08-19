import os
from os.path import join as pjoin
from DTA.info import *
from DTA.common import book2century
from distutils.dir_util import copy_tree
from shutil import copyfile


def build_core():
    dict_book2century = book2century()
    list_files = os.listdir(pjoin(data_folder, 'dta_kernkorpus_2018-10-17'))
    for fn in list_files:
        book_title = fn.split('.')[0]
        if book_title in dict_book2century:
            century = dict_book2century[book_title]
            century_folder = pjoin(data_folder, 'core_image', century)
            if not os.path.exists(century_folder):
                os.makedirs(century_folder)
            if os.path.exists(pjoin(century_folder, book_title)):
                continue
            image_folder = pjoin(data_folder, 'all_image', century, book_title)
            copy_tree(image_folder, pjoin(century_folder, book_title))


def buil_core_xml():
    dict_book2century = book2century()
    list_files = os.listdir(pjoin(data_folder, 'dta_kernkorpus_2018-10-17'))
    for fn in list_files:
        book_title = fn.split('.')[0]
        if book_title in dict_book2century:
            century = dict_book2century[book_title]
            century_folder = pjoin(data_folder, 'core_xml', century)
            if not os.path.exists(century_folder):
                os.makedirs(century_folder)
            copyfile(pjoin(data_folder, 'dta_kernkorpus_2018-10-17', fn), pjoin(century_folder, fn))

#build_core()





