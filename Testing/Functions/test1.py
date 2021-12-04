def longest_english_word(answer):
    longest_word = []
    longest = 0
    for i in answer:
        for char in i:
            if char not in '''qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM''':
                continue
        if len(i) > longest:
            longest = len(i)
            longest_word.clear()
            longest_word.append(i)
        elif len(i) == longest:
            longest_word.append(i)
        else:
            pass
    print(*longest_word)


def common_word(answer):
    cnt = []
    for i in answer:
        cnt.append(len(i))
    print(answer[max(cnt)])


def main():
    filename = input("Give the name of the file:\n")
    with open(filename, encoding='utf-8') as file:
        answer = file.read()
        for i in '''"!"\#$%&()*+-,/:;<=>?@[\\]^_{|}~"''':
            answer = answer.replace(i, '')
        longest_english_word(answer.split())
        common_word(answer.split())


if __name__ == '__main__':
    main()
