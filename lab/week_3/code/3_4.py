def char_count(string):
  return dict((c, string.count(c)) for c in set(string))