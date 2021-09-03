name = 'Keith S. Taylor'
age = 35 #defo a lie
height = 192 #cm
weight = 84 #kg
eyes = 'brown'
teeth = 'white' #ish
hair = 'brown'

print(f"Let's talk about {name}.")
print(f"He's {height} cm tall.")
print(f"He weighs in at {weight} kg.")
print("Actually that's not too heavy.")
imp_height = round((height / 2.54), 1)
imp_weight = round((weight / 0.4535), 1)
print(f"In imperial that works out at {imp_height} inches tall and {imp_weight} llbs.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on how much red wine he's had.")

total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
