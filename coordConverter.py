import requests
import csv
import re

url = 'https://dapi.kakao.com/v2/local/geo/transcoord.json'
params = {'input_coord': 'WTM', 'output_coord': 'WGS84'}
headers = {
	'Authorization': 'KakaoAK f0adefbdde707e6e2a62ed70bb51e883',
	'Content-Type': 'application/json; charset=utf-8'
}

def converter(x, y):
	params['x'] = x
	params['y'] = y
	res = requests.get(url, params=params, headers=headers)
	return res.json()['documents'][0]

fr = open('WATER_PIEPLINE.csv', 'r', encoding='euc-kr')
rdr = csv.reader(fr)
fw = open('WATER_PIEPLINE2.csv', 'a', encoding='euc-kr', newline='')
wr = csv.writer(fw)
for i, line in enumerate(rdr):
	if i < 4711:
		continue
	if i != 0:
		coord = [x for x in re.split("[\b(MULTILINESTRING)\b\s,)(]+",line[0]) if x != '']
		length = len(coord)
		new_line = 'MULTILINESTRING (('
		if length % 2 == 1:
			raise Exception('Something wrong... Check csv file!');
		for i in range((int)(length/2)):
			tmp = converter(coord[2*i], coord[2*i+1])
			if i != 0:
				new_line += ','
			new_line += str(tmp['x']) + ' ' + str(tmp['y'])
		new_line += '))'
		line[0] = new_line
	wr.writerow(line)

fr.close()
fw.close()