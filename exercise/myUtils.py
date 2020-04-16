import time


def count_time(func):
    def int_time(*args, **kwargs):
        start_time = time.time()  # 程序开始时间
        res = func(*args, **kwargs)
        over_time = time.time()  # 程序结束时间
        total_time = (over_time - start_time) * 1000
        print('程序%s运行用时%s毫秒' % (func.__name__, round(total_time, 3)))
        return res

    return int_time
