# Instead of having multiple constructors have functions that will have the same result as constructors
class FootballPlayer:
    def __init__(self, passerRating, rushingYards, receivingYards, totalTackles, 
                 interceptions, fieldGoals, avgPunt, avgKickoffReturn, avgPuntReturn):
        self.passerRating = passerRating            # Specific to QBs
        self.rushingYards = rushingYards            # Specific to RBs & QBs
        self.receivingYards = receivingYards        # Specific to RBs & WRs
        self.totalTackles = totalTackles            # Specific to DEF
        self.interceptions = interceptions          # Specific to DEF
        self.fieldGoals = fieldGoals                # Specific to Kickers
        self.avgPunt = avgPunt                      # Specific to Punters
        self.avgKickoffReturn = avgKickoffReturn    # Specific to Special Teams
        self.avgPuntReturn = avgPuntReturn          # Specific to Special Teams
	
    def getPasserRating(self):
        return self.passerRating
	
def createQB(passerRating, rushingYards):
    return FootballPlayer(passerRating, rushingYards, 0, 0, 0, 0, 0.0, 0.0, 0.0)
    
def createWR(rushingYards, receivingYards):
    return FootballPlayer(0, rushingYards, receivingYards, 0, 0, 0, 0.0, 0.0, 0.0)
        
def createKicker(fieldGoals, avgPunt):
    return FootballPlayer(0, 0, 0, 0, 0, fieldGoals, avgPunt, 0.0, 0.0)
	
aaronRodgers = createQB(108.0, 259)
calvinJohnson = createWR(11, 1964);
sebastianJanikowski = createKicker(31, 33.0);

print("Aaron Rodgers Passer Rating: ", aaronRodgers.getPasserRating())



# Create a general catch all constructor
class FootballPlayer2:
	
    def __init__(self, playerName, college, fortyYardDash, repsBenchPress, sixtyYardDash):
        self.playerName = playerName         
        self.college = college          
        self.fortyYardDash = fortyYardDash       
        self.repsBenchPress = repsBenchPress        
        self.sixtyYardDash = sixtyYardDash          
	
    def getPlayerName(self):
        return self.playerName

    def getCollege(self):
        return self.college

    def get40YdDash(self):
        return self.fortyYardDash

    def getRepsBenchPress(self):
        return self.repsBenchPress

    def get60YdDash(self):
        return self.sixtyYardDash	

    @classmethod
    def firstConstructor(cls, playerName, college, fortyYardDash, repsBenchPress):
        return FootballPlayer2(playerName, college, fortyYardDash, repsBenchPress, 0.0)
    
    @classmethod
    def secondConstructor(cls, playerName, college, fortyYardDash, sixtyYardDash):
        return FootballPlayer2(playerName, college, fortyYardDash, 0, sixtyYardDash)
		
jamellFleming = FootballPlayer2.secondConstructor("Jamell Fleming", "Oklahoma", 4.53, 10.75)
		
print(jamellFleming.getPlayerName())
print(jamellFleming.getCollege())
print(jamellFleming.get40YdDash())
print(jamellFleming.getRepsBenchPress())

