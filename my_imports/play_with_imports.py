#from another_file import another_file_function, another_file_variable
import another_file
from pprint import pprint

def main():
    another_file_function()
    print(another_file_variable)

if __name__ == "__main__":
    main()
