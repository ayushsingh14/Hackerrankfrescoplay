class Movie:
 def __init__(self, name,n,cost):  
  self.name = name
  self.n = n
  self.cost = cost
 
 def __str__(self):
          string = """Movie : {}
Number of Tickets : {}
Total Cost : {}""".format(self.name, self.n, self.cost)
          return string
  
