from fictional_names import name_generator

### General Names? ###
def generate_names(gender, style, library):
  name = name_generator.generate_name(gender=gender, style=style, library=True)
  return name

print(generate_names('male','orc',True))

