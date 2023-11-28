import sys
from collections import Counter

class VoteInputError(Exception):
    pass

class Poll():
    """Initialize a poll. Make issecure = true to control the number of votes and the voters"""
    def __init__(self, issecure=False):
        pass
    
    def check_vote_type(self, vote_type):
        if vote_type is None:
            return None
        
        self.vote_type = self.vote_types[self.vote_type]

    def vote(self, votes):
        """Vote in your poll. Input possibilities for the votes include:
            \n{"Candidate": "Number of Votes"} A dictionary with key-value pairs of candidate, number of votes.
            \n{"Voter": "Candidate"}  A dictionary with key-value pairs of voter, candidate vote.
            \n["Candidate Vote"] A list of candidate votes.
            \nReturns a list of tuples of the candidate name, their votes and the percentage of votes.
            \n\n[("Candidate", "Number of Votes", "Percentage of votes)]"""
        self.votes = votes
        try:
            self.x = [False for x in self.votes.values() if isinstance(x, int)]
        except:
            self.x = False
        if self.x:
            try:
                self.result = sorted(self.votes.items())
                self.list_numbers = [x[1] for x in self.result]
                self.G = sum(self.list_numbers)
                
                self.percentages = [x / self.G * 100 for x in self.list_numbers]
                self.list_result = [list(tuple) for tuple in self.result]
                [self.list_result[x].insert(2, val) for x, val in enumerate(self.percentages)]
                self.result = [tuple(lst) for lst in self.list_result]
                return self.result
            except TypeError:
                raise VoteInputError("Invalid input type")
        elif isinstance(self.votes, dict):
            try:
                self.result = Counter(sorted(self.votes.values()))
                self.list_numbers = [x for x in self.result.values()]
                self.G = sum(self.list_numbers)
                
                self.percentages = [x / self.G * 100 for x in self.list_numbers]
                self.result = list(zip(self.result, self.list_numbers, self.percentages))
                return self.result
            except TypeError:
                raise VoteInputError("Invalid input type")
        else:
            try:
                self.result = Counter(self.votes)
                self.list_numbers = [x for x in self.result.values()]
                self.G = sum(self.list_numbers)
                
                self.percentages = [x / self.G * 100 for x in self.list_numbers]
                self.result = list(zip(self.result, self.list_numbers, self.percentages))
                return self.result
            except TypeError:
                raise VoteInputError("Invalid input type")

v = Poll()
dad = {"Trump": 10900000000000000, "asas": 12321321321321321}
print(v.vote(dad))
