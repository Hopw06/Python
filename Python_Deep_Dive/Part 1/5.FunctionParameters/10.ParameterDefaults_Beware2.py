def add_item(name, quantity, unit, grocery_list):
    item_fmt = "{0} ({1} {2})".format(name, quantity, unit)
    grocery_list.append(item_fmt)

store_1 = []
store_2 = []

add_item('bananas', 2, 'units', store_1)
add_item('grapes', 1, 'bunch', store_1)
add_item('python', 1, 'medium-rare', store_2)

print(store_1)
print(store_2)

#work great
# in case user do not provide the store list, we have to return list from add_item function.
# Promblem is when we use default value for list

def add_item(name, quantity, unit, grocery_list = []):
    item_fmt = "{0} ({1} {2})".format(name, quantity, unit)
    grocery_list.append(item_fmt)
    return grocery_list

store_1 = add_item('bananas', 2, 'units')
store_1 = add_item('grapes', 1, 'bunch')

print(store_1)

store_2 = add_item('milk', 1, 'gallon')

print(store_2) # store_2 contain items in store_1
# BECAUSE WE USE SAME LIST FOR DEFAULT VALUE IN ADD_ITEM FUNCTIONS. 

# solution is set default value to none:

def add_item(name, quantity, unit, grocery_list = None):
    if grocery_list is None:
        grocery_list = []
    item_fmt = "{0} ({1} {2})".format(name, quantity, unit)
    grocery_list.append(item_fmt)
    return grocery_list

store_1 = add_item('bananas', 2, 'units')
add_item('grapes', 1, 'bunch', store_1)

print(store_1)

store_2 = add_item('milk', 1, 'gallon')

print(store_2)

# But this issue is sometimes useful:
# Used for memoization:

def factorial(n, cache = {}):
    if n < 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        print('calculating {0}!'.format(n))
        rs = n * factorial(n - 1)
        cache[n] = rs
        return rs

factorial(5)

factorial(10)

# Because we use same dictionary for default value, so the calculated value will be cached. (not to be re-calculate)
