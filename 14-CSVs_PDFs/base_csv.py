import csv


data = open('example.csv', encoding='utf-8')

csv_data = csv.reader(data)

# reformat csv_data into list of lists python object
data_lines = list(csv_data)
full_names = []
for data_line in data_lines[1:]:
    full_names.append(data_line[1] + ' ' + data_line[2])
    print(data_line[3])

file_to_output = open('to_save_file.csv', mode='w', newline='')
csv_writer = csv.writer(file_to_output, delimiter=',')
csv_writer.writerow(['a', 'b','c'])
csv_writer.writerows([['1', '2','3'],['4', '5','6'],['7', '8','9']])
file_to_output.close()

f = open('to_save_file.csv', mode='a', newline='')
csv_writer = csv.writer(f, delimiter=',')
csv_writer.writerow(['10', '11','12'])
f.close()
