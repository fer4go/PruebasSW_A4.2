"""Word count
Program to Count words within a text file
The program reads a file with a list of wrods and counts
how many of them are duplicated
"""

import sys
import time


def read_file(fname):
    """
    Function to read the file.
    Returns a list of type string
    """
    print("Working file: " + fname)

    lista = []
    try:
        with open(fname, 'r', encoding='utf-8') as data:
            lista = list(data)
    except FileNotFoundError:
        print("File not found!")

    return lista


def count_repeated(lista):
    """
    Counts the number of times a word is in the list
    """
    counter = {}
    for word in lista:
        counter[word] = counter.get(word, 0) + 1
    return counter


def save_file(word_lista):
    """
    function to save the resulst into a txt file
    """
    with open("WordCountResults.txt", 'w', encoding='utf-8') as res_file:
        res_file.write("Word Count Results:\n")
        res_file.write("Row Labels - Count\n")
        for word, count in word_lista.items():
            str_count = str(count)
            res_file.write(word + " -> " + str_count + "\n")


def main():
    """
    main Function
    """
    start_time = time.time()

    path = ''
    if len(sys.argv) == 2:
        path = sys.argv[1]
    else:
        print("Not enough input paramenters: Missing file name.")
        print("Run script: python compute_statistics.py path/datafile.txt")
        sys.exit(0)

    lista = []
    lista = read_file(path)
    print(len(lista))

    # lista = ['hola', 'mundo', 'cruel', 'cruel']

    word_list = count_repeated(lista[:])
    save_file(word_list)

    elapsed_time = time.time() - start_time
    print("Time taken: " + str(elapsed_time) + " seconds.\n")


if __name__ == '__main__':
    main()
