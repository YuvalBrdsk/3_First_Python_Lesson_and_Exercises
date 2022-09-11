from unittest import TestCase, mock
from unittest.mock import patch
from game_cards.Card import Card

class TestCard(TestCase):

    def setUp(self):
        """Function that works automatically before any test, and gives the variants for the test"""
        self.card = Card(5,3)
        print("setUp")

    def tearDown(self):
        """Function that runs automatically after any test and closes the test"""
        print("tearDown")

    #Test __init__ Card
    def test__init__valid(self):
        """Function that tests if the __init__ of Card worked in the setUp and the values and suits are valid"""
        self.assertEqual(self.card.card_value, 5)
        self.assertEqual(self.card.card_suit, 3)

    def test__init__valid_edge_value(self):
        """Function that tests if the __init__ of Card worked when the values are in the edge of validation"""
        card=Card(1,2)
        self.assertEqual(card.card_value, 1)
        card = Card(13, 3)
        self.assertEqual(card.card_value, 13)

    def test__init__valid_edge_suit(self):
        """Function that tests if the __init__ of Card worked when the suits are in the edge of validations"""
        card=Card(2,1)
        self.assertEqual(card.card_suit, 1)
        card = Card(12, 4)
        self.assertEqual(card.card_suit, 4)

    def test__init__invalid_values(self):
        """Function that tests if the program raise with value error when gets invalid card values"""
        with self.assertRaises(ValueError):
            card = Card(14, 2)
        with self.assertRaises(ValueError):
            card = Card(0, 2)
        with self.assertRaises(ValueError):
            card = Card(-13, 2)
        with self.assertRaises(ValueError):
            card = Card(100, 2)

    def test__init__invalid_suits(self):
        """Function that tests if the program raise with value error when gets invalid card suits"""
        with self.assertRaises(ValueError):
            card = Card(12, 5)
        with self.assertRaises(ValueError):
            card = Card(3, 0)
        with self.assertRaises(ValueError):
            card = Card(12, -4)
        with self.assertRaises(ValueError):
            card = Card(3, 100)

    def test__init__invalid_value_type(self):
        """Function that tests if the program raise with Type error when gets classes of card Value that are not of the integer class"""
        with self.assertRaises(TypeError):
            card = Card("13", 2)
        with self.assertRaises(TypeError):
            card = Card(1.5, 2)
        with self.assertRaises(TypeError):
            card = Card("?", 2)
        with self.assertRaises(TypeError):
            card = Card([1,2,3,4], 2)
        with self.assertRaises(TypeError):
            card = Card((1,2,3,4), 2)

    def test__init__invalid_suite_type(self):
        """Function that tests if the program raise with Type error when gets classes of card Suits that are not of the integer class"""
        with self.assertRaises(TypeError):
            card = Card(10, "2")
        with self.assertRaises(TypeError):
            card = Card(10, 2.2)
        with self.assertRaises(TypeError):
            card = Card(10, "<3")
        with self.assertRaises(TypeError):
            card = Card(10, {1:2, 3:4})
        with self.assertRaises(TypeError):
            card = Card(10, [2,2,3])

    #Test __gt__ Card
    def test__gt__valid(self):
        """Function that test the valid boolean responses to different cases of other card"""
        other=Card(2,2)
        self.assertTrue(self.card.__gt__(other))
        other = Card(10, 2)
        self.assertFalse(self.card.__gt__(other))
        other = Card(5, 2)
        self.assertFalse(self.card.__gt__(other))
        card= Card(1,3)
        other = Card(2, 2)
        self.assertTrue(self.card.__gt__(other))

    def test__gt__valid_other_same_as_card(self):
        """Function that tests that there indeed returns False if they are the same card"""
        other= Card(5,3)
        self.assertFalse(self.card.__gt__(other))

    def test__gt__invalid_values(self):
        """Function that tests that indeed the program will raise if the value of one of the cards is incourrect and __gt__ won't happen"""
        with self.assertRaises(ValueError):
            self.assertFalse(card=Card(14, 3).__gt__(other = Card(1, 3)))
        with self.assertRaises(ValueError):
            self.assertFalse(card=Card(12, 3).__gt__(other=Card(0, 3)))

    def test__gt__invalid_suits(self):
        """Function that tests that indeed the program will raise if the suit of one of the cards is incourrect and __gt__ won't happen"""
        with self.assertRaises(ValueError):
            self.assertFalse(card=Card(10, 5).__gt__(other = Card(10, 1)))
        with self.assertRaises(ValueError):
            self.assertFalse(card=Card(10, 4).__gt__(other = Card(10, 0)))

    def test__gt__invalid_other_type(self):
        """Function that test if the program raise with Type error when gets classes of other that are not of the Card class"""
        with self.assertRaises(TypeError):
            other = 2
            self.card.__gt__(other)
        with self.assertRaises(TypeError):
            other = "2"
            self.card.__gt__(other)
        with self.assertRaises(TypeError):
            other = [1, 2, 3, 4]
            self.card.__gt__(other)
        with self.assertRaises(TypeError):
            other = (1, 2, 3, 4)
            self.card.__gt__(other)
        with self.assertRaises(TypeError):
            other = {1:2, 3:4}
            self.card.__gt__(other)

    #Test __eq__ Card
    def test__eq__valid_true(self):
        """Function that tests return True when the cards are the same"""
        other= Card(5,3)
        self.assertTrue(self.card.__eq__(other))

    def test__eq__valid_false(self):
        """Function that test return False when the value of card and other are different"""
        other= Card(10,4)
        self.assertFalse(self.card.__eq__(other))
        other = Card(13, 2)
        self.assertFalse(self.card.__eq__(other))
        other = Card(8, 1)
        self.assertFalse(self.card.__eq__(other))

    def test__eq__valid_eq_suit(self):
        """Function that test return False when the value of card and other are different and the suit is the same"""
        other = Card(6, 3)
        self.assertFalse(self.card.__eq__(other))
        other = Card(10, 3)
        self.assertFalse(self.card.__eq__(other))

    def test__eq__invalid_values(self):
        """Function that tests that indeed the program will raise if the value of one of the cards is incourrect and __eq__ won't happen"""
        with self.assertRaises(ValueError):
            self.assertFalse(card=Card(14, 2).__eq__(other=Card(2, 2)))
        with self.assertRaises(ValueError):
            self.assertFalse(card=Card(12, 2).__eq__(other=Card(0, 2)))

    def test__eq__invalid_suits(self):
        """Function that tests that indeed the program will raise if the suit of one of the cards is incourrect and __eq__ won't happen"""
        with self.assertRaises(ValueError):
            self.assertFalse(card=Card(9, 5).__eq__(other=Card(8, 1)))
        with self.assertRaises(ValueError):
            self.assertFalse(card=Card(6, 4).__eq__(other=Card(7, 0)))

    def test__eq__invalid_other_type(self):
        """Function that tests the program raise with Type error when gets classes of other that are not of the Card class"""
        with self.assertRaises(TypeError):
            other = 2
            self.card.__eq__(other)
        with self.assertRaises(TypeError):
            other = "2"
            self.card.__eq__(other)
        with self.assertRaises(TypeError):
            other = [1, 2, 3, 4]
            self.card.__eq__(other)
        with self.assertRaises(TypeError):
            other = (1, 2, 3, 4)
            self.card.__eq__(other)
        with self.assertRaises(TypeError):
            other = {1: 2, 3: 4}
            self.card.__eq__(other)

    # Test suit_name-addition
    def test_suit_name_valid(self):
        """Function that tests that suit_name take the number of the suit of the card and change it to it's name"""
        self.assertEqual(self.card.suit_name(), "Heart")
        card= Card(5,1)
        self.assertEqual(card.suit_name(), "Diamond")
        card = Card(5, 2)
        self.assertEqual(card.suit_name(), "Spade")
        card = Card(5, 4)
        self.assertEqual(card.suit_name(), "Club")

    def test_suit_name_invalid_card_suit(self):
        """Function that test the program raise with Value error when gets card with an invalid suit"""
        with self.assertRaises(ValueError):
            card = Card(5, 5)
            card.suit_name()
        with self.assertRaises(ValueError):
            card = Card(5, 0)
            card.suit_name()
        with self.assertRaises(ValueError):
            card = Card(5, -1)
            card.suit_name()

    #Test value_name-addition
    def test_value_name_valid(self):
        """Function that tests that value_name takes the number of the value of the card and changes it to its name"""
        self.assertEqual(self.card.value_name(), "5")
        card= Card(1,3)
        self.assertEqual(card.value_name(), "Ace")
        card = Card(11, 3)
        self.assertEqual(card.value_name(), "Jack")
        card = Card(12, 3)
        self.assertEqual(card.value_name(), "Queen")
        card = Card(13, 3)
        self.assertEqual(card.value_name(), "King")

    def test_value_name_invalid_card_value(self):
        """Function that tests the program raise with Value error when gets a card with an invalid value"""
        with self.assertRaises(ValueError):
            card = Card(14, 3)
            card.suit_name()
        with self.assertRaises(ValueError):
            card = Card(0, 3)
            card.suit_name()
        with self.assertRaises(ValueError):
            card = Card(-1, 3)
            card.suit_name()