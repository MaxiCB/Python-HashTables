import string
from applications.histo.bst import BinarySearchTree

class Histo:
    def __init__(self, file: str):
        f = open(file, 'r')
        self.words = f.read().translate(str.maketrans('', '', string.punctuation)).lower().replace('\n', ' ').split(' ')
        self.bst = BinarySearchTree(self.words[0])
        self.counts = {self.words[0]: 1}

    def find_count(self):
        for word in self.words[1:]:
            if self.bst.contains(word):
                self.counts[word] += 1
            else:
                self.bst.insert(word)
                self.counts[word] = 1
        self.counts = sorted(self.counts.items(), key=lambda kv:(-kv[1], kv[0]))

    def print_hist(self):
        for item in self.counts:
            if item[0] is not '':
                hashes = ""
                for mark in range(int(item[1])):
                    hashes += "#"
                print(item[0] + ' '*(15-len(item[0])) + hashes)


if __name__ == '__main__':
    hist = Histo('robin.txt')
    hist.find_count()
    hist.print_hist()
