usernames = []
scores = [] 
for x in range (0,5):
    username = input("Please enter your username")
    usernames.append(username)
    score = int(input("Please enter your test score"))
    while score > 100 or score < 0:
        print("Error, not a valid score")
        score = int(input("Please enter your score"))
    scores.append(score)
print(usernames)
print(scores)