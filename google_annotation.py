import csv

'''
Pre-conversion command: awk -F, ' { print $1,$5,$7,$6,$8,$3 } ' OFS="," training_data.csv
'''

with open('./image_data/trimed_training.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    row_string = ''
    prev_row = None
    for row in reader:
        if prev_row and prev_row[0] != row[0]:
            print(row_string)
            row_string = '~/data/train/' + row[0] + '.jpg'
        row_string += ' '
        row_string += ','.join(row[1:])
        prev_row = row
