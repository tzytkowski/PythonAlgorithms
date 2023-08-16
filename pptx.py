class GymMembership:
  def __init__(self, num, gym_type):
    self.num = num
    self.gym_type = gym_type
    


  def DetermineRate(self, rate):
    self.rate = rate
    if self.gym_type == "bronze":
      self.rate = 25
    elif self.gym_type == "silver":
      self.rate= 35
    elif self.gym_type == "gold":
      self.rate = 50
    elif self.gym_type == "platinum":
      self.rate = 75
    return rate


  def DetermineTotal(self, total):
    self.total = total
    total = self.rate * self.num
   

  def ReturnTotal(total):
    return total



obj = GymMembership(5, "silver")
obj.DetermineRate()
obj.DetermineTotal()
obj.ReturnTotal()
print(obj.num, obj.gym_type)

