day_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
  if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    return True
  else:
    return False


def day_of_year(day, month, year):
  if is_leap(year):
    day_in_month[1] = 29
  return sum(day_in_month[:month-1]) + day
