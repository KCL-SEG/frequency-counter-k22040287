# Frequencies code:
# This project creates a dictionary and counts elements in a list
# If an item in the list repeats, it is incremented in the dictionary.
# 

def frequencies(items):
    frequencies = {}
    for item in items:
        # catch items where the same item is stored as a string or int
        if isinstance(item, (int, float)):
            item = str(item)
        if item in frequencies.keys():
            frequencies[item] += 1
        else:
            frequencies[item] = 1
    return frequencies

if __name__ == '__main__':
    print(frequencies(['0', 4,4,'4','d','d','e',0,'a','d','4']))
