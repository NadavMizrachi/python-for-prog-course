import time
import multiprocessing


def sleepy_man(id):
    print(f'Process id {id} Starting to sleep...')
    time.sleep(1)
    print('Done sleeping')


if __name__ == "__main__":
    tic = time.time()
    p1 = multiprocessing.Process(target=sleepy_man, args=(1,))
    p2 = multiprocessing.Process(target=sleepy_man, args=(2,))
    p1.start()
    p2.start()

    # Wait for process p1 to finish it's job
    p1.join()

    # Wait for process p2 to finish it's job
    p2.join()
    toc = time.time()

    print(f'Done in {toc - tic} seconds')