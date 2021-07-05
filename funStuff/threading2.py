import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...for{seconds}'


# with concurrent.futures.ThreadPoolExecutor() as executer:
#     secs = [5, 4, 3, 2, 1]
#     results = [executer.submit(do_something, sec) for sec in secs]
#
#     for f in concurrent.futures.as_completed(results):
#         print(f.result())
with concurrent.futures.ThreadPoolExecutor() as executer:
    secs = [5, 4, 3, 2, 1]
    results = executer.map(do_something, secs)

    for result in results:
        print(result)



finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} second(s)')
