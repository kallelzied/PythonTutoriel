def count_words():
    results = dict()
    with open("soccer.txt", 'r') as f:
        for line in f:
            for word in line.split():
                results[word] = results.setdefault(word, 0) + 1

    for word, count in sorted(results.items(), key=lambda x: x[1]):
        print('{} {}'.format(count, word))


count_words()
