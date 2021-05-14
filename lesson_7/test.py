# from time import time
import cProfile


def create_array():
    arr = []
    for i in range(0, 400000):
        arr.append(i)

def print_statement():
    print('Array created successully')

def main():
    create_array()
    print_statement()


# start = time()
#
# create_array()
# print_statement()
#
# end = time()
#
# print(f'Czas to {end - start} liczony w sekundach !')

if __name__ == '__main__':
    import cProfile, pstats
    profiler = cProfile.Profile()
    profiler.enable()
    main()
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('ncalls')
    stats.print_stats()
    stats.dump_stats('plik')