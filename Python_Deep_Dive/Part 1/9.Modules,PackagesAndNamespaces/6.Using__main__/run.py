print('loading run.py: __name__ = {0}'.format(__name__))
import module1
import timing

if __name__ == '__main__':
    print('running run.py...')
    result = timing.timeit("print('hello')")
    print(result)