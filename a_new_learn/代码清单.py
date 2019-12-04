# Properly formatted price list based on specified width

width = int(input('Please enter width: '))

price_width = 10
item_width = width - price_width

header_fmt = "{{:{}}}{{:>{}}}".format(item_width, price_width)
fmt = "{{:{}}}{{:>{}.2f}}".format(item_width, price_width)

print('='* width)

print(header_fmt.format('Item', 'price'))

print('-'*width)

print(fmt.format('Apple',200))
print(fmt.format('Pears',300))
print(fmt.format('Cantalopes',2000))
print(fmt.format('Dried apricots(16 oz)',500))
print(fmt.format('Prunes(4 lbs)',3000))

print('=' * width)