total_sum = 0
total_length = 0

def what_element(element):
    print(type(element))
    if isinstance(element, (int, float)):
        print(element)
        count_digits(element)
    elif isinstance(element, str):
        print(element)
        count_lens(element)
    elif isinstance(element, list):
        print(element)
        for item in element:
            what_element(item)
    elif isinstance(element, tuple):
        print(element)
        for item in element:
            what_element(item)
    elif isinstance(element, dict):
        print(element)
        for key, value in element.items():
            what_element(key)
            what_element(value)
    elif isinstance(element, set):
        for item in element:
            what_element(item)

def count_digits(digit):
    global total_sum
    print(digit)
    total_sum += digit

def count_lens(string):
    global total_length
    print(total_length)
    total_length += len(string)

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
what_element(data_structure)


print("Общая сумма:", total_sum + total_length)
