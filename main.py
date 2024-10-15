from fictional_names import name_generator

def slavic_names(number):
  if number != None:
    for num in number: 
      print(name_generator.generate_name(gender='male', style='slavic'))
  else:
    print("Skipped")

def viking_names(number):
  if number != None:  
    for num in number: 
      print(name_generator.generate_name(gender='male', style='viking'))
  else:
    print("Skipped")
  
def elf_names(number):
  if number != None:
    for num in number: 
      print(name_generator.generate_name(gender='male', style='elven', library=True))
  else:
    print("Skipped")

def orc_names(number):
  if number != None:
    for num in number: 
      print(name_generator.generate_name(gender='male', style='orc', library=True))
  else:
    print("Skipped")

def dwarf_names(number):
  if number != None:
    for num in number: 
      print(name_generator.generate_name(gender='male', style='dwarven', library=False))
  else:
    print("Skipped")

def generate_names(number, gender, style, library):
  for num in number: 
    print(name_generator.generate_name(gender=gender, style=style, library=True))
  else:
    print("Skipped")

print("")
print("How many slavic names do you want to generate?")
slavic_names(int(input()))
print("")
print("How many viking names do you want to generate?")
viking_names(int(input()))
print("")
print("How many elf names do you want to generate?")
elf_names(int(input()))
print("")
print("How many orc names do you want to generate?")
orc_names(int(input()))
print("")
print("How many dwarf names do you want to generate?")
dwarf_names(int(input()))