# sorted list algorithm
def sorted_list(this_list):
    length = len(this_list)
    if (length < 1):
        return this_list
    else:
        extracted_item = this_list.pop()

    higher_lists = []
    lower_lists = []

    for i in this_list:
        if(i > extracted_item):
            higher_lists.append(i)
        else:
            lower_lists.append(i)

    return sorted_list(lower_lists) + [extracted_item] + sorted_list(higher_lists)

    

print(sorted_list([12, 43, 2, 9, 2, 4]))
