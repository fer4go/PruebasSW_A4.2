"""Compute Statistics
Program that reads a file with a list of numeric values, counts the
number of values and performs MEAN, MEDIAN, MODE, STANDARD DEVIATION
(SD), and VARIANCE.
The results are displayed into the console and also saved to a txt file.
"""

import sys
import time
import math


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


def list_str_to_number(lista):
    """
    Converts a list of strings to numbers
    """
    # return [int(x) if x.isdigit() else float(x) for x in lista]
    numbers = []
    for number in lista:
        try:
            if number.isdigit():
                numbers.append(int(number))
            else:
                numbers.append(float(number))
        except ValueError:
            print("Invalid numeric data: " + number)

    return numbers


def calc_mean(nlist):
    """
    Calculate the MEAN from a list of numbers.
    """
    nlen = len(nlist)

    sum = 0
    for number in nlist:
        sum = number + sum

    return str(sum/nlen)


def calc_median(nlist):
    """
    Calculate the MEDIAN from a list of numbers.
    """
    numbers = nlist
    med = int(len(numbers)/2)

    # order the list
    output = []
    while numbers:
        smallest = min(numbers)
        index = numbers.index(smallest)
        output.append(numbers.pop(index))

    median = 0
    if med % 2:
        # odd number
        median = (output[med] + output[med + 1])/2
    else:
        # even number
        median = output[med]

    return str(median)


def calc_mode(nlist):
    """
    Calculate the MODE from a list of numbers.
    """

    dict = {i: nlist.count(i) for i in nlist}
    mode = max(dict, key=dict.get)

    return str(mode)


def calc_sd(nlist, media):
    """
    Calculate the STANDARD DEVIATION from a list of numbers.
    """
    med = float(media)
    sum = 0
    for number in nlist:
        sum = (number - med)*(number - med) + sum

    sum = sum / len(nlist)
    stdev = math.sqrt(sum)

    return str(stdev)

if __name__ == '__main__':
    """
    Main function
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
    numbers_list = list_str_to_number(lista[:])

    mean = calc_mean(numbers_list[:])
    mode = calc_mode(numbers_list[:])
    median = calc_median(numbers_list[:])
    stdev = calc_sd(numbers_list, median)
    count = str(len(numbers_list))

    print("Count: " + count)
    print("Mean: " + mean)
    print("Median: " + median)
    print("Mode: " + mode)
    print("SD: " + stdev)

    with open("StatisticsResults.txt", 'w', encoding='utf-8') as res_file:
        res_file.write("Compute Statistics:\n")
        res_file.write("Count: " + count + "\n")
        res_file.write("Mean: " + mean + "\n")
        res_file.write("Median: " + median + "\n")
        res_file.write("Mode: " + mode + "\n")
        res_file.write("Standar Deviation: " + stdev + "\n")

    elapsed_time = time.time() - start_time

    print("Time taken: " + str(elapsed_time) + " seconds.\n")
