from fictional_names import name_generator

def slavic_names():
  print("Slavic:")
  print(name_generator.generate_name(style='slavic'))

def viking_names():
  print("Viking:")
  print(name_generator.generate_name(style='viking'))

def elf_names():
  print("Elf:")
  print(name_generator.generate_name(style='elven', library=True))

def orc_names():
  print("Orc:")
  print(name_generator.generate_name(style='orc', library=True))

def dwarf_names():
  print("Dwarf:")
  print(name_generator.generate_name(gender='male', style='dwarven', library=False))

print("")
slavic_names()
print("")
viking_names()
print("")
elf_names()
print("")
orc_names()
print("")
dwarf_names()