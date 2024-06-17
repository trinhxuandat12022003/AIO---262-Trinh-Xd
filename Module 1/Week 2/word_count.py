def count_word(file_path):
    counter = {}
    with open(file_path, 'r') as f:
        for line in f:
            value = line.split()
            for word in value:
                if word in counter:
                    counter[word] += 1
                else:
                    counter[word] = 1

    return counter


file_path = 'P1_data.txt'
result = count_word(file_path)
print(result['man'])
