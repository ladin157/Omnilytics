import random
import string


def _alphabetical():
    letters = string.ascii_letters
    length = random.randint(3, 15)
    mystr = ''.join(random.choices(letters, k=length))
    return mystr


def _real():
    return random.uniform(10, 1000000)


def _integers():
    return random.randint(1, 1000000)


def _alphanumerics():
    letters_digits = string.ascii_letters + string.digits
    length = random.randint(5, 20)
    prefix_length = random.randint(0, 10)
    suffix_length = random.randint(0, 10)
    prefix = ''.join([' ' for i in range(prefix_length)])
    suffix = ''.join([' ' for i in range(suffix_length)])
    mystr = prefix + ''.join(random.choices(letters_digits, k=length)) + suffix
    return mystr


def generate_string(default_type='alphabetical'):
    default_type = default_type.strip()
    if default_type.__eq__('alphabetical'):
        return _alphabetical()
    if default_type.__eq__('real'):
        return _real()
    if default_type.__eq__('int'):
        return _integers()
    if default_type.__eq__('alphanumeric'):
        return _alphanumerics()
    raise Exception("Does not support type {}".format(default_type))


if __name__ == '__main__':
    print(generate_string())
    print(generate_string(default_type='real'))
    print(generate_string(default_type='int'))
    print(generate_string(default_type='alphanumeric'))
