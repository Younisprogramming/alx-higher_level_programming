#!/usr/bin/python3
""" akwmlam.a/aaa//a,da"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))
