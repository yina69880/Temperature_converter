# quick component to convert degrees C to F
# Functions takes in value, does converion and puts answer into a list

def to_f(from_c):
    farenheit = (from_c *9/5) + 32
    return farenheit


# Main routine
temperatures = [0, 40, 100]
converted = []


for item in temperatures:
    answer = to_f(item)
    ans_statement = "{} degrees C {} degrees F".format(item, answer)
    converted.append(ans_statement)

print(converted)
