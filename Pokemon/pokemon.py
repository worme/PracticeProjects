class Pokemon():
  """Represents an instance of a Pokemon."""
  def __init__(self, name, level, element_type, max_health, current_health, knocked_out):
    self.name = name
    self.level = level
    self.element_type = element_type
    self.max_health = max_health 
    self.current_health = current_health
    self.knocked_out = knocked_out

  def lose_health(self, amount):
    """Takes an amount as an argument and lowers a pokemon's current health by that number."""
    self.current_health -= amount
    print(f"{self.name} now has {self.current_health} hitpoints.")

  def gain_health(self, amount):
    """Takes an amount as an argument and raises a pokemon's current health by that number."""
    if self.current_health < self.max_health:
      self.current_health += amount
      if self.current_health > self.max_health:
        self.max_health = self.level * 10
      print(f"{self.name} now has {self.current_health} hitpoints.")

  def knock_out(self):
    """Determines if a pokemon has been knocked out by assessing if the pokemon's current health has fallen to 0 or below."""    
    self.knocked_out = True
    print(f"{self.name} has been knocked out.")

  def revive(self):
    """Changes the knocked out status of a pokemon to False."""
    self.knock_out = False
    print(f"{self.name} has been revived.")

  def attack(self, other_poke):
    """Takes a pokemon as an argument and determines the damage caused from one pokemon to the one passed. This is based on element types."""
    if self.knocked_out == False:
      if other_poke.current_health > 0:
        if self.element_type == "Fire":
          if other_poke.element_type == "Grass":
            print(f"{self.name} attacks {other_poke.name}. {other_poke.name} loses {self.level * 2} hitpoints.")
            other_poke.lose_health(self.level * 2)
          elif other_poke.element_type == "Water":
            print(f"{self.name} attacks {other_poke.name}. {other_poke.name} loses {self.level / 2} hitpoints.")
            other_poke.lose_health(self.level / 2)
          elif other_poke.element_type == "Fire":
            print(f"{self.name} attacks {other_poke.name}. {other_poke.name} loses {self.level} hitpoints.")
            other_poke.lose_health(self.level)

        if self.element_type == "Water":
          if other_poke.element_type == "Fire":
            print(f"{self.name} attacks {other_poke.name}. {other_poke.name} loses {self.level * 2} hitpoints.")
            other_poke.lose_health(self.level * 2)
          elif other_poke.element_type == "Grass":
            print(f"{self.name} attacks {other_poke.name}. {other_poke.name} loses {self.level / 2} hitpoints.")
            other_poke.lose_health(self.level / 2)
          elif other_poke.element_type == "Water":
            print(f"{self.name} attacks {other_poke.name}. {other_poke.name} loses {self.level} hitpoints.")
            other_poke.lose_health(self.level)

        if self.element_type == "Grass":
          if other_poke.element_type == "Water":
            print(f"{self.name} attacks {other_poke.name}. {other_poke.name} loses {self.level * 2} hitpoints.")
            other_poke.lose_health(self.level * 2)
          elif other_poke.element_type == "Fire":
            print(f"{self.name} attacks {other_poke.name}. {other_poke.name} loses {self.level / 2} hitpoints.")
            other_poke.lose_health(self.level / 2)
          elif other_poke.element_type == "Grass":
            print(f"{self.name} attacks {other_poke.name}. {other_poke.name} loses {self.level} hitpoints.")
            other_poke.lose_health(self.level)

      if other_poke.current_health <= 0:
        other_poke.knock_out()
    elif self.knocked_out == True:
      print(f"{self.name} is knocked out and cannot attack.")

class Trainer():
  """Represents a Trainer instance."""
  def __init__(self, name, poke_list, active_poke, potions):
    self.poke_list = poke_list
    self.name = name
    self.active_poke = active_poke
    self.potions = potions

  def use_potion(self):
    """Takes no arguments. Checks if a potion is in the potion list and then removes it."""
    heal_amount = 3
    if len(self.potions) == 0:
      print(f"{self.name} has no more potions.")
    elif len(self.potions) >= 1:
      print(f"{self.name} has used a healing potion on {self.active_poke.name}.")
      self.active_poke.gain_health(heal_amount)
      del self.potions[0]
      
  
  def attack_trainer(self, other_trainer):
    """Takes a trainer object as an argument and uses Pokemon class with attack method to attack the other trainer's active pokemon."""
    print(f"{self.name} is attcking {other_trainer.name}")
    self.active_poke.attack(other_trainer.active_poke)
  
  def switch_active_poke(self, poke):
    """Takes a pokemon object as an argument and sets it as the active pokemon."""
    if poke.knocked_out == False:
      self.active_poke = poke
      print(f"{self.name}'s active pokemon has been switched. Active pokemon is now {poke.name}.")
    elif poke.knocked_out == True:
      print(f"{self.name} tried to switch pokemon to {poke.name}.")
      print(f"Cannot switch pokemon because {poke.name} is knocked out.")
