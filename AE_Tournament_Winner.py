# Input
# Matches [Home, Away]
[
  ["HTML", "C#"],
  ["C#", "Python"],
  ["Python", "HTML"]
]
# Results [0 - Away Win, 1 - Home Win] 
# 1 win = 3 pts, Loss = 0 pts
[0, 0, 1]

# Expected Output
# Find Tournament Winner
["Python"] 

# Approach 1
def tournamentWinner(competitions, results):
    # Write your code here.
    d = {}
    # Iterating through the matches
    for i in range(0,len(competitions)):
        # Iterating through the results
        # If result is 0 -> Away team gets 3 points
        if results[i] == 0:
            # If already team present add 3 more points
            if competitions[i][1] in d:
                d[competitions[i][1]]+=3  
            else:
                d[competitions[i][1]] = 3
            print(d)
        # If result is 1 -> Home team gets 3 points
        elif results[i] == 1:
            # # If already team present add 3 more points
            if competitions[i][0] in d:
                d[competitions[i][0]]+=3   
            else:
                d[competitions[i][0]] = 3
            print(d)
    #print(d)
    return max(d, key = d.get)
    

