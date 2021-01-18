# This code is for Python assignment 007/2 (Covid-19), takes only "Yes" or "No" as inputs
age = input("Are you a cigarette addict older than 75 years old? ")
chronic = input("Do you have a severe chronic disease? ")
immune = input("Is your immune system too weak? ")
if age == 'No' and chronic == 'No' and immune == 'No':
    print("You are not in risky group")
else:
    print("You are in risky group")