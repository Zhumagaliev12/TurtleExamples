import random
import randomcolor


# numbers = [1,2,3,4,5,6,7,8,9]
# num = []
# for i in range(6):
#     number = str(random.choice(numbers))
#     num += number
# num1 = int("".join(map(str, num)))
# col = "#"+str(num1)


# san = random.randint(1,9)

color = randomcolor.RandomColor()

print(color.generate())