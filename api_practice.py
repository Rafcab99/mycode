#!/usr/bin/env python3

from pprint import pprint
import urllib.request
import json

MAJORTOM = "http://api.open-notify.org/astros.json"

def main():
    groundctrl = urllib.request.urlopen(MAJORTOM)
    
    helmet = groundctrl.read()

    helmet = json.loads(helmet.decode("utf-8"))
    print("This is our JSON converted to a Pythonic dictionary =>")
    pprint(helmet)
    print("=====================================================")
    print(f"There are {helmet['number']} people in space.")

    for astro in helmet['people']:
        print(f"{astro['name']} is on the craft {astro['craft']}")

if __name__ == "__main__":
    main()
