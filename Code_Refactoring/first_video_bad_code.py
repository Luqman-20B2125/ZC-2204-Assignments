# Demonstrate the Creation Method replacement of Constructors
# Code Refactoring
class FootballPlayer:
	
    def __init__(self):
        self.passerRating = 0           # Specific to QBs
        self.rushingYards = 0           # Specific to RBs & QBs
        self.receivingYards = 0         # Specific to RBs & WRs
        self.totalTackles = 0           # Specific to DEF
        self.interceptions = 0          # Specific to DEF
        self.fieldGoals = 0             # Specific to Kickers
        self.avgPunt = 0.0              # Specific to Punters
        self.avgKickoffReturn = 0.0     # Specific to Special Teams
        self.avgPuntReturn = 0.0        # Specific to Special Teams

    @classmethod
    def FootballPlayer(cls, passerRating, rushingYards):
        cls.passerRating = passerRating
        cls.rushingYards = rushingYards

    @classmethod
    def FootballPlayer(cls, rushingYards):
        cls.rushingYards = rushingYards
	
	#Can't do this because the signature must be different
    
    @classmethod
    def FootballPlayer(cls, receivingYards):
        cls.receivingYards = receivingYards




# Demonstrate chain constructors
# Code Refactoring
class FootballPlayer2:
	
    def __init__(self):
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
	
	
	
	# Too much duplication in constructors
    @classmethod
    def FootballPlayer2(cls, playerName, college, fortyYardDash, sixtyYardDash):
        cls.playerName = playerName
        cls.college = college
        cls.fortyYardDash = fortyYardDash
        cls.sixtyYardDash = sixtyYardDash
    
    @classmethod
    def FootballPlayer2(cls, playerName, college, fortyYardDash, repsBenchPress):
        cls.playerName = playerName
        cls.college = college
        cls.fortyYardDash = fortyYardDash
        cls.repsBenchPress = repsBenchPress

    @classmethod
    def FootballPlayer2(cls, playerName, college, fortyYardDash, repsBenchPress, sixtyYardDash):
        cls.playerName = playerName
        cls.college = college
        cls.fortyYardDash = fortyYardDash
        cls.repsBenchPress = repsBenchPress
        cls.sixtyYardDash = sixtyYardDash
	
	