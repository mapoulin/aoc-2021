from urllib.request import Request, urlopen
from urllib.error import HTTPError
from os.path import dirname, abspath, exists
import os

SESSION = os.environ['AOC_SES']
INPUT_URL = "https://adventofcode.com/2021/day/{day_number}/input"
INPUT_FILE_PATH = "./d{day_number}/input.txt"

def read_input(day_number):
    input_url = INPUT_URL.format(day_number = day_number)
    input_file = INPUT_FILE_PATH.format(day_number = day_number)

    return download_to_file(input_url, input_file) \
        if not exists(input_file) else read_file(input_file)

def download_to_file(url, path):
    request = Request(url, headers={"cookie": "session=" + SESSION})

    try:
        with urlopen(request) as response, open(path, 'wb') as out_file:
            data = response.read()
            out_file.write(data)

        return data.decode().splitlines()
    except HTTPError as e:
        print(e)
        print(e.read().decode())
        exit()

def read_file(path):
    with open(path, 'r') as file:
        return [line.rstrip() for line in file]
