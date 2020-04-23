#!/usr/bin/python3
import sys
import os


def arg_error():
    print("\nERROR: Incorrect arguments supplied!")
    print("To view helpful information on how to use this script, try {} -h".format(sys.argv[0]))
    exit()


def write_to_new_file(filename, text):
    try:
        f = open(filename, "x")  # a=append, w=overwrite, r=read, x=create
        f.write(text + "\n")
        f.close()
        read_file(filename)

    except FileExistsError:
        print("File already exists - Cannot create new file")
        exit()


def overwrite_existing_file(filename, text):
    f = open(filename, "w")  # a=append, w=overwrite, r=read, x=create
    f.write(text + "\n")
    f.close()
    read_file(filename)


def append_to_existing_file(filename, text):
    f = open(filename, "a")  # a=append, w=overwrite, r=read, x=create
    f.write(text + "\n")
    f.close()
    read_file(filename)


def read_file(filename):
    try:
        f = open(filename)
        contents = f.read()
        print(contents)
        f.close()
    except FileNotFoundError:
        print("ERROR: File not found")
    else:
        print(filename + " read OK")


def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(filename + " deleted OK")
        exit()
    else:
        print("ERROR: File not found")


def main():
    argv_count = len(sys.argv) - 1

    if argv_count == 1:
        if sys.argv[1] == "-h" or sys.argv[1] == "--h":
            print('''usage: 
{0} -h to view this help text
{0} -r [filename] to read contents of a file
{0} -d [filename] to delete a file
{0} -a [filename] ["text"] append text to an existing file\
or create a new file if it does not exist
{0} -w [filename] ["text"] to overwrite an existing file\
 or create a new file if it does not exist'''.format(sys.argv[0]))
            exit()
        else:
            arg_error()

    elif argv_count != 2 and argv_count != 3:
        arg_error()

    elif argv_count == 3:
        txt = sys.argv[3]

    action, file = sys.argv[1], sys.argv[2]

    if action == '-r' and argv_count == 2:
        read_file(file)
    elif action == '-d' and argv_count == 2:
        delete_file(file)
    elif action == '-a' and argv_count == 3:
        append_to_existing_file(file, txt)
    elif action == '-w' and argv_count == 3:
        overwrite_existing_file(file, txt)
    elif action == 'n':
        write_to_new_file(file, txt)
    else:
        print("ERROR: Invalid arguments")
        exit()


if __name__ == '__main__':
    main()
