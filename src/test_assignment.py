import unittest
from src.assignment import (random_num, get_length_of_string, get_sum_of_even_numbers_in_the_list, \
                            get_sum_of_odd_numbers_in_the_list, get_largest_number_in_the_list,
                            get_smallest_number_in_the_list, \
                            matching_strings, sum_third_score, set_num, sum_collection, remove_item, find_intersection,
                            union_of_set, \
                            sub_set_of_sets, remove_elements_in_first_set, minimum_and_maimum_elements_in_set,
                            set_length, sum_elements_at_odd_index, \
                            sum_elements_at_even_index, get_maximum_elements_in_a_set, get_minimum_elements_in_a_set)


class MyTestCase(unittest.TestCase):
    def test_that_my_list_has_num_1_50(self):
        self.assertEqual(random_num(), [16, 38, 35, 9, 24, 39, 31, 41, 38, 5])  # add assertion here

    def test_that_my_length_func_is_working(self):
        self.assertEqual(random_num(), [16, 38, 35, 9, 24, 39, 31, 41, 38, 5])
        self.assertEqual(get_length_of_string([16, 38, 35, 9, 24, 39, 31, 41, 38, 5]), 10)

    def test_function_is_addind_up_elements_at_even_index_in_the_list(self):
        self.assertEqual(random_num(), [16, 38, 35, 9, 24, 39, 31, 41, 38, 5])
        self.assertEqual(get_sum_of_even_numbers_in_the_list([16, 38, 35, 9, 24, 39, 31, 41, 38, 5]), 144)

    def test_function_is_addind_up_elements_at_odd_index_in_the_list(self):
        self.assertEqual(random_num(), [16, 38, 35, 9, 24, 39, 31, 41, 38, 5])
        self.assertEqual(get_sum_of_odd_numbers_in_the_list([16, 38, 35, 9, 24, 39, 31, 41, 38, 5]), 132)

    def test_function_is_returning_the_largest_in_the_list(self):
        self.assertEqual(random_num(), [16, 38, 35, 9, 24, 39, 31, 41, 38, 5])
        self.assertEqual(get_largest_number_in_the_list([16, 38, 35, 9, 24, 39, 31, 41, 38, 5]), 41)

    def test_function_is_returning_the_smallest_in_the_list(self):
        self.assertEqual(random_num(), [16, 38, 35, 9, 24, 39, 31, 41, 38, 5])
        self.assertEqual(get_smallest_number_in_the_list([16, 38, 35, 9, 24, 39, 31, 41, 38, 5]), 5)

    def test_matching_string(self):
        self.assertEqual(matching_strings(["abca", "1234", "1231", "bbbb", "23452", "nnww"]),
                         (4, ['abca', '1231', 'bbbb', '23452']))

    def test_sum_of_every_third_elements_in_list(self):
        self.assertEqual(sum_third_score([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), 45)

    def test_that_it_is_ten_elements_in_the_list(self):
        self.assertEqual(get_length_of_string([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 10)

    def test_that_function_returns_the_sum_of_set(self):
        self.assertEqual(set_num(), {1, 2, 3, 4, 5, 6, 7, 8, 9, 10})
        self.assertEqual(sum_collection({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}), 55)

    def test_that_function_returns_the_number_if_it_is_in_set(self):
        self.assertEqual(set_num(), {1, 2, 3, 4, 5, 6, 7, 8, 9, 10})
        self.assertEqual(remove_item({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 5), 5)

    def test_that_function_returns_the_none_if_it_is_not_in_set(self):
        self.assertEqual(remove_item({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 50), None)

    def test_that_function_returns_a_set_of_two_sets(self):
        number1 = list(range(1, 10))
        number2 = list(range(10, 20))
        sets1 = set(number1)
        sets2 = set(number2)
        self.assertEqual(find_intersection(sets1, sets2),
                         {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19})

    def test_that_function_returns_union_of_set(self):
        set1 = {2, 3, 4, 5, 6, 6}
        set2 = {8, 9, 1, 0, 11, 7}
        self.assertEqual(union_of_set(set2, set1), {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11})

    def test_that_function_returns_true_if_sets_are_subset(self):
        set1 = {1, 2, 3}
        set2 = {1, 2, 3, 4, 5}
        self.assertTrue(sub_set_of_sets(set1, set2))

    def test_that_function_returns_false_if_sets_are_not_subset(self):
        set1 = {2, 3, 4, 5, 6, 6}
        set2 = {8, 9, 1, 0, 11, 7}
        self.assertFalse(sub_set_of_sets(set1, set2))

    def test_that_function_can_clear_first_set(self):
        set1 = {2, 3, 4, 5, 6, 6}
        set2 = {8, 9, 1, 0, 11, 7}
        self.assertEqual(remove_elements_in_first_set(set1, set2), (set(), {0, 1, 7, 8, 9, 11}))

    def test_that_functions_returns_maximum_and_minimum_elements_in_the_set(self):
        set1 = {2, 3, 4, 5, 6, 6}
        self.assertEqual(minimum_and_maimum_elements_in_set(set1), (6, 2))

    def test_that_function_returns_length(self):
        set1 = {2, 3, 4, 5, 6}
        self.assertEqual(set_length(set1), 5)

    def test_that_if_we_have_duplicates_length_function_will_remove_duplicates(self):
        set1 = {2, 3, 4, 5, 6, 6, 2}
        self.assertEqual(set_length(set1), 5)

    def test_that_function_returns_sum_of_elements_at_odd_index(self):
        my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        self.assertEqual(sum_elements_at_odd_index(my_tuple), 25)

    def test_that_function_return_sum_of_elements_at_even_index(self):
        my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        self.assertEqual(sum_elements_at_even_index(my_tuple), 30)

    def test_that_function_returns_the_maximum_element_in_the_tuple(self):
        my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        self.assertEqual(get_maximum_elements_in_a_set(my_tuple), 10)

    def test_that_function_returns_the_minimum_element_in_the_tuple(self):
        my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        self.assertEqual(get_minimum_elements_in_a_set(my_tuple),1)


if __name__ == '__main__':
    unittest.main()
