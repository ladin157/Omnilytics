import os
from recognizer import is_integer, is_real, is_alphabetical, is_alphanumeric


def get_file_size(filename='strings.txt'):
    BYTE = 1
    KB = 1024 * BYTE
    MB = 1024 * KB
    size_in_bytes = os.path.getsize(filename)
    return size_in_bytes / MB


# def iterator_read(filename='strings.txt'):
#     if not os.path.exists(filename):
#         raise FileNotFoundError("File not found")
#     with open(filename, mode='r') as f:
#         for line in f:

def read_to_dict(filename='strings.txt'):
    if not os.path.exists(filename):
        raise FileNotFoundError("File not found")
    results = list()
    with open(filename) as f:
        text = f.readline()
        strs = text.split(', ')
        for s in strs:
            res = {}
            res['text'] = s.strip()
            if is_integer(s):
                res['des'] = 'integer'
            elif is_real(s):
                res['des'] = 'real numbers'
            elif is_alphabetical(s):
                res['des'] = 'alphabetical strings'
            elif is_alphanumeric(s):
                res['des'] = 'alphanumeric'
            else:
                continue
            results.append(res)
    return results


def write(filename='strings.txt', strs=list()):
    if not isinstance(strs, list):
        raise Exception("The params must be the list type")
    if len(strs) == 0:
        raise Exception("The list must contain at least one item")
    save_str = strs[0] + ''.join(', ' + strs[i] for i in range(1, len(strs)))
    with open(filename, mode='w') as f:
        f.write(save_str)


if __name__ == '__main__':
    # write(strs=list(['Hello', 'NoiNguyen', '   fsdfsdfd53454      ']))
    # results = read(filename='strings.txt')
    # for result in results:
    #     print(result['text'], ' - ', result['des'])
    file_size = get_file_size(filename='strings_10MB.txt')
    print(file_size)
