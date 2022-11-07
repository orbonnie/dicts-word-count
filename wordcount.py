"""Count words in file."""


# put your code here.
def count_words(filename):
    count = {}
    input_file = open(filename)
    for line in input_file:
        words = line.split(" ")
        for word in words:
            if word.strip() in count:
                count[word.strip()] +=1
            else:
               count [word.strip()]=1

    for key, value in count.items():
        print(key, value)

    return count


results = count_words('twain.txt')

# print(results)