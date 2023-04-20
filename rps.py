from random import randint

# defines rock paper scissors
# p1 = player 1
# p2 = player 2
# if p1 wins, return True
def rps(p1, p2):

    if (p1 == p2):
        print("TIE!!!")
        return False

    rock = "ROCK"
    paper = "PAPER"
    scissors = "SCISSORS"
    result = False
    
    p1 = p1.upper()
    p2 = p2.upper()

    print("player1: ", p1)
    print("player2: ", p2)

    if ((p1 == rock and p2 == scissors) 
    or (p1 == scissors and p2 == paper) 
    or (p1 == paper and p2 == rock)):
        result = True

    if (result):
        print(p1 + " beats " + p2)    
    else: print(p1 + " does not beat " + p2)
    return result


def playerGen():
    players = []
    for i in range(2):
        v = randint(1, 3)
        if (v == 1):
            v = "paper"
        if (v == 2):
            v = "rock"
        if (v == 3):
            v = "scissors"
        players.append(v)
    return players
        
players = playerGen()

print(rps(players[0], players[1]))