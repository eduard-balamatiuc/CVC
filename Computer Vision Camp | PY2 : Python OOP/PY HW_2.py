class Sigmartian:
   def __init__(self, name, SQL):
      self.name = name
      self.SQL = SQL
   def is_curious(self):
      return True
   def wants_to_learn(self):
      return True
   def knows_programming(self):
       print('Definately')

class Expert_Sigmartian(Sigmartian):
   def __init__(self, name, SQL):
      super().__init__(name, SQL)
   def knows_programming(self):
       print('A lot')
   def knows_statistics(self):
       return True

class Starter_Sigmartian(Sigmartian):
    def __init__(self, name, SQL):
        super().__init(name, SQL)
    def knows_programming(self):
        print('Maybe not yet')
    def knows_statistics(self):
        return True

