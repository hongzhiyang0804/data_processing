f = open("sqlResult_2470282.txt")
all_lines = f.readlines() #读取全部内容
for line in all_lines:
    line = line.split('临床意义')[0]
    line = line.split('苔色')[-1] + ',' +'\n'
    with open('moss_color.csv', 'a') as file:
        file.write(line)
    print(line)
