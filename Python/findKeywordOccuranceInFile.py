import os
import re
#Program to read a text file and search the count of target string available in the text file
def find_file(filename):
    # This is to get the directory that the program
    # is currently running in.
    cwd_path = os.path.dirname(os.path.realpath(__file__))
    print(cwd_path)
   
    # if the file is inside the same workign directory then use - "os.path.abspath(filename)"
    # print(os.path.abspath(filename))

    for root, dirs, fnames in os.walk(os.path.dirname(cwd_path)):
        if filename in fnames:
            print(os.path.join(root, filename), type(os.path.join(root, filename)))
            return os.path.join(root, filename)
    


def findOccurance(filename, targetString):

    # Check the file name for .txt extension ele throw error
    if not filename.endswith(".txt"):
        print("Enter the correct file name with extension")
        exit()

    file_path = find_file(filename)
    count = 0
    with open(file_path, 'r', encoding='utf-8') as fp:
        # ocurrance = re.findall(r'\S+(anshuman)\s+', f.read())
        # print(ocurrance, type(ocurrance))
        # content = f.read()
        
        # if targetString in content:
        #     count +=1 
        #     print("Found the string - {} time".format(count))
       
        contents = fp.read()
        print(contents.count(targetString))
        line_list = contents.split('\n')
        for l_no, line in enumerate(line_list):
            if targetString.lower() in line:
                print("String found at line : {}".format(l_no+1))
                print(line)
        # with regex
        # is_found = re.findall(targetString, fp.read(), re.MULTILINE)
        # print(is_found)
   
if __name__ == '__main__':
    filename = "moonlanding.txt"
    string1 = "moon"
    findOccurance(filename, string1)