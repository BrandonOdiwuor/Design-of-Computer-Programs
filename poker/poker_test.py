from poker import *
import unittest

class TestPokerMethods(unittest.TestCase):
  SF = '6C 7C 8C 9C TC'.split()  # Straight Flush
  FK = '9D 9H 9S 9C 7D'.split()  # Four of a kind
  FH = 'TD TC TH 7C 7D'.split()  # Full House
  F = '7D 4D 6D 8D TD'.split()   # Flush
  S = '3C 4D 5C 6S 7H'.split()   # Straight
  SA = 'AD 2H 3C 4D 5C'.split()  # Straight with Ace as lowest card
  TK = '7D 7C 7H 5H 3D'.split()  # Three of a kind
  TP = '7D 7H 3C 3H 4D'.split()  # Two Pair
  OP = '2D 2H 5C 8D AH'.split()  # One Pair
  HC = '4D 3C 5D 9H TC'.split()  # High Card
  
  def test_card_ranks(self):
    self.assertEqual(card_ranks(['6C', '9H', 'TD', '7S', '8C']), [10, 9, 8, 7, 6])    
    self.assertEqual(card_ranks(['AC', '4S', '2H', '5S', '3C']), [5, 4, 3, 2, 1])

  def test_poker(self):
    t = TestPokerMethods

    self.assertEqual(poker([t.SF, t.FK, t.FH, t.F, t.S]), [t.SF])    #

    self.assertEqual(poker([t.S]), [t.S])                            # One Player 

    self.assertEqual(poker([t.FK, t.FK, t.FK]), [t.FK, t.FK, t.FK])  # Ties

  # 
  def test_straight(self):
    t = TestPokerMethods

    self.assertTrue(straight(card_ranks(t.S)))    
    self.assertFalse(straight(card_ranks(t.FK)))
    self.assertTrue(straight(card_ranks(t.SA)))

  def test_flush(self):
    t = TestPokerMethods

    self.assertTrue(flush(t.F))
    self.assertFalse(flush(t.S))

  def test_two_pair(self):
    t = TestPokerMethods

    self.assertEqual(two_pair(card_ranks(t.TP)), (7, 3))
    self.assertEqual(two_pair(card_ranks(t.OP)), None)


  def test_kind(self):
    t = TestPokerMethods

    # Four of a kind
    self.assertEqual(kind(4, card_ranks(t.FK)), 9)

    # Three of a kind
    self.assertEqual(kind(3, card_ranks(t.TK)), 7)

    self.assertEqual(kind(3, card_ranks(t.HC)), None)


    
  def test_hand_rank(self):
    t = TestPokerMethods

    self.assertEqual()



if __name__ == '__main__':
  unittest.main()