class Parking:

  def __init__(self):
    self.parking_capacity = 20
    self.occupied_spaces = 0

  def check_availability(self):
    if self.occupied_spaces <= self.parking_capacity:
      self.occupied_spaces += 1
      return True
    else:
      return False

  def leave_parking(self):
    self.occupied_spaces -= 1
    return True 