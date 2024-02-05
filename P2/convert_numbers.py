"""Convert numbers
Program to Convert decimal numbers into Binary and
Hexadecimal formats
The program reads a file with a list of numbers and the results
are displayed into the console and also saved to a txt file.
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


def convert_to_binary(lnum):
    """
    Convert a list of integer numbers into a list of their binary
    representation
    """
    numbers = lnum[:]
    binary_list = []

    for number in numbers:
        nu = number
        binary = ''

        if number == 0:
            binary = '0' + binary

        while nu != 0:
            bin = int(nu % 2)
            nu = int(nu / 2)
            binary = str(bin) + binary

        binary_list.append(binary)

    return binary_list


def convert_to_hexadecimal(lnum):
    """
    Convert a list of integer numbers into a list of their hexadecimal
    representation
    """
    numbers = lnum[:]
    hexa_list = []

    for number in numbers:
        nu = number
        hexadecimal = ''
        hex_str = ''

        if number == 0:
            hexadecimal = '0' + hexadecimal

        while nu != 0:
            hex = int(nu % 16)
            nu = int(nu / 16)

            if (hex == 15):
                hex_str = 'F'
            elif (hex == 14):
                hex_str = 'E'
            elif (hex == 13):
                hex_str = 'D'
            elif (hex == 12):
                hex_str = 'C'
            elif (hex == 11):
                hex_str = 'B'
            elif (hex == 10):
                hex_str = 'A'
            else:
                hex_str = str(hex)

            hexadecimal = hex_str + hexadecimal

        hexa_list.append(hexadecimal)

    return hexa_list


def save_file(lista, bin_list, hex_list):
    """
    function to save the resulst into a txt file
    """
    with open("ConversionResults.txt", 'w', encoding='utf-8') as res_file:
        res_file.write("Conversion Results:\n")
        res_file.write("NUMBER - BINARY - HEXADECIMAL\n")
        for i in range(len(lista)):
            res_file.write(
                str(lista[i]) + " - " + bin_list[i] +
                " - " + hex_list[i] + "\n")


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

    # lista = ['15', '16', '32', 'VAL']
    numbers_list = list_str_to_number(lista[:])

    # print(lista)
    # print(numbers_list)

    bin_list = convert_to_binary(numbers_list)
    hex_list = convert_to_hexadecimal(numbers_list)

    save_file(numbers_list, bin_list, hex_list)

    elapsed_time = time.time() - start_time
    print("Time taken: " + str(elapsed_time) + " seconds.\n")


if __name__ == '__main__':
    main()
