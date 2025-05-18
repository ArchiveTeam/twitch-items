import sys

import zstandard

ITEMS_PER_FILE = 5 * 10 ** 7


def main(start: int, stop: int):
    for i in range(start, stop, ITEMS_PER_FILE):
        local_stop = min(i+ITEMS_PER_FILE, stop)
        with zstandard.open('novideo_{}-{}.txt.zst'.format(i, local_stop-1), 'w') as f:
            for j in range(i, local_stop):
                f.write('novideo:'+str(j)+'\n')

if __name__ == '__main__':
    main(int(sys.argv[1]), int(sys.argv[2]))

