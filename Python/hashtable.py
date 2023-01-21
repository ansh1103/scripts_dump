class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    # this function will take the key which is a string and return the hash of the string
    # the hash function is derived by adding the ascii value of all the characters in the string key
    # and then doing mod 100(%100)
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, value):
        hash = self.get_hash(key)
        found = False
        for index, element in enumerate(self.arr[hash]):
            if len(element) == 2 and element[0] == key:
                self.arr[hash][index] = (key, value)
                found = True
                break
        if not found:
            self.arr[hash].append((key, value))

    def __getitem__(self, item):
        hash = self.get_hash(item)
        return self.arr[hash]


if __name__ == '__main__':
    d = HashTable()
    d['march 23'] = 320
    d.__setitem__('march 24', 450)
    d.__setitem__('march 29', 520)
    d['march 23'] = 419
    print('Stock price on march 23 is : {}'.format(d['march 23']))
