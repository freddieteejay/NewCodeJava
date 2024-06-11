import random


def random_num():
    random.seed(3)
    numbers = []
    for i in range(10):
        random_number = random.randint(1, 50)
        numbers.append(random_number)
    return numbers


print(random_num())

ran = random_num()


def get_length_of_string(ran):
    if type(ran) in [int, float]:
        raise ValueError("Argument nust be interable")
    my_len = []
    for letters in ran:
        my_len.append(1)
    return sum(my_len)


print(f"the length is : {get_length_of_string(ran)}")


def get_sum_of_even_numbers_in_the_list(number):
    even_num = 0
    for count in range(0, len(number), 2):
        even_num += number[count]
    return even_num


print(f"the sum of numbers at even index are: {get_sum_of_even_numbers_in_the_list(ran)}")


def get_sum_of_odd_numbers_in_the_list(number):
    odd_sum = 0
    for count in range(1, len(number), 2):
        odd_sum += number[count]
    return odd_sum


print(f"the sum of odd numbers in th list is: {get_sum_of_odd_numbers_in_the_list(ran)}")


def get_largest_number_in_the_list(number):
    max_num = number[0]
    for count in range(get_length_of_string(number)):
        if number[count] > max_num:
            max_num = number[count]
    return max_num


print(f"the largest number in the list is: {get_largest_number_in_the_list(ran)}")


def get_smallest_number_in_the_list(number):
    min_num = number[0]
    for count in range(get_length_of_string(number)):
        if number[count] < min_num:
            min_num = number[count]
    return min_num


print(f"the smallest number in the list is: {get_smallest_number_in_the_list(ran)}")

my_list = {"abca", "1234", "1231", "bbbb", "23452", "nnww"}


def matching_strings(lists_of_string):
    counter = 0
    matching_string = []
    for string in lists_of_string:
        if get_length_of_string(lists_of_string) >= 2 and string[0] == string[-1]:
            counter += 1
            matching_string.append(string)
    return counter, matching_string


print(matching_strings(my_list))

list_of_int = []
for count in range(1, 16):
    list_of_int.append(count)
print(f"the sequential list of numbers 1 to 15 are {list_of_int}")

duplicate_list = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]
print(f"the duplicate list is {duplicate_list}")

my_list = list(set(duplicate_list))
print(f"the duplicate eliminated list is: {my_list}")


def sum_third_score(lst):
    return sum(lst[2::3])


print(f" the sum of the third scores is {sum_third_score(list_of_int)}")


# def sum_first_middle_and_lats(number):
#     if len(number) == 1:
#         return number[0]
#     elif len(number) == 2:
#         return number[0] + number[1]
#     else:
#         middle_index = len(number) // 2
#         if len(number) % 2 == 0:
#             middle_index = (number[middle_index - 1] + number[middle_index]) / 2
#         else:
#             middle_index = number[middle_index]
#             return number + middle_index + number[-1]
#
#
# print(f"")


def set_num():
    num_list = set()
    # while get_length_of_string(num_list) < 10:
    #     num = int(input("Enter a number: "))
    for num in range(1, 11):
        num_list.add(num)
    return num_list


#
x = set_num()


#
#
def sum_collection(x):
    add_collect = 0
    for num in x:
        add_collect += num
    return add_collect


print(f"the sum of set is{sum_collection(x)}")


def remove_item(sets, num):
    if num in sets:
        sets.remove(num)
        return num
    else:
        return None


print(remove_item(x, 56))

number1 = list(range(1, 10))
number2 = list(range(10, 20))
sets1 = {2,3,4,5,6}
sets2 = {2,3,5,6,7,8}


def find_intersection(set1, sets2):
    combined_set = set1 | sets2
    return combined_set


print(find_intersection(sets1, sets2))


def union_of_set(sets1,sets2):
    return sets1 | sets2
print(union_of_set(sets1,sets2))

def sub_set_of_sets(sets1, sets2):
    return sets1 <= sets2

print(sub_set_of_sets(sets1,sets2))


def remove_elements_in_first_set(set1, set2):
    set1 = set()
    return set1,set2

print(remove_elements_in_first_set(sets1,sets2))

def minimum_and_maimum_elements_in_set(set1):
    maximum = None
    minimum = None
    for num in set1:
        if maximum is None or num > maximum:
            maximum = num
        if minimum is None or num < minimum:
            minimum = num

    return maximum, minimum


def set_length(set1):
    count = 0
    for elements in set1:
        count += 1
    return count
print(set_length(sets1))


def add_numbers_into_tuple():
    my_tuple = tuple(range(1,21))
    return my_tuple
print(add_numbers_into_tuple())

reuseable_tuple = add_numbers_into_tuple()

def sum_elements_at_odd_index(my_tuple):
    sum_odd = ()
    alist = []
    my_list = list(my_tuple)
    for count in range(len(my_list)):
        if count % 2 == 0:
            alist.append(my_list[count])
    new_tuple = tuple(alist)
    summed_tuple = sum(new_tuple)
    return summed_tuple
print(sum_elements_at_odd_index(reuseable_tuple))


def sum_elements_at_even_index(my_tuple):
    sum_odd = ()
    alist = []
    my_list = list(my_tuple)
    for count in range(len(my_list)):
        if count % 2 != 0:
            alist.append(my_list[count])
    new_tuple = tuple(alist)
    summed_tuple = sum(new_tuple)
    return summed_tuple
print(sum_elements_at_even_index(reuseable_tuple))

def get_maximum_elements_in_a_set(my_tuple):
    my_list = list(my_tuple)
    max = my_list[0]
    for count in range(len(my_list)):
        if my_list[count] > max:
            max = my_list[count]

    return max
print(get_maximum_elements_in_a_set(reuseable_tuple))


def get_minimum_elements_in_a_set(my_tuple):
    my_list = list(my_tuple)
    min = my_list[0]
    for count in range(len(my_list)):
        if my_list[count] < min:
            min = my_list[count]
    return min

print(get_minimum_elements_in_a_set(reuseable_tuple))

maximum = get_maximum_elements_in_a_set(reuseable_tuple)
minimum = get_minimum_elements_in_a_set(reuseable_tuple)

def sum_up_elements_in_tuples(my_tuple1, my_tuple2):
    my_list = []
    sum = my_tuple1 + my_tuple2
    my_list.append(sum)
    new_tuple = tuple(my_list)
    return new_tuple

print(sum_up_elements_in_tuples(maximum,minimum))

