def is_leap(year):
  if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    return True
  else:
    return False


def day_of_year(day, month, year):
  day_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if is_leap(year):
    day_in_month[1] = 29
  return sum(day_in_month[:month-1]) + day


def day_in_year(year):
  if(is_leap(year)):
    return 366
  return 365


def check_day_in_month(day, month, year):
  days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

  if is_leap(year):
    days_of_month[1] = 29

  if day > days_of_month[month-1] or day < 1:
    return False

  return True


def date_diff(date_1, date_2):
  date_1 = list(map(int, date_1.split("-")))
  date_2 = list(map(int, date_2.split("-")))

  if (date_1[1] not in range(1, 13) or date_2[1] not in range(1, 13)):
    return -1

  if (not check_day_in_month(date_1[0], date_1[1], date_1[2]) or not check_day_in_month(date_2[0], date_2[1], date_2[2])):
    return -1

  diff_days = 0
  diff_days += 365 - day_of_year(date_1[0], date_1[1], date_1[2]) + 1

  for year in range(date_1[2]+1, date_2[2]):
    if is_leap(year):
      diff_days += 366
    else:
      diff_days += 365

  diff_days += day_of_year(date_2[0], date_2[1], date_2[2])

  return diff_days
