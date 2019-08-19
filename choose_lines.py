from os.path import join as pjoin
from info import root_folder, book_info_folder
import random
import sys

def choose_lines(font, cent, start, end, split_id):
    books = []
    with open(pjoin(root_folder, '%s_%d_%d' % (font, cent, split_id)), encoding='utf-8') as f_:
        for line in f_:
            books.append(line.strip())
    chosen_books = books[start:end]
    all_lines = []
    for bn in chosen_books:
        with open(pjoin(book_info_folder, bn), encoding='utf-8') as f_in:
            all_lines += f_in.readlines()[1:]
    random.shuffle(all_lines)
    with open(pjoin(root_folder, '%s_%d_%d_%d_%d' % (font, cent, start, end, split_id)), 'w', encoding='utf-8') as f_out:
        f_out.write(str(len(all_lines)) + '\n')
        for line in all_lines:
            f_out.write(line)

choose_lines(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]))





