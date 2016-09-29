import random
text = "People don't know how great you are. People don't know how smart you are. These are the smart people. These are the smart people. These are really the smart people. And they never like to say it. But I say it. And I'm a smart person. These are the smart. We have the smartest people. We have the smartest people. And they know it. And some say it. But they hate to say it. But we have the smartest people."
#text = "Sadly, sadly there is no other way. The truth is our immigration system is worse than anybody ever realized. But the facts aren't known because the media won't report on them. The politicians won't talk about them and the special interests spend a lot of money trying to cover them up because they are making an absolute fortune. That's the way it is."


def shift(s):
    return random.randint(0, 5)*" " + s


def randsplit(s):
    if len(s) < 20:
        return s
    else:
        t = ""
        shifted_words = map(shift, s.split(" "))
        for i in range(0, len(shifted_words), 2):
            if (i/2 % 2):
                t += "\n".join(shifted_words[i:i+2])
                t += " "
            else:
                t += " ".join(shifted_words[i:i+2])
                t += " "
        return t

lines = text.split(". ")
lines = map(randsplit, lines)
lines = map(shift, lines)
text = "\n".join(lines)

print text.lower()
print len(text)
