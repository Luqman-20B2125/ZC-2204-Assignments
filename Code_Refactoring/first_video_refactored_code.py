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
        self.playerName = ""           
        self.college = ""           
        self.fortyYardDash = 0.0        
        self.repsBenchPress = 0        
        self.sixtyYardDash = 0.0          
	
    def getPlayerNameI(self):
        return self.playerName

    def getCollege(self):
        return self.college

    def get40YdDash(self):
        return self.fortyYardDash

    def getRepsBenchPress(self):
        return self.repsBenchPress

    def get60YdDash(self):
        return self.sixtyYardDash	
	

"""
	public FootballPlayer2(String playerName, String college, 
			double fortyYardDash, int repsBenchPress){
		
		this(playerName, college, fortyYardDash, repsBenchPress, 0.0);
		
	}
	
	public FootballPlayer2(String playerName, String college, 
			double fortyYardDash, double sixtyYardDash){
		
		this(playerName, college, fortyYardDash, 0, sixtyYardDash);
		
	}
	
	def void main(String[] args){
		
		FootballPlayer2 jamellFleming = new FootballPlayer2("Jamell Fleming", "Oklahoma", 4.53, 10.75)
		
		System.out.println(jamellFleming.getPlayerName())
		System.out.println(jamellFleming.getCollege())
		System.out.println(jamellFleming.get40YdDash())
		System.out.println(jamellFleming.getRepsBenchPress())
		System.out.println(jamellFleming.get60YdDash())
"""
