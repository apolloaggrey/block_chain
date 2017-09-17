from classes import Block
from classes import Data
import time


def main():
    # print("enter var >>>")
    # var = input()

    data = [
        Data("test_file.csv", 1),
        Data("test_file.csv", 2),
        Data("test_file.csv", 3),
        Data("test_file.csv", 4),
        Data("test_file.csv", 5),
        Data("test_file2.csv", 1),
        Data("test_file2.csv", 2),
        Data("test_file2.csv", 3),
        Data("test_file2.csv", 4),
        Data("test_file2.csv", 5),
        Data("test_file2.csv", 1),
        Data("test_file.csv", 2), ]

    block1 = Block()
    block1.expand("5")

    block1.add_data(x for x in data)
    print(block1.name, "is of size", block1.max_size)
    print(block1.name, "has", block1.size, "entries")
    block1.hash_block()
    block1.confirm()
    print(block1.confirmed)

    print("\n")
    time.sleep(2)
    print("\n")

    block2 = Block()
    block2.expand(2)
    block2.add_data(x for x in data)
    print( "{0} is of size {1}".format(block2.name,block2.max_size))
    print(block2.name, "has", block2.size, "entries")
    block2.hash_block()
    print(block2.confirm())

    print("\n")
    time.sleep(2)
    print("\n")

    block2 = Block()
    block2.expand("6")
    for x in data:
        block2.add_data(x)
    print(block2.name, "is of size", block2.max_size)
    print(block2.name, "has", block2.size, "entries")
    block2.hash_block()
    print(block2.confirm())

    print("\n")
    time.sleep(2)
    print("\n")

    block2 = Block()
    block2.expand("-2")
    for x in data:
        block2.add_data(x)
    print(block2.name, "is of size", block2.max_size)
    print(block2.name, "has", block2.size, "entries")
    block2.hash_block()
    print(block2.confirm())

    print("\n")
    time.sleep(2)
    print("\n")

    block2 = Block()
    for x in data:
        block2.add_data(x)
    print(block2.name, "is of size", block2.max_size)
    print(block2.name, "has", block2.size, "entries")
    block2.hash_block()
    print(block2.confirm())

    print("\n")
    time.sleep(2)
    print("\n")

    block2 = Block()
    block2.expand("4")
    for x in data:
        block2.add_data(x)
    print(block2.name, "is of size", block2.max_size)
    print(block2.name, "has", block2.size, "entries")
    block2.hash_block()
    print(block2.confirm()
)

if __name__ == '__main__':
    main()
