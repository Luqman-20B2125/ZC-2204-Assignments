class FootballPlayer40YardDashInfo:

    def __init__(self):
        self.players = []

    def addFootballPlayer(self, player):
        self.players.add(player)

	# This method is the focus of the extract method tutorial

    def printPlayerInfo(self):

        avg40YdTime = 0.0

		# Extracted Prints the titles

        self.printTitles()

        # Original Print titles

        """
		print("%-15s %15s", "Name", "Avg 40 Time\n")

		# Print dashes under titles

		for i in range(30)
            print(*"_")

		print()
		"""

        self.printPlayersWith40Avg()

        """ Originally Cycled through all the players

		for(FootballPlayer player : players){

			print("%-19s", player.getName())

			double total40YdDashTimes = 0.0

			double[] fortyYardDashTimes = player.get40YardDashTimes()

			for(int i = 0 i < len(player.get40YardDashTimes()) i++){

				total40YdDashTimes += fortyYardDashTimes[i]

			}

			avg40YdTime = total40YdDashTimes / len(player.get40YardDashTimes())

			print("%1$.2f", avg40YdTime)

			print()

		} """

    def printTitles(self):
        print("Name".ljust(15," "), "Avg 40 Time")
        self.printChars('_', 30)

    def printChars(self,charToPrint, howManyTimes):
        for i in range(howManyTimes):
            print(charToPrint, end = "")

        print()

    def printPlayersWith40Avg(self):

        for player in self.players:

            print("%-19s", player.getName())

            total40YdDashTimes = 0.0

            fortyYardDashTimes = player.get40YardDashTimes()

            for player40YardDashTime in fortyYardDashTimes:
                total40YdDashTimes += player40YardDashTime

            avg40YdTime = total40YdDashTimes / len(fortyYardDashTimes)

            print("%1$.2f", avg40YdTime)

			# If the code is as clear as a method name use the code instead
			# Remove the method call here
            
			# String inTop15 = checkIfInTop15(avg40YdTime) ? " *Top 15\n" : "\n"
            
            # method didn't need to be extracted as it didnt make code more understandable
            """
            def checkIfInTop15(avg40YdTime):

                return avg40YdTime < 4.41
            """
			# Replace it with

            inTop15 = " *Top 15\n" if (avg40YdTime < 4.41) else "\n"

            print(inTop15)

		# Know when temps are getting in the way
		# To get rid of a temp
		# 1. Declare it as final to make sure it is declared only once
		# 2. Replace the right side with the temp name

        # With temp
        """
        dashTime = 4.50

        avg40YdDash = self.getAvgDashTime()

        dashGrade = "Good" if (dashTime <= avg40YdDash) else "Bad"

        print("That was a ", dashGrade, " time")
        """

        # Without temp
        dashTime = 4.50

        dashGrade = "Good" if (dashTime <= self.getAvgDashTime()) else "Bad"

        print("That was a ", dashGrade, " time")

    def getAvgDashTime(self, dashTimes):

        totalDashTimes = 0.0

        for i in range(len(dashTimes)):
            totalDashTimes += dashTimes[i]
        return totalDashTimes / len(dashTimes)

    def getAvgDashTime(self):
        return 4.41        
	


fb40Dash = FootballPlayer40YardDashInfo()

# Cannot run this part due to football player being used is not provided by video
"""
# Add Clark Kent for example

cKent40YdDashTimes = [4.36, 4.39, 4.41]
clarkKent = FootballPlayer("Clark Kent", cKent40YdDashTimes)
fb40Dash.addFootballPlayer(clarkKent)

# Add Bruce Wayne for example

bWayne40YdDashTimes = [4.42, 4.43, 4.49]
bruceWayne = FootballPlayer("Bruce Wayne", bWayne40YdDashTimes)
fb40Dash.addFootballPlayer(bruceWayne)
"""
fb40Dash.printPlayerInfo()




#Working with local variables
"""
double average 0.0;

double[] dashTimes = {4.36, 4.39, 4.41};

double totalDashTimes = 0.0;

for(int i=0; i < len(dashTimes); i++){
	totalDashTimes += dashTimes[i]; }
average = totalDashTimes / numOfTimes.length;


#Replaced by

dashTimes = [4.36, 4.39, 4.41]

average = getAvgDashTime(dashTimes)

def getAvgDashTime(dashTimes):

		double totalDashTimes = 0.0;

		for i in range(len(dashTimes))
			totalDashTimes += dashTimes[i]		
		return totalDashTimes / len(dashTimes)

#Replacing a temp with a Query

double avgDashTime = totalDashTimes / totalDashes;

if(avgDashTime > 4.41) {
	System.out.println("Average Time"); }

#Better Solution

if(avgDashTime() > 4.41) {
	System.out.println("Average Time"); }

double avgDashTime(){

	return totalDashTimes / totalDashes;}

 * /
"""