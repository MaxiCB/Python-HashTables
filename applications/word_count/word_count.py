import re


def word_count(s):
    s = s.lower()
    temp: list[str] = s.split(' ')
    output = {}
    for word in temp:
        test = re.sub('[ \\\\":;,-.+=)/|[\]{}(&*^ ]', '', word)
        if test != '':
            if test in output:
                output[test] += 1
            else:
                output[test] = 1
    return output


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
