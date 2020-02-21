#Exercise 1
#Create a python file with 3 functions:
#A def print_file_content(file) that can print content of a csv file to the console

def print_file_content(filename):

    with open(filename) as f_obj:
        content = f_obj.readlines()

    for line in content:
        print(line)

print_file_content('./befkbhalderstatkode.csv')

#B def write_list_to_file(output_file, lst) that can take a list of tuple and write each element to a new line in file
# rewrite the function so that it gets an arbitrary number of strings instead of a list
def write_list_to_file(output_file, lst):
    with open(output_file, 'w') as file_object:
            for lst in lst:
                file_object.write(lst)
                print(lst)

lis = ("first","test","for", "thisssssss")
write_list_to_file("nametowriteto",lis )


#C def read_csv(input_file) that take a csv file and read each row into a list
def read_csv(input_file):

    with open(input_file) as f_obj:
        content = f_obj.readlines()
        
    for line in content[:20]:
        print(line.strip().split(','))

print_file_content('./befkbhalderstatkode.csv')

#Add a functionality so that the file can be called from cli with 2 arguments
#A path to csv file
#B an argument --file file_name that if given will write the content to file_name or otherwise will print it to the console.

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')

    print(parser.parse_args())


