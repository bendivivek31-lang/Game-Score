#Taking Inputs
print("=" * 30)
Player = input("Enter the player's name: ")
Games_Played = int(input("Number of Games played: "))
Total_Score = int(input("Total Score Achieved: "))
#Calculation
Average_Score = Total_Score / Games_Played
print("=" * 30)
#Displaying Output
print("----RESULT----\n")
print(f"Player Name: {Player}")
print(f"Games Played: {Games_Played}")
print(f"Total Score: {Total_Score}")
print(f"Aerage Score: {Average_Score}")