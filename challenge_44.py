#!/usr/bin/env python3



def main():
    bottles = 99
    while bottles <= 99: 
        print(bottles, "bottles of beer on the wall!", bottles, "bottles of beer! You take one down, pass it around!", bottles," bottles of beer on the wall!")
        bottles -= 1
        if bottles == 0:
            break
if __name__ == "__main__":
    main()
