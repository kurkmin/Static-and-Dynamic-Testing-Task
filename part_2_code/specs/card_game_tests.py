import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.cardGame = CardGame()
        
    def test_can_check_for_ace(self):
        card = Card("spades", 1)
        self.assertEqual(True, self.cardGame.check_for_ace(card))
    
    def test_can_get_highest_card(self):
        card1 = Card("clubs", 2)
        card2 = Card("hearts", 3)
        self.assertEqual(card2, self.cardGame.highest_card(card1, card2))

    def test_can_get_cards_total(self):
        cards = [Card("clubs", 2), Card("hearts", 3)]
        self.assertEqual("You have a total of 5", self.cardGame.cards_total(cards))
