def to_dict(lst=None):
    if lst is None:
        lst = []
    if isinstance(lst, list):
        return {element: element for element in lst}


x = input('Enter something to list: ')
y = input('Enter something to list again: ')
t = input('Enter something to list and one more: ')
print(to_dict([x, y, t]))
