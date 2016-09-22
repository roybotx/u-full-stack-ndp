with open("my_test_file1.txt", "r") as f1:
    read_from_file_1 = f1.read()

index_list = []
index = 0
while index < len(read_from_file_1):
    index = read_from_file_1.find('|', index)
    if index == -1:
        break
    index_list.append(index)
    index += 1

    f2 = open("my_text_file2.txt", "w+")
    read_from_file_2 = f2.read()
    for i in index_list:
        write_to_file = f2.write(read_from_file_2[:i] + "|" + read_from_file_2[i:])

print(index_list)
print(write_to_file)
f2.close()
