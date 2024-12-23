def get_items():
    user_input = input("Enter a list of items separated by commas: ")
    
    item_list = user_input.split(',')
    
    item_tuple = tuple(item_list)
    
    return item_tuple

if __name__ == "__main__":
    result = get_items()
    print("The tuple you entered:", result)
