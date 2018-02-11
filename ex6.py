#interpolating an int into a string
types_of_people = 10
x = f"There are {types_of_people} types of people"

#interpolating a string into a string
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}"

#printing the interpolated strings
print(x)
print(y)

#printing the interpolated strings inside of an interpolated string
print(f"I said: {x}")
print(f"I also said: '{y}'")


hilarious = False
joke_eval = "Isn't that joke so funny!? {}"

#formatting a string
print(joke_eval.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side"

print(w+e)
print(350/6)