
'''my tinkering with REGEX & exact string matches to parse text files'''
import re

def matchTXT(file='charge.txt', regex=r'^.*(shot|shell).*$', flag=0):
    '''doc string'''
    try:
        re.compile(regex)
        is_valid = True
    except re.error:
        is_valid = False
        print("the provided regex r'{}' is not valid".format(regex))
        quit()

    try:
        with open(file, mode='r') as f:
            f_content = f.readlines()
    except:
        print('unable to open file: {}'.format(file))
        f_content = []

    result = []

    if flag == 0:
        for line in f_content:
            r = re.search(regex, line, re.I)
            if r:
                result.append(r.group())
        return result
    elif flag == 1:
        f_content = [line for line in f_content if 'Cannon' in line or 'Cossack' in line]
        result = f_content
        return result


if __name__ == '__main__':
    print(*matchTXT(regex=r'[', flag=0), sep='\n')
    print(*matchTXT(flag=1), sep=' ')