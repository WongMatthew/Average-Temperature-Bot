# Avg Temp Bot
# Matthew Wong
# 10/4/2020
# Finds the average of as many temperatures as desired

# Initialize variables
newtemperature = 0
Sum = 0

# Introduce Bot
print("Hello, I am a computing Bot, I can find the average temperature (Celsius) across 'x' number of days.")

# Only accept integer inputs, rejects string inputs
while True:
    try:
        days = int(input("How many days would you like me to calculate for? "))
        break
    except:
        print("Thats not a valid number of days")

# Ask for and add all the temperatures together, rejects string inputs --> Accumulator Process
for i in range(days):
  while True:
    try:
        temperature = float(input("Please input a temperature: "))
        newtemperature += temperature
        break
    except:
      print("Thats not a valid temperature")

# Get the average temperature
avgtemperature = newtemperature / days

# Give average temperature
print(str(avgtemperature) + "°C")

if avgtemperature >= 25:
  print("Wow thats hot")
elif 14 <= avgtemperature < 24:
  print("That's a good temperature")
elif avgtemperature < 14:
  print("Wow thats cold")