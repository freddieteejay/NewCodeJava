
    # def get_length_of_string(string):
        # if type(string) in [int, float]:
        #     raise ValueError("Argument nust be interable")
        # my_len = []
        # for letters in string:
        #     my_len.append(1)
        # return sum(my_len)
        # sum = 0
        # for _ in string:
        #     sum += 1
        # return sum

# tuple = (1, 2, 3, 4, "ojo",2, [])
# tuple[6].append(5)
# tuple[6].extend([6,3,4,"kent"])
# print(tuple)

class MyStack:
    def __init__(self):
        self.stack = []
        self.queue = []



    def add_to_stack(self,stack):
        return self.stack.append(stack)

    def add_to_queue(self,queue):
        return self.queue.append(queue)

    def get_item(self,i):
        return self.queue[i]

    def get_item_in_stack(self,i):
        if type(i) in [str, float]:
            raise ValueError("Not alllowed!")
        return self.stack[i]

    def remove_item_in_a_stack(self,i):
        return self.stack.pop(i)



    def remove_iten_in_a_queue(self,i):
        return self.queue.pop(i)




# def get_length_of_string(string):
#     if type(string) in [int, float]:
#         raise ValueError("Argument nust be interable")
#     my_len = []
#     for letters in string:
#         my_len.append(1)
#     return sum(my_len)
#
# get_length_of_string(12)

