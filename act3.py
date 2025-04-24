class parrot :
    species="bird"
    def __init__(self,name,age) :
        self.name=name
        self.age=age

blu=parrot("bird",13)
woo=parrot("bird",12)

print(f"blu is {blu.age} years old")
print(f"woo is {woo.age} years old")

print(f"blu is a {blu.species}")
print(f"woo is a {woo.species}")