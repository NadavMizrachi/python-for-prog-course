from multiprocessing import Pool, cpu_count

def inc(x):
    return x ** 2

if __name__ == "__main__":
    numbers = range(1, 10)
    my_pool = Pool(processes=cpu_count())
    outputs = my_pool.map(inc, numbers)
    print(outputs)