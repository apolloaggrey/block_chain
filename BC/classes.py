from time import clock
import hashlib
import random
import math


class Data(object):
    """docstring for Data"""

    def __init__(self, file, line):
        super(Data, self).__init__()
        self.file = file
        try:
            self.line = int(line)
        except Exception as e:
            print(e, ...)

    def __str__(self):
        with open(self.file, mode="r") as file:
            get_line = lambda x, y: x == y
            line_count = 0
            for line in file:
                if get_line(line_count, self.line):
                    return str(line.strip("\n"))
                line_count += 1
            return "Data does not exist ..."


class Block(object):
    """docstring for Block"""

    #class Globals
    chain_number = 0
    links = ["0000", None]

    def __init__(self, name=str("B-"), max_size=int(12)):
        super(Block, self).__init__()
        self.max_size = max_size
        self.difficulty = int(10 / 100 * self.max_size)
        self.link1 = Block.links[Block.chain_number]
        # last difficulty length of hash
        self.link2 = Block.links[Block.chain_number + 1]
        self.chain_number = Block.chain_number
        self.name = name + str(self.chain_number)
        Block.chain_number += 1
        self.time = 10  # time.time()
        self.data = []
        self.size = 0
        self.hash = "None"
        self.confirmed = False

    def add_data(self, data):
        if self.size < self.max_size:
            self.data.append(data)
            self.size += 1
        else:
            print("max_size of " + str(self.max_size) + " attained")

    def size(self):
        self.size = len(self.data)  # fail-safe
        return self.size

    def expand(self, size):
        try:
            self.max_size += int(size)
            self.difficulty = int(30 / 100 * self.max_size)
        except ValueError:
            print("size must be of type int")
        pass

    def hash_word(self, word):
        code = hashlib.sha256(str(word).encode()).hexdigest()  # word
        return code

    def hash_block(self):
        # from preceding block
        nounce1 = self.hash_word(self.time)  # time
        nounce2 = self.hash_word(self.size)  # size
        hashed_data = ""
        for x in self.data:
            hashed_data += self.hash_word(x)
            # print(x, ...)
        hashes = 0
        start = clock()
        while not self.hash.startswith(str(Block.links[self.chain_number])[(self.difficulty) * -1:]):
            hashes += 1
            self.link2 = ""
            sequence = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                        'a', 'b', 'c', 'd', 'e', 'f')
            for x in range(25):
                self.link2 += str(random.choice(sequence))
            nounce0 = self.hash_word(self.link2)  # nounce
            data = ""
            data += nounce0 + nounce1 + nounce2 + hashed_data
            self.hash = self.hash_word(data)  # block
        Block.links.append(None)
        print(self.hash)
        Block.links[self.chain_number + 1] = self.hash
        stop = clock()
        time = (stop - start)
        print("Hashes   :", hashes)
        print("Time     :", time, "(s)")
        print("Speed    :", (hashes / time), "H/s")
        print("Solution :", self.link2)

    def confirm(self):
            # from preceding block
        nounce1 = self.hash_word(self.time)  # time
        nounce2 = self.hash_word(self.size)  # size
        nounce0 = self.hash_word(self.link2)  # nounce//confirm
        data = ""
        data += nounce0 + nounce1 + nounce2
        for x in self.data:
            data += self.hash_word(x)
        # block
        if self.hash.startswith(str(Block.links[self.chain_number])[self.difficulty * -1:]):
            self.confirmed = True
        return self.confirmed
