from subprocess import Popen, PIPE
from contextlib import suppress
import os


try:
    pass
except:
    pass

def read(textfile):
    f_content = None
    with suppress(OSError), open('badfilename', mode='r') as f:
        f_content = [i for i in f]
    #with open(textfile, mode='r') as f:
        #f_content = [i for i in f]
    if f_content != None:
        return f_content
    else:
        f_content = ['failed']
        print('unable to read content from {}'.format(textfile))
        return f_content


def main(hosts):
    '''read in textfile & ping each entry'''
    for i in hosts:
        result = os.system("ping -c 1 " + i)
        if result == 0:
            print(i, " is alive")
        else:
            print(i, " is dead")

def cmd(command):
    run = Popen(args = command, stdout=None, shell=True)
    run.wait
    return run.poll()

    # 'echo to stdout; echo to stderr 1>&2; exit 1',

if __name__ == '__main__':
    main(read('hosts.txt'))
    #main(read(cmd('ping -c 1 8.8.8.8')))
    #print(cmd('ping -c 1 8.8.8.8'))