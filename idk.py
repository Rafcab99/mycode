from pprint import pprint 

import requests

MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():

    groundctrl = requests.get(MAJORTOM)
    groundctrl = groundctrl.json()

    print("\n\nConverted Python data")
    print(groundctrl)

    print('\n\nPeople in Space: ', groundctrl['number'])


