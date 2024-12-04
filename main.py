from fictional_names import name_generator

def slavic_names(number):
  if number != 0:
    for num in number: 
      names = name_generator.generate_name(gender='male', style='slavic')

def viking_names(number):
  if number != 0:  
    for num in number: 
      names = name_generator.generate_name(gender='male', style='viking')

### Fantasy Names? ###

def elf_names(number):
  if number != 0:
    for num in number: 
      names = name_generator.generate_name(gender='male', style='elven', library=True)

def orc_names(number):
  if number != 0:
    for num in number: 
      names = name_generator.generate_name(gender='male', style='orc', library=True)

def dwarf_names(number):
  if number != 0:
    for num in number: 
      names = name_generator.generate_name(gender='male', style='dwarven', library=False)

### General Names? ###
def generate_names(number, gender, style, library):
  for num in number: 
    names = name_generator.generate_name(gender=gender, style=style, library=True)

