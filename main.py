import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description='Arguments parsing for hoovada.')
    group = parser.add_argument_group('Arguments')
    group.add_argument('-m', '--mode', required=False, type=str,
                       help='Mode to run app. Mode can be dev or prod')
    group.add_argument('-i', '--ip', required=False, type=str,
                       help='The IP address')
    group.add_argument('-p', '--port', required=False, type=str,
                       help='The port to run app')
    arguments = parser.parse_args()
    return arguments


def main(args):
    pass


if __name__ == '__main__':
    args = parse_args()
    main(args)
