#! /usr/bin/python
# Author - Sritanu Chakraborty
# Email - sritanu25@gmail.com
# Date - 21st Jan,2015

import unittest
from conway_game_of_life import generate_random_pattern
from conway_game_of_life import pattern_to_binary_converter, next_generation_pattern_generator
from conway_game_of_life import process_neighbours, count_neighbours


class TestGameofLife(unittest.TestCase):

    """
    The test class to unittest on various functions of conway_game_of_life.py with
    cols = 8,rows=4
    input_pattern_array = [['.','.','.','.','.','.','.','.'],['.','.','.','.','*','.','.','.'],
    ['.','.','.','*','*','.','.','.'],['.','.','.','.','.','.','.','.']]
    output_pattern_array = [['.','.','.','.','.','.','.','.'],['.','.','.','*','*','.','.','.'],
    ['.','.','.','*','*','.','.','.'],['.','.','.','.','.','.','.','.']]
    """

    def test_pattern_to_binary_converter(self):
        """
        This function tests whether the pattern_to_binary_converter function
        converts the pattern array to the right binary array.
        """
        pattern_array = [['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '*', '.', '.', '.'],
                         ['.', '.', '.', '*', '*', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.']]
        res = pattern_to_binary_converter(8, 4, pattern_array)
        output = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 0, 0, 0, 1, 0, 0, 'x'], ['x', 0, 0, 1, 1, 0, 0, 'x'],
                  ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
        self.assertItemsEqual(res, output)

    def test_next_generation_pattern_generator(self):
        """
        This function tests whether the next_generation_pattern_generator function
        generates the right next generation array from the binary array.
        """
        binary_array = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 0, 0, 0, 1, 0, 0, 'x'], ['x', 0, 0, 1, 1, 0, 0, 'x'],
                        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
        res = next_generation_pattern_generator(8, 4, binary_array, [])
        output = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0],
                  [0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]

        self.assertItemsEqual(res, output)

    def test_process_neighbours_one(self):
        """
        This function tests whether the right value is being processed in the (1,3) position of 
        the next_generation pattern.
        """

        binary_array = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 0, 0, 0, 1, 0, 0, 'x'], ['x', 0, 0, 1, 1, 0, 0, 'x'],
                        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
        res = process_neighbours(1, 3, binary_array)

        self.assertEqual(res, 1)

    def test_process_neighbours_two(self):
        """
        This function tests whether the right value is being processed in the (2,3) position of 
        the next_generation pattern.
        """

        binary_array = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 0, 0, 0, 1, 0, 0, 'x'], ['x', 0, 0, 1, 1, 0, 0, 'x'],
                        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
        res = process_neighbours(2, 3, binary_array)

        self.assertEqual(res, 1)

    def test_process_neighbours_three(self):
        """
        This function tests whether the right value is being processed in the (1,4) position of 
        the next_generation pattern.
        """

        binary_array = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 0, 0, 0, 1, 0, 0, 'x'], ['x', 0, 0, 1, 1, 0, 0, 'x'],
                        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
        res = process_neighbours(1, 4, binary_array)

        self.assertEqual(res, 1)

    def test_process_neighbours_four(self):
        """
        This function tests whether the right value is being processed in the (2,4) position of 
        the next_generation pattern.
        """

        binary_array = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 0, 0, 0, 1, 0, 0, 'x'], ['x', 0, 0, 1, 1, 0, 0, 'x'],
                        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
        res = process_neighbours(2, 4, binary_array)

        self.assertEqual(res, 1)

    def test_process_neighbours_five(self):
        """
        This function tests whether the right value is being processed in the (1,1) position of 
        the next_generation pattern.
        """

        binary_array = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 0, 0, 0, 1, 0, 0, 'x'], ['x', 0, 0, 1, 1, 0, 0, 'x'],
                        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
        res = process_neighbours(1, 1, binary_array)

        self.assertEqual(res, 0)

    def test_process_neighbours_six(self):
        """
        This function tests whether the right value is being processed in the (1,2) position of 
        the next_generation pattern.
        """

        binary_array = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 0, 0, 0, 1, 0, 0, 'x'], ['x', 0, 0, 1, 1, 0, 0, 'x'],
                        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
        res = process_neighbours(1, 2, binary_array)

        self.assertEqual(res, 0)

    def test_process_neighbours_seven(self):
        """
        This function tests whether the right value is being processed in the (1,5) position of 
        the next_generation pattern.
        """

        binary_array = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 0, 0, 0, 1, 0, 0, 'x'], ['x', 0, 0, 1, 1, 0, 0, 'x'],
                        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
        res = process_neighbours(1, 5, binary_array)

        self.assertEqual(res, 0)

    def test_process_neighbours_eight(self):
        """
        This function tests whether the right value is being processed in the (1,6) position of 
        the next_generation pattern.
        """

        binary_array = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 0, 0, 0, 1, 0, 0, 'x'], ['x', 0, 0, 1, 1, 0, 0, 'x'],
                        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
        res = process_neighbours(1, 6, binary_array)

        self.assertEqual(res, 0)

    def test_process_neighbours_nine(self):
        """
        This function tests whether the right value is being processed in the (2,1) position of 
        the next_generation pattern.
        """

        binary_array = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 0, 0, 0, 1, 0, 0, 'x'], ['x', 0, 0, 1, 1, 0, 0, 'x'],
                        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
        res = process_neighbours(2, 1, binary_array)

        self.assertEqual(res, 0)

    def test_process_neighbours_ten(self):
        """
        This function tests whether the right value is being processed in the (2,2) position of 
        the next_generation pattern.
        """

        binary_array = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 0, 0, 0, 1, 0, 0, 'x'], ['x', 0, 0, 1, 1, 0, 0, 'x'],
                        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
        res = process_neighbours(2, 2, binary_array)

        self.assertEqual(res, 0)

    def test_process_neighbours_eleven(self):
        """
        This function tests whether the right value is being processed in the (2,5) position of 
        the next_generation pattern.
        """

        binary_array = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 0, 0, 0, 1, 0, 0, 'x'], ['x', 0, 0, 1, 1, 0, 0, 'x'],
                        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
        res = process_neighbours(2, 5, binary_array)

        self.assertEqual(res, 0)

    def test_process_neighbours_twelve(self):
        """
        This function tests whether the right value is being processed in the (2,6) position of 
        the next_generation pattern.
        """

        binary_array = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 0, 0, 0, 1, 0, 0, 'x'], ['x', 0, 0, 1, 1, 0, 0, 'x'],
                        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
        res = process_neighbours(2, 6, binary_array)

        self.assertEqual(res, 0)

    def test_count_neighbours_one(self):
        """
        This function tests whether the right neighbour count value is being processed for the 
        (1,1) position of the current binary array.
        """

        binary_array = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 0, 0, 0, 1, 0, 0, 'x'], ['x', 0, 0, 1, 1, 0, 0, 'x'],
                        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
        res = count_neighbours(1, 1, binary_array)

        self.assertEqual(res, 0)

    def test_count_neighbours_two(self):
        """
        This function tests whether the right neighbour count value is being processed for the 
        (1,2) position of the current binary array.
        """

        binary_array = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 0, 0, 0, 1, 0, 0, 'x'], ['x', 0, 0, 1, 1, 0, 0, 'x'],
                        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
        res = count_neighbours(1, 2, binary_array)

        self.assertEqual(res, 1)

    def test_count_neighbours_three(self):
        """
        This function tests whether the right neighbour count value is being processed for the 
        (1,3) position of the current binary array.
        """

        binary_array = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 0, 0, 0, 1, 0, 0, 'x'], ['x', 0, 0, 1, 1, 0, 0, 'x'],
                        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
        res = count_neighbours(1, 3, binary_array)

        self.assertEqual(res, 3)

    def test_count_neighbours_four(self):
        """
        This function tests whether the right neighbour count value is being processed for the 
        (1,4) position of the current binary array.
        """

        binary_array = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 0, 0, 0, 1, 0, 0, 'x'], ['x', 0, 0, 1, 1, 0, 0, 'x'],
                        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
        res = count_neighbours(1, 4, binary_array)

        self.assertEqual(res, 2)

    def test_count_neighbours_five(self):
        """
        This function tests whether the right neighbour count value is being processed for the 
        (1,5) position of the current binary array.
        """

        binary_array = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 0, 0, 0, 1, 0, 0, 'x'], ['x', 0, 0, 1, 1, 0, 0, 'x'],
                        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
        res = count_neighbours(1, 5, binary_array)

        self.assertEqual(res, 2)

    def test_count_neighbours_six(self):
        """
        This function tests whether the right neighbour count value is being processed for the 
        (1,6) position of the current binary array.
        """

        binary_array = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 0, 0, 0, 1, 0, 0, 'x'], ['x', 0, 0, 1, 1, 0, 0, 'x'],
                        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
        res = count_neighbours(1, 6, binary_array)

        self.assertEqual(res, 0)

    def test_count_neighbours_seven(self):
        """
        This function tests whether the right neighbour count value is being processed for the 
        (2,1) position of the current binary array.
        """

        binary_array = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 0, 0, 0, 1, 0, 0, 'x'], ['x', 0, 0, 1, 1, 0, 0, 'x'],
                        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
        res = count_neighbours(2, 1, binary_array)

        self.assertEqual(res, 0)

    def test_count_neighbours_eight(self):
        """
        This function tests whether the right neighbour count value is being processed for the 
        (2,2) position of the current binary array.
        """

        binary_array = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 0, 0, 0, 1, 0, 0, 'x'], ['x', 0, 0, 1, 1, 0, 0, 'x'],
                        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
        res = count_neighbours(2, 2, binary_array)

        self.assertEqual(res, 1)

    def test_count_neighbours_nine(self):
        """
        This function tests whether the right neighbour count value is being processed for the 
        (2,3) position of the current binary array.
        """

        binary_array = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 0, 0, 0, 1, 0, 0, 'x'], ['x', 0, 0, 1, 1, 0, 0, 'x'],
                        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
        res = count_neighbours(2, 3, binary_array)

        self.assertEqual(res, 2)

    def test_count_neighbours_ten(self):
        """
        This function tests whether the right neighbour count value is being processed for the 
        (2,4) position of the current binary array.
        """

        binary_array = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 0, 0, 0, 1, 0, 0, 'x'], ['x', 0, 0, 1, 1, 0, 0, 'x'],
                        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
        res = count_neighbours(2, 4, binary_array)

        self.assertEqual(res, 2)

    def test_count_neighbours_eleven(self):
        """
        This function tests whether the right neighbour count value is being processed for the 
        (2,5) position of the current binary array.
        """

        binary_array = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 0, 0, 0, 1, 0, 0, 'x'], ['x', 0, 0, 1, 1, 0, 0, 'x'],
                        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
        res = count_neighbours(2, 5, binary_array)

        self.assertEqual(res, 2)

    def test_count_neighbours_twelve(self):
        """
        This function tests whether the right neighbour count value is being processed for the 
        (2,6) position of the current binary array.
        """

        binary_array = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 0, 0, 0, 1, 0, 0, 'x'], ['x', 0, 0, 1, 1, 0, 0, 'x'],
                        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
        res = count_neighbours(2, 6, binary_array)

        self.assertEqual(res, 0)

    def test_generate_random_pattern(self):
        """
        This function tests whether the generate_random_pattern function converts the 
        binary array to the right output pattern array.
        """

        pattern_array = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 0, 0, 1, 1, 0, 0, 'x'], ['x', 0, 0, 1, 1, 0, 0, 'x'],
                         ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]

        res = generate_random_pattern(8, 4, pattern_array)

        output = [['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '*', '*', '.', '.', '.'],
                  ['.', '.', '.', '*', '*', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.']]

        self.assertItemsEqual(res, output)


if __name__ == '__main__':
    unittest.main()
