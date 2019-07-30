from os.path import join as pjoin
from info import data_folder


def books():
    with open(pjoin(data_folder, 'list_urls'), encoding='utf-8') as f_:
        for line in f_:
            try:
                century, book_title, text = line.strip().split('\t')
                yield century, book_title, text
            except:
                print(line)


def book2century():
    dict_books = {}
    with open(pjoin(data_folder, 'list_urls'), encoding='utf-8') as f_:
        for line in f_:
            century, book_title, text = line.strip().split('\t')
            dict_books[book_title] = century
    return dict_books


def book2count():
    dict_book2count = {}
    with open(pjoin(data_folder, 'list_count'), encoding='utf-8') as f_:
        for line in f_:
            book, count = line.strip().split('\t')
            count = int(count)
            dict_book2count[book] = count
    return dict_book2count
