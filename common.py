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
    dict_book2font = {}
    fonts = []
    with open(pjoin(data_folder, 'list_font'), encoding='utf-8') as f_:
        for line in f_:
            fonts.append(line.strip())
    with open(pjoin(data_folder, 'list_urls'), encoding='utf-8') as f_:
        i = 0
        for line in f_:
            century, book_title, text = line.strip().split('\t')
            dict_books[book_title] = century
            dict_book2font[book_title] = fonts[i]
            i += 1
    return dict_books, dict_book2font



def book2count():
    dict_book2count = {}
    with open(pjoin(data_folder, 'list_count'), encoding='utf-8') as f_:
        for line in f_:
            book, count = line.strip().split('\t')
            count = int(count)
            dict_book2count[book] = count
    return dict_book2count


def book2lang():
    dict_book2lang = {}
    with open(pjoin(data_folder, 'list_lang'), encoding='utf-8') as f_:
        for line in f_:
            book, lang = line.strip().split('\t')
            dict_book2lang[book] = lang
    return dict_book2lang