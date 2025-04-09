import gzip
import lzma
import sys

import zstandard


def main(filepath: str):
    norm_filepath = filepath
    open_func = {
        'gz': gzip.open,
        'xz': lzma.open
    }.get(filepath.rsplit('.', 1)[-1]) or open
    items = []
    with open_func(filepath, 'r') as f:
        indices = ['id', 'peril']
        for i, line in enumerate(f):
            if type(line) is bytes:
                line = str(line, 'utf8')
            line = line.split(',')
            if i == 0:
                indices = {
                    k: (line.index(k) if k in line else -1)
                    for k in indices
                }
                assert 'id' in indices
                continue
            video_id = line[indices['id']]
            video_peril = line[indices['peril']] if indices['peril'] >= 0 else 'y'
            if video_peril == 'y':
                items.append('video:' + video_id)
    with open(norm_filepath+'_items.txt', 'w') as f:
        f.write('\n'.join(items)+'\n')

if __name__ == '__main__':
    for filepath in sys.argv[1:]:
        main(filepath)

