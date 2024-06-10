import unittest
from src.length_func import MyStack


class Testlength(unittest.TestCase):
    # def test_get_length(self):
    #     self.assertEqual(get_length_of_string([1, 2, 3, 4, 45, 5, 5]), 7)
    #
    # def test_that_function_throws_exception(self):
    #     self.assertRaises(ValueError, get_length_of_string, 0)


    def test_add_to_stack(self):
        stack = MyStack()
        stack.add_to_stack("sem")
        stack.add_to_stack("colon")
        self.assertEqual(len(stack.stack),2)

    #def test_stack_returns_the_first(self):


    def test_add_to_queue(self):
        queue = MyStack()
        queue.add_to_queue("sem")
        queue.add_to_queue("colon")
        self.assertEqual(len(queue.queue),2)


    def test_my_queue_returns_the_last_one_i_put(self):
        queue = MyStack()
        queue.add_to_queue("semi")
        queue.add_to_queue("coolon")
        queue.add_to_queue("fareed")
        self.assertEqual(queue.get_item(0), "semi")
        self.assertEqual("fareed", queue.get_item(2))

    def test_that_the_stack_is_giving_correct_output(self):
        stack = MyStack()
        stack.add_to_stack("semi")
        stack.add_to_stack("colon")
        stack.add_to_stack("fareed")
        self.assertEqual("fareed",stack.get_item_in_stack(-1))

    def test_if_remove_element_from_the_stack_i_will_have_the_nextone(self):
        stack = MyStack()
        stack.add_to_stack("fareed")
        stack.add_to_stack("buchi")
        stack.add_to_stack("sk")
        stack.add_to_stack("deji")
        self.assertEqual("deji", stack.remove_item_in_a_stack(-1))
        self.assertEqual("sk",stack.get_item_in_stack(-1))


    def test_if_remove_element_from_the_queue_i_will_have_the_nextone(self):
        queue = MyStack()
        queue.add_to_queue("fareed")
        queue.add_to_queue("buchi")
        queue.add_to_queue("sk")
        queue.add_to_queue("deji")
        self.assertEqual("fareed", queue.remove_iten_in_a_queue(0))
        self.assertEqual("buchi", queue.get_item(0))

    # def test_that_function_throws_exception(self):
    #     stack = MyStack()
    #     stack.add_to_queue("fareed")
    #     self.assertRaises(ValueError, stack.get_item_in_stack("u"), "fareed")