#trò chơi giải mã từ viết tắt
print("welcome to my computer!")
playing = input("do you want play? ")
if playing != "yes":
    quit()
print("okay, let's play game")

score =0

anwser = input("what do you WAN stadn for? ")
if anwser == "wide area network": 
    print("correct")
    score += 1
else: 
    print("incorrect")

anwser = input("what do you LAN stadn for? ")
if anwser  == "local area network": 
    print("correct")
    score += 1
else: 
    print("incorrect")

anwser = input("what do you MAN stadn for? ")
if anwser  == "metropolitan area network": 
    print("correct")
    score += 1
else: 
    print("incorrect")

anwser = input("what do you WLAN stadn for? ")
if anwser  == "wireless local area network": 
    print("correct")
    score += 1
else: 
    print("incorrect")

print("you got",score,"questions correct")
