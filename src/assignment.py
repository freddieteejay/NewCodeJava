import random
numbers = []
for _ in range(10):
    numbers.append(random.randint(1,50))

print(f"The number in the list are: {numbers}")
def get_length_of_string(number):
    if type(number) in [int, float]:
     raise ValueError("Argument nust be interable")
    my_len = []
    for letters in number:
        my_len.append(1)
    return sum(my_len)
print(f"the length is : {get_length_of_string(numbers)}")

def get_sum_of_even_numbers_in_the_list(number):
    even_num = 0
    for count in range(0,len(number),2):
        even_num += number[count]
    return even_num

print(f"the sum of numbers at even index are: {get_sum_of_even_numbers_in_the_list(numbers)}")

def get_sum_of_odd_numbers_in_the_list(number):
    odd_sum = 0
    for count in range(1,len(number),2):
        odd_sum += number[count]
    return odd_sum

print(f"the sum of odd numbers in th list is: {get_sum_of_odd_numbers_in_the_list(numbers)}")

def get_largest_number_in_the_list(number):
    max_num = number[0]
    for count in range(get_length_of_string(number)):
        if number[count] > max_num:
            max_num = number[count]
    return max_num
print(f"the largest number in the list is: {get_largest_number_in_the_list(numbers)}")

def get_smallest_number_in_the_list(number):
    min_num = number[0]
    for count in range(get_length_of_string(number)):
        if number[count] < min_num:
            min_num = number[count]
    return min_num
print(f"the smallest number in the list is: {get_smallest_number_in_the_list(numbers)}")

my_list = {"abca", "1234", "1231", "bbbb", "23452", "nnww"}
def matching_strings(lists_of_string):
    counter = 0
    matching_string = []
    for string in lists_of_string:
        if get_length_of_string(lists_of_string) >= 2 and string[0] == string[-1]:
            counter += 1
            matching_string.append(string)
    print(f"there are {counter} strings which are the same and they are {matching_string}")
matching_strings(my_list)

list_of_int = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(f"the sequential list of numbers 1 to 15 are {list_of_int}")
duplicate_list = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15]
print(f"the duplicate list is {duplicate_list}")

my_list = list(set(duplicate_list))
print(f"the duplicate eliminated list is: {my_list}")

def sum_third_score(lst):
    return sum(lst[2::3])
print (f" the sum of the third scores is {sum_third_score(list_of_int)}")

def sum_first_middle_and_lats(number):
    if len(number) == 1:
        return number[0]
    elif len(number) == 2:
        return sum(number)
    else:
        middle_index = len(number)//2
        if len(number) % 2 == 0:
            middle_index = (number[middle_index - 1] + number[middle_index]) /2
        else:
            middle_index = number[middle_index]
            return number + middle_index + number[-1]

print(f"")

def set_num():
    num_list = set()
    while get_length_of_string(num_list) < 10:
        num = int(input("Enter a number: "))
        num_list.add(num)
    print("setted number: ", num_list)

set_num()
