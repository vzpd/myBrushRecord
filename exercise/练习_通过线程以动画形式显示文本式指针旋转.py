import threading
import itertools
import time
import sys


class Signal:
    go = True


def spin(msg, signal):
    write, flush = sys.stdout.write, sys.stdout.flush
    print('start')
    back = '\x08'
    for char in itertools.cycle('|/-\\'):
        # write(char + ' ' + msg)
        # flush()
        status = char + ' ' + msg
        print(char + ' ' + msg, end='')
        time.sleep(.25)
        # 使用退格符，把光标移动回来,使4个符号在同一行连续输出，以形成动画效果
        write(back * len(status))
        flush()
        if not signal.go:
            break


def supervisor():
    signal = Signal()
    spinner = threading.Thread(target=spin, args=('thinking...', signal))
    print('spinner object', spinner)
    spinner.start()
    time.sleep(3)
    signal.go = False
    spinner.join()
    return 42


def main():
    res = supervisor()
    print('Answer:', res)


if __name__ == '__main__':
    main()
