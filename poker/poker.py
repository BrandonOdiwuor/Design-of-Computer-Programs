def poker(hands):
  ''' Returns a list of winning hand: poker([hand,...]) => hand '''
  return allmax(hands, key=hand_rank)

def allmax(iterable, key=None):
  '''
  Returns a list equal to max in the iterable
  '''
  return [x for x in iterable if hand_rank(x) == hand_rank(max(iterable, key=key))]

def hand_rank(hand):
  '''
  Returns a value indicating the ranking of a hand
  '''
  ranks = card_ranks(hand)

  if straight(ranks) and flush(hand):                # Straight flush
    return (8, max(ranks))
  elif kind(4, ranks):                              # Four of a kind
    return (7, kind(4, ranks), kind(1, ranks))
  elif kind(3, ranks) and kind(2, ranks):           # Full house
    return (6, kind(3, ranks), kind(2, ranks))
  elif flush(hand):                                 # Flush
    return (5, ranks)
  elif straight(ranks):                              # Straight
    return (4, max(ranks))
  elif kind(3, ranks):                              # Three of kind
    return (3, kind(3, ranks), ranks)
  elif pair(2, ranks):                              # Two pair
    return (2, two_pair(ranks), ranks)
  elif pair(1, ranks):                              # One pair
    return (1, kind(2, ranks), ranks)
  else:                                             # High Card
    return (0, ranks)

def card_ranks(hand):
  '''
  Returns a list consisting of card ranks, sorted in descending order
  '''
  ranks = ['--23456789TJQKA'.index(r) for r,s in hand]
  ranks.sort(reverse=True)
  return [5, 4, 3, 2, 1] if ranks == [14, 5, 4, 3, 2] else ranks

def straight(ranks):
  '''
  Return a boolean indicating if the ordered ranks form a 5-card straight.
  '''
  lst = list(range(ranks[len(ranks) - 1], ranks[0]+1))
  lst.reverse()
  return ranks == lst

def flush(hand):
  '''
  Return a boolean indicating if all the cards have the same suit.
  '''
  suites = [s for r,s in hand]
  return len(set(suites)) == 1
    

def two_pair(ranks):
  '''
  Returns a turple in the form (highest, lowest) 
  if the ranks is a two pair; Otherwise None
  '''
  lst = [x for x in ranks if ranks.count(x) == 2]
  if len(lst) == 4:
    my_set = sorted(set(lst), reverse=True)
    return (my_set[0], my_set[1])
  else:
    return None

def kind(n, ranks):
  '''
  Return the first rank that this hand has exactly n of.
  Return None if there is no n-of-a-kind in the hand.
  '''
  for r in ranks:
    if ranks.count(r) == n: return r 
  return None


def test():
  '''Test cases for the functions in pocker program'''
  sf = '6C 7C 8C 9C TC'.split()
  fk = '9D 9H 9S 9C 7D'.split()
  fh = 'TD TC TH 7C 7D'.split()
  f = '1D 4D 6D 8D TD'.split()
  s = '1D 2H 3C 4D 5C'.split()
  tk = '7D 7C 7H 5H 1D'.split()
  tp = '7D 7H 3C 3H 1D'.split()
  op = '2D 2H 5C 8D AH'.split()
  hc = '1D 3C 5D 9H TC'.split()

  assert poker([sf, fk, fh]) == [sf]
  assert poker([fk, fh]) == [fk]
  assert poker([fh, fh]) == [fh] * 2 
  assert poker([fk]) == [fk]
  assert poker(30*[sf] + 60*[fk] + 10*[fh]) == [sf] * 30
  assert hand_rank(sf) == (8, 10)
  assert hand_rank(fk) == (7, 9, 7)
  assert hand_rank(fh) == (6, 10, 7)
  return 'test pass'

print test()
