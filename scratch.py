def main():
    # Define a dictionary with five arbitrary items
    my_dict = {'apple': 2, 'banana': 3, 'orange': 4, 'grape': 5, 'kiwi': 6}

    # Try to access a key that is not in the dictionary
    value = my_dict.get('mango')

    # Print the value
    print(value)

if __name__ == '__main__':
    main()
