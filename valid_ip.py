def checkIP(inetv4):
    '''Args: ipv4 address to test, returns valid or not valid ip result'''
    host = inetv4.split('.')
    host = [int(b) for b in host]
    host = [b for b in host if b >=0 and b <= 255]
    return len(host) == 4, inetv4


if __name__ == '__main__':
    '''quick check of checkIP()'''
    check = checkIP('10.10.10.250')

    if check[0]:
        print('The addess {} is valid'.format(check[1]))
    else:
        print('The addess {} is not valid'.format(check[1]))