import concurrent.futures
import time

start = time.perf_counter()


def do_something():
    print(f'Sleeping  second(s)...')
    time.sleep(1)
    print('Done Sleeping...')

if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executer:
        executer.map(do_something())

    finish = time.perf_counter()

    print(f'Finished in {round(finish - start, 2)} second(s)')
