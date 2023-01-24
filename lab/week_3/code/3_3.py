def is_plusone_dictionary(dic):
  dic_arr = [value for item in dic.items() for value in item]
  return dic_arr == sorted(dic_arr) and dic_arr == list(range(min(dic_arr), max(dic_arr) + 1))
