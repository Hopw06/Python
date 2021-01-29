print('Running module2.py')
import module1

def hello():
    print('module2 say Hello!\nand...')
    module1.hello()