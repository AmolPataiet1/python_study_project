class Threadingmethods:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def test(self):
    return f"{self.name}({self.age})"