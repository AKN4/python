import random
def generate_name():
    first_names=["Ahmet","Melih","Mehmet","Abdullah","John","Jakoob","Meltem"]
    last_names=["Smith","Akın","Yılmaz","Kara","Bulut","Daum","Gül"]
    return ("{} {}".format(random.choice(first_names),random.choice(last_names)))

for i in range(5):
    print(generate_name())