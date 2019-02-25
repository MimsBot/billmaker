def print_bill(*items):
    subtotal = calculate_subtotal(items)
    tax = 0.13 * subtotal
    total = subtotal + tax

    print_header()

    for item in items:
        print_item(item)

    print_footer(subtotal, tax, total)


def calculate_subtotal(items):
    return len(items) * 2


def print_header():
    print('B is for BACON')
    print()
    print('----------------')


def print_item(item):
    print('2.00 {}'.format(item))


def print_footer(subtotal, tax):
    print('----------------')
    print('{:2f } SUBTOTAL'.format(subtotal))
    print('{:2f } TAX'.format(tax))
    print('-----------------')
    print('THIS IS WHERE THE TOTAL WILL GO')
    print()
    print('Please Come Again!')
    print()


print_bill('Bacon', 'Bacon', 'Veggie Bacon')
