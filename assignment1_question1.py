'''
    Ronan Ballantine
    Python Assignment Q1
    01/03/2022
'''


def contains_letter(items, letter):
    items_containing_letter = 0
    for item in items:
        if letter in item:
            print(item)
            items_containing_letter += 1
        else:
            pass

    print(f'\nThe number of items in the list containing "{letter}" = {items_containing_letter}\n')

# End of contains_letter function


def item_length(items):
    for item in items:
        letter_count = len(item)
        print(f'{item} has {letter_count} letters')

# End of item_length function


def item_less_than(items, amount):
    less_than = []
    for item in items:

        if len(item) < amount:
            less_than.append(item)
        else:
            pass

    return less_than

# End of less_than function


def greater_or_equal(items, amount):
    i = 0
    list_length = len(items)
    print('\n')
    while i < (list_length - 1):

        name_length = len(items[i])
        if name_length >= amount:
            print(items[i][:(name_length - 1)])
        else:
            pass
        i += 1

# End of greater_or_equal function


def longest_and_shortest(items):
    longest_word = ''
    longest_words = []

    shortest_word = items[0]
    shortest_words = [items[0]]

    for item in items:

        if len(item) > len(longest_word):

            longest_word = item
            longest_words = [item]

        elif len(item) == len(longest_word):
            longest_words.append(item)

        else:
            pass

        if len(item) < len(shortest_word):
            shortest_word = item
            shortest_words.clear()
            shortest_words = [item]

        elif len(item) == len(shortest_word):
            if item != shortest_word:
                shortest_words.append(item)
            else:
                pass
        else:
            pass

    print(f'\nThe longest words are: {", ".join(longest_words)}')
    print(f'The shortest words are: {", ".join(shortest_words)}')

# End of longest_and_shortest function


gunners = ['ljungberg', 'pires', 'vieira', 'bergkamp', 'henri',
           'wright', 'adams', 'overmars', 'campbell', 'kanu', 'petit', 'cole', 'anelka']


contains_letter(gunners, 'e')

item_length(gunners)

newgunners = item_less_than(gunners, 6)
print(f'\n{newgunners}')

greater_or_equal(gunners, 8)

longest_and_shortest(gunners)
