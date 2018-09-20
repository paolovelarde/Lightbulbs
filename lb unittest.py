import unittest
import ex8

ON = "I am on"
OFF = "I am off"


class TestEx8_LightSwitch(unittest.TestCase):
    """ Simple test case for the LightSwitch class. """

    def test_init_method_on(self):
        sw1 = ex8.LightSwitch("on")
        self.assertEqual(sw1.__str__(), ON, "Testing init with state = ON failed")

    def test_init_method_off(self):
        sw2 = ex8.LightSwitch("off")
        self.assertEqual(sw2.__str__(), OFF, "Testing init with state = OFF failed")

    def test_turn_on(self):
        sw = ex8.LightSwitch("off")
        sw.turn_on()
        self.assertEqual(sw.__str__(), ON, "Testing turn_on() failed")

    def test_turn_off(self):
        sw = ex8.LightSwitch("on")
        sw.turn_off()
        self.assertEqual(sw.__str__(), OFF, "Testing turn_off() failed")

    def test_flip_on_to_off(self):
        sw1 = ex8.LightSwitch("on")

        sw1.flip()
        self.assertEqual(sw1.__str__(), OFF, "Testing flip() on to off failed")
        sw1.flip()
        self.assertEqual(sw1.__str__(), ON, "Testing flip() back to on failed")

    def test_flip_off_to_on(self):
        sw2 = ex8.LightSwitch("off")

        sw2.flip()
        self.assertEqual(sw2.__str__(), ON, "Testing flip() off to on failed")
        sw2.flip()
        self.assertEqual(sw2.__str__(), OFF, "Testing flip() back to off failed")

    def test_illegal_operation_on(self):
        sw1 = ex8.LightSwitch("on")
        sw1.turn_on()
        self.assertEqual(sw1.__str__(), ON, 'Testing turn_on() with state = ON failed')

    def test_illegal_operation_off(self):
        sw2 = ex8.LightSwitch("off")
        sw2.turn_off()
        self.assertEqual(sw2.__str__(), OFF, 'Testing turn_off() with state = OFF failed')
        # self.assertRaises(ex8.InvalidSwitchException, sw1.turn_on)
        # self.assertRaises(ex8.InvalidSwitchException, sw2.turn_off)

    def test_no_print_function(self):
        self.assertFalse('print' in ex8.LightSwitch.__init__.__code__.co_names,
                         'print() function found in __init__()')
        self.assertFalse('print' in ex8.LightSwitch.__str__.__code__.co_names,
                         'print() function found in __str__()')
        self.assertFalse('print' in ex8.LightSwitch.turn_on.__code__.co_names,
                         'print() function found in turn_on()')
        self.assertFalse('print' in ex8.LightSwitch.turn_off.__code__.co_names,
                         'print() function found in turn_off()')
        self.assertFalse('print' in ex8.LightSwitch.flip.__code__.co_names,
                         'print() function found in flip()')


BOARD_MSG = 'The following switches are on: '


class TestEx8_SwitchBoard(unittest.TestCase):
    """ Simple test case for the SwitchBoard class. """

    def test_init_method(self):
        board = ex8.SwitchBoard(1)
        self.assertEqual(board.__str__().strip(), BOARD_MSG.strip(), 'Create SwitchBoard instance failed')

    def test_which_switch(self):
        board = ex8.SwitchBoard(10)
        self.assertEqual([], board.which_switch(), "Testing which_switch() and flip() methods failed, no flipped.")

        board.flip(0)
        self.assertEqual([0], board.which_switch(), "Testing which_switch() and flip() methods failed, flipped 0.")

        board.flip(8)
        self.assertEqual([0, 8], board.which_switch(), "Testing which_switch() and flip() methods, flipped 8.")

        board.flip(5)
        self.assertEqual([0, 5, 8], board.which_switch(), "Testing which_switch() and flip() methods, flipped 5.")

        board.flip(8)
        self.assertEqual([0, 5], board.which_switch(), "Testing which_switch() and flip() methods, flipped 8 again.")

    def test_str_method(self):
        board = ex8.SwitchBoard(10)
        self.assertEqual(BOARD_MSG.strip(), board.__str__().strip(), 'Test __str__ method failed')

    def test_flip_every(self):
        board = ex8.SwitchBoard(10)
        self.assertEqual([], board.which_switch(),
                         "Testing which_switch() and flip_every() methods failed, no flipped.")

        board.flip_every(2)
        self.assertEqual([0, 2, 4, 6, 8], board.which_switch(),
                         "Testing which_switch() and flip_every() methods failed, flipped every 2 switch.")
        board.flip_every(3)
        self.assertEqual([2, 3, 4, 8, 9], board.which_switch(),
                         "Testing which_switch() and flip_every() methods failed, flipped every 2 and 3 switch.")
        board.flip_every(5)
        self.assertEqual([0, 2, 3, 4, 5, 8, 9], board.which_switch(),
                         "Testing which_switch() and flip_every() methods failed, flipped every 2 and 3 and 5 switch")

    def test_reset(self):
        board = ex8.SwitchBoard(10)
        board.flip(0)
        board.flip(5)
        board.flip(8)
        self.assertEqual([0, 5, 8], board.which_switch(),
                         "Testing which_switch() and reset() methods failed, flipped 0, 5, 8 switch")

        board.reset()
        self.assertEqual([], board.which_switch(),
                         "Testing which_switch() and reset() methods failed, board not rested.")

    def test_no_print_function(self):
        self.assertFalse('print' in ex8.SwitchBoard.__init__.__code__.co_names,
                         'print() function found in __init__()')
        self.assertFalse('print' in ex8.SwitchBoard.__str__.__code__.co_names,
                         'print() function found in __str__()')
        self.assertFalse('print' in ex8.SwitchBoard.flip.__code__.co_names,
                         'print() function found in flip()')
        self.assertFalse('print' in ex8.SwitchBoard.flip_every.__code__.co_names,
                         'print() function found in flip_every()')
        self.assertFalse('print' in ex8.SwitchBoard.which_switch.__code__.co_names,
                         'print() function found in which_switch()')
        self.assertFalse('print' in ex8.SwitchBoard.reset.__code__.co_names,
                         'print() function found in reset()')


class TestEx8_Inheritance(unittest.TestCase):
    """ Simple test case for the LightSwitch class. """

    def test_light_switch(self):
        self.assertFalse(issubclass(ex8.LightSwitch, ex8.SwitchBoard),
                         "LightSwitch should not be a subclass of SwitchBoard")

    def test_switch_board(self):
        self.assertFalse(issubclass(ex8.SwitchBoard, ex8.LightSwitch),
                         "SwitchBoard should not be a subclass of LightSwitch")


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)