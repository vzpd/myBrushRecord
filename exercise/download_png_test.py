import os
import sys
import time
from concurrent import futures

import requests

POP20_CC = ['sprite copy ' + str(i) + '.png' for i in range(1, 21)]

BASE_URL = 'https:xxx.com'

DEST_DIR = 'download'

MAX_WORKERS = 20

if not os.path.exists(DEST_DIR):
    os.makedirs(DEST_DIR)


def getpng(name):
    url = '{}/{}'.format(BASE_URL, name)
    resp = requests.get(url)
    return resp.content


def savepng(png, filename):
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(png)


def show(text):
    print(text)
    sys.stdout.flush()


# 单线程下载
def download_many(cc_list):
    for pngname in POP20_CC:
        png = getpng(pngname)
        show(pngname)
        savepng(png, pngname)
    return len(cc_list)


def download_one(pngname):
    png = getpng(pngname)
    show(pngname)
    savepng(png, pngname)
    return pngname


def download_many_thread(cc_list):
    workers = min(MAX_WORKERS, len(cc_list))
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(download_one, cc_list)
    print(list(res))
    print(len(list(res)))
    print(res)

    return len(list(res))


def main(download_many):
    t0 = time.time()
    count = download_many(POP20_CC)
    elapsed = time.time() - t0
    msg = '\n{} flags downloaded in {:.2f}s'
    print(msg.format(count, elapsed))


if __name__ == '__main__':
    # main(download_many)
    main(download_many_thread)
