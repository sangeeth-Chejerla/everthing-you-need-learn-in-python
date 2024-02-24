def myenumerate(enum):
    for i in range(len(enum)):
        yield i, enum[i]

# Example usage of myenumerate
my_list = ['apple', 'banana', 'cherry']

for index, value in myenumerate(my_list):
    print(f"Index: {index}, Value: {value}")
