import argparse
import random

from file_helper import get_file_size
from generator import generate_string


def main():
    while True:
        file_size = get_file_size(filename='strings.txt')
        if abs(file_size - 10) <= 10e-4:
            break
        str_types = ['alphabetical', 'int', 'real', 'alphanumeric']
        choice = random.choice(str_types)
        generated_str = generate_string(default_type=choice)
        with open('strings.txt', mode='a+') as f:
            f.write(', ' + generated_str.__str__())


if __name__ == '__main__':
    main()
