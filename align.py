import json

with open('data/part-00180-7440b052-9409-46d9-bd4f-6257a22f5e6d-c000.json', encoding='utf-8') as f_:
    for line in f_:
        cur_line = json.loads(line)
        gt = cur_line["talg"]
        ocr = cur_line["walg"]
