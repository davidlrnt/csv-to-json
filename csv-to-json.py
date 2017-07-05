import os
import glob
import csv
import json
from os.path import basename

path = os.path.basename('/csv')

for filename in glob.glob(os.path.join(path, '*.csv')):
	baseName = basename(filename).replace(".csv", "")

	newObj = {}
	newObj[baseName] = []

	with open(filename, newline='') as csvfile:
		csvRead = csv.reader(csvfile, delimiter='	', quotechar='|')

		index = 0
		keys = []
		for row in csvRead:
			if index == 0:
				keys = row
			else:
				rowObj = {}
				for i, key in enumerate(keys):
					rowObj[key] = row[i]
				newObj[baseName].append(rowObj)
			index += 1

	out = os.path.join(path, baseName + '.json')
	with open(out, 'w') as outfile:
		json.dump(newObj, outfile)