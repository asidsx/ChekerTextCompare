
with open('data.json', 'r', encoding='utf-8') as data_file, \
     open('old.txt', 'r', encoding='utf-8') as old_file, \
     open('error.txt', 'w', encoding='utf-8') as error_file:
    

    data_lines = data_file.readlines()

    old_lines = old_file.readlines()

    old_lines = [line.strip() for line in old_lines]


    not_found = []


    for line in data_lines:
        if line.strip() in old_lines:
            continue
        not_found.append(line)


    error_file.writelines(not_found)


    data_file.seek(0)
    data_file.truncate()
    data_file.writelines(not_found)
