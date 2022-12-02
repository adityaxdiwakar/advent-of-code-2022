# define some constants
ROCK = 1; PAPER = 2; SCISSOR = 3
LOSE = 1; DRAW = 2; WIN = 3

# define some conversions
convs = {"A": ROCK, "B": PAPER, "C": SCISSOR, "X": ROCK, "Y": PAPER, "Z": SCISSOR}
winners = {ROCK: PAPER, PAPER: SCISSOR, SCISSOR: ROCK}
losers = dict((v, k) for k,v in winners.items())
# define a winner function
def win(me, them): return me != them and them != winners[me]
def draw(me, them): return me == them

#open file, parse lines as integers
games = [(lambda g: (convs[g[0]], convs[g[1]]))(game.split(" "))
    for game in open("input.txt", "r").read().strip().split("\n")]

# part 1, sum up scores with XYZ being your hand
score = 0
for them, me in games:
    if win(me, them): score += 6
    if draw(me, them): score += 3
    score += me
print(score)

# part 2, sum up scores with XYZ being result
score = 0
for them, result in games:
    score += {
        DRAW: 3 + them, 
        WIN: 6 + winners[them], 
        LOSE: losers[them]
    }[result]
print(score)
