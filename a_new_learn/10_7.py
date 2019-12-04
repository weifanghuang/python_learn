# print out the date specified by the number of years,months and days.

months = [
    'January',
    'February',
    'March',
    'April',
    'may',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]
# a list containing the endings corresponding to 1-31
endings = ['st', 'nd', 'rd'] + 17*['th']\
        + ['st', 'nd', 'rd'] + 7*['th']\
        + ['st']

Year = input('Years: ')
month = input('Month (1-12): ')
day = input('day(1-31): ')

month_number = int(month)
day_number = int(day)

month_name = months[month_number-1]
ordinal = day + endings[day_number-1]

print(month_name + ' ' + ordinal + ' ' + Year)

