import random

chars = 'qwertyuiopasdfghjkl;zxcvbnm,.1234567890'


def get_string(size=1024):
    string = [random.choice(chars) for _ in range(size)]
    return ''.join(string)


def file_faker(size=1024, fName='result', fType='docx'):
    """Parameters:
        size: the size of the document u want (KB).
        fName: the name of the document u want.
        fType: the type of the document u want, e.g. docx.
    Returns: None
    Results: generate a fake file.
    """
    with open(f'{fName}.{fType}', 'w') as fd:
        fd.write(get_string(1024 * size))


if __name__ == "__main__":
    file_faker()
