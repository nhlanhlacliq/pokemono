class Trainer:
  def __init__(self, name, potions, pokemon_list, active = 0, active_pokemon = 0):
    self.name = name
    self.potions = potions
    self.pokemon_list = pokemon_list
    self.active = active
    self.active_pokemon = self.pokemon_list[active]
    print(f"Trainer {self.name} starts with {self.active_pokemon}!")
    print("=====================================================")
    print()

  def __repr__(self):
    return str(self.potions)

  def use_potion(self):
    if not self.active_pokemon.ko:

      if self.potions > 0:
        self.potions -= 1
        print(f"{self.name} used a potion!")
        self.active_pokemon.gain_health()
      else:
        print('You have no potions left.')

    else:
      if self.potions > 0:
        self.potions -= 1
        print(f"{self.name} used revive!")
        self.active_pokemon.revive()
      else:
        print('You have no potions left.')

  def attack(self, trainer):
    self.active_pokemon.attack(trainer.active_pokemon)

  def switch(self):
    self.active += 1
    self.active_pokemon = self.pokemon_list[self.active]
    print(f"{self.name} switched to {self.active_pokemon}")
    



class Pokemon(Trainer):
  def __init__(self, name, level, element, max_hp = 10, current_hp = 10, ko = False):
    self.name = name
    self.level = level
    self.element = element
    self.max_hp = level * 3
    self.current_hp = self.max_hp
    self.ko = ko

  def __repr__(self):
    return self.name # \nLevel: {self.level} \nHealth: {self.current_hp}/{self.max_hp} \nKnocked out: {self.ko}"  

  def knock_out(self):
    if self.ko:
      print(f"{self.name} has been knocked out!")

  def revive(self):
    if self.ko:
      print(f"{self.name} has been revived!")
      self.current_hp = self.level * 2
      print(f"{self.name} now has {self.current_hp} health points")
      self.ko = False
      print()
    if not self.ko:
      pass

  def lose_health(self, dmg):
    print(f"{self.name} is taking damage ({dmg})...")
    self.current_hp -= dmg
    if self.current_hp <= 0:
      self.current_hp = 0
      self.ko = True
      self.knock_out()
    else:
      print(f"{self.name} now has {self.current_hp} health points")
    print()

  def gain_health(self):
    if not self.ko:
      hp = self.level
      #print(f"{self.name} is gaining health ({hp})...")
      self.current_hp += hp
      if self.current_hp > self.max_hp:
        self.current_hp = self.max_hp
        print("Can't Heal above max health. LOL you lost a potion.")
      print(f"{self.name} now has {self.current_hp} health points")
      print()
    else:
      pass

  def attack(self, pokemon):
    if not self.ko:
      print(f"{self.name} attacks {pokemon}!")
      #Fire
      if self.element == "Fire" and pokemon.element == "Grass":
        dmg = self.level * 2
        print(f"({self.element} has an ADVANTAGE over {pokemon.element})")
      elif self.element == "Fire" and pokemon.element == "Water":
        dmg = self.level * 0.5
        print(f"({self.element} has an DISADVANTAGE over {pokemon.element})")
     

      #Grass
      elif self.element == "Grass" and pokemon.element == "Fire":
        dmg = self.level * 0.5
        print(f"({self.element} has an DISADVANTAGE over {pokemon.element})")
      elif self.element == "Grass" and pokemon.element == "Water":
        dmg = self.level * 2
        print(f"({self.element} has an ADVANTAGE over {pokemon.element})")

      #Water
      elif self.element == "Water" and pokemon.element == "Fire":
        dmg = self.level * 2
        print(f"({self.element} has an ADVANTAGE over {pokemon.element})")
      elif self.element == "Water" and pokemon.element == "Grass":
        dmg = self.level * 0.5
        print(f"({self.element} has an DISADVANTAGE over {pokemon.element})")

      #Neutral
      else:
        dmg = self.level
      pokemon.lose_health(dmg)
    else:
      pass 

# Gen 1
charmander = Pokemon("Charmander", 10, "Fire")
bulba = Pokemon("Bulbasaur", 10, "Grass")
squirtle = Pokemon("Squirtle", 10, "Water")
charizard = Pokemon("Charizard", 30, "Fire")
venusaur = Pokemon("Venusaur", 30, "Grass")
blastoise = Pokemon("Blastoise", 30, "Water")
# Gen 2
cyndaquil = Pokemon("Cyndaquil", 10, "Fire")
chikorita = Pokemon("Chikorita", 10, "Grass")
totodile = Pokemon("Totodile", 10, "Water")
typhlosion = Pokemon("Typhlosion", 30, "Fire")
meganium = Pokemon("Meganium", 30, "Grass")
feraligatr = Pokemon("Feraligatr", 30, "Water")

ash = Trainer("Ash", 2, [charmander, bulba, squirtle, charizard, venusaur, blastoise])
brock = Trainer("Brock", 2, [cyndaquil,chikorita,totodile,typhlosion,meganium,feraligatr])


ash.attack(brock)
ash.attack(brock)
ash.switch()
ash.use_potion()
ash.use_potion()
ash.use_potion()