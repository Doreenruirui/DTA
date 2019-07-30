import os
import json


dict_place_len = {}
dict_place_line = {}
for fn in files:
	with open(fn, encoding='utf-8') as f_:
		for line in f_:
			cur_dict = json.loads(line)
			cur_place = cur_dict["place"]
			cur_text = cur_dict["text"]
			lines = [ele.strip() for ele in cur_text.split() if len(ele.strip()) > 0]
			nline  = len(lines)
			if nline > 0:
				dict_place_line[cur_place] = dict_place_line.get(cur_place, 0) + nline
				dict_place_len[cur_place] = dict_place_len.get(cur_place, 0) + sum([len(ele) for ele in lines])
		
