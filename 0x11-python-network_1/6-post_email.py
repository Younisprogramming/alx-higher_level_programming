#!/usr/bin/python3
"""value of emali"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    value = {'email': email}
    response = requests.post(url, data=value)
    print(response.text)
