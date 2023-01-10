import math
time = list(map(int, input().split()))

time_in_min = time[0] * 60 + time[1]
time_out_min = time[2] * 60 + time[3]

duration = time_out_min - time_in_min

pay = 0

if (duration <= 15):
  pay = 0
elif (duration <= 3 * 60):
  pay = math.ceil(duration / 60) * 10
elif (duration <= 6 * 60):
  pay = math.ceil(duration / 60 - 3) * 20 + 30
elif (duration > 6 * 60):
  pay = 200

print(pay)
