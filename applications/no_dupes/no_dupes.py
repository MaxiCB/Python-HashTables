def no_dupes(s):
    # temp = s.split(" ")
    # out_set = set(temp)
    #
    # return " ".join(out_set)

    out = []
    for i in s.split():
        if s.count(i) > 1 and (i not in out) or s.count(i) is 1:
            out.append(i)
    return ' '.join(out)


if __name__ == "__main__":
    print(no_dupes(""))
    print(no_dupes("hello"))
    print(no_dupes("hello hello"))
    print(no_dupes("cats dogs fish cats dogs"))
    print(no_dupes("spam spam spam eggs spam sausage spam spam and spam"))