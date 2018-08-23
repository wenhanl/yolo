import csv

'''
Pre-conversion command: awk -F, ' { print $1,$5,$7,$6,$8,$3 } ' OFS="," training_data.csv
'''

with open('./model_data/google_classes.txt') as f:
    classes = f.read().splitlines()
    class_to_id = {classes[index]: index for index in range(len(classes))}

with open('./trimed_training.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    prev_row = None
    for row in reader:
        if prev_row and prev_row[0] != row[0]:
            print(row_string)
            row_string = '/home/ubuntu/data/train/' + row[0] + '.jpg'
        if not prev_row:
            row_string = '/home/ubuntu/data/train/' + row[0] + '.jpg'
        row_string += ' '
        row_string += ','.join(row[1:-1])
        row_string += ','
        row_string += str(class_to_id[row[-1]])
        prev_row = row
