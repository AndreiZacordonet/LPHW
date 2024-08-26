from sys import argv

script, user_name, age = argv
prompt = '~home/immabuckyou> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("Are you realy {}, {}?".format(age, user_name))
true_age = input(prompt)

print(f"""
{'LIAR!' if true_age != age else 'Good boy'}
Alright. so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
