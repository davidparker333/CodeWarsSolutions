# The police have placed radars that will detect those vehicles that exceed the speed limit on that road. If the driver's speed
# is 10km/h to 19km/h above the speed limit, the fine will be 100 dollars, if it is exceeded by 20km/h to 29km/h the
# fine will be 250 dollars and if it is exceeded by more than 30km/h the fine will be 500 dollars.

# You will be provided with the speed limits of those roads with radar as a collection of speedlimits
# [90,100,110,120,....] and the speed of the driver will be the same on all roads and can never be
# negative and the amount of the fine will be accumulated example 95km/h.

# # Example (Speed=100, Signals=[110,100,80]-> 250)

def speed_limit(speed, signals):
  return sum([apply_fine(speed, x) for x in signals])

def apply_fine(speed, limit):
  fine = 0
  delta = speed - limit
  if delta >= 30:
    fine = 500
  elif delta >= 20:
    fine = 250
  elif delta >= 10:
    fine = 100
  return fine
