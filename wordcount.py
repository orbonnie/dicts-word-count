import re

def count_words(filename):
    """Count words in file."""

    count = {}
    input_file = open(filename)
    for line in input_file:
        line = re.sub(r"[^\w\s]", "", line).lower()
        words = line.rstrip().split(" ")
        for word in words:
            if word:
                if word.strip() in count:
                    count[word.strip()] += 1
                else:
                    count [word.strip()] = 1

    sorted_count = sorted(count.items(), key=lambda item: item[1])

    for value in sorted_count:
        print(value[0], value[1])

    return count


results = count_words('twain.txt')

# print(results)