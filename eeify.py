import random
text = "People don't know how great you are. People don't know how smart you are. These are the smart people. These are the smart people. These are really the smart people. And they never like to say it. But I say it. And I'm a smart person. These are the smart. We have the smartest people. We have the smartest people. And they know it. And some say it. But they hate to say it. But we have the smartest people."
def shift(s):
    return random.randint(0, 10)*" " + s
lines = text.split(". ")
lines = map(shift,lines)
text = "\n".join(lines)

print text.lower()
print len(text)
