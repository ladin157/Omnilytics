from file_helper import read_to_dict


def main():
    results = read_to_dict()
    for result in results:
        print(result['text'], ' - ', result['des'])


if __name__ == '__main__':
    main()
