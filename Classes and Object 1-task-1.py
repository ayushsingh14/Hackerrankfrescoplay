class Movie:
 def __init__(self, name,n,cost):  
  self.name = name
  self.n = n
  self.cost = cost
        
 def __str__(self):
  return 'Movie : {self.name}\nNumber of Tickets : {self.n}\nTotal Cost: {self.cost}'.format(self=self)    
