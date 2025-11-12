def ages(persons):
    result = {}
    for name in persons:
        born = persons[name]['born']
        died = persons[name]['died']
        age = died - born
        result[name] = age
    return result

persons = {
    'lenin': {'born': 1870, 'died': 1924},
    'mao': {'born': 1893, 'died': 1976},
    'gandhi': {'born': 1869, 'died': 1948},
    'hirohito': {'born': 1901, 'died': 1989},
}

print(ages(persons))
