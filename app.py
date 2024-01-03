from constants import TEAMS, PLAYERS
import random

def clean_data(players):
    clean_data_list = []
    for player in players:
        clean_data = {
            "name": player["name"],
            "guardians": player["guardians"],
            "experience": player["experience"] == "YES",
            "height": int(player["height"].split()[0])
        }
        clean_data_list.append(clean_data)
    return clean_data_list

def balance_teams(player_name_list, num_players_team):
    teams_assignment = {team: [] for team in TEAMS}

    for team_name in TEAMS:
        random.shuffle(player_name_list)
        for _ in range(num_players_team):
            teams_assignment[team_name].append(player_name_list.pop())

    return teams_assignment

if __name__ == "__main__":
    players = PLAYERS
    num_players_team = int(len(players) / len(TEAMS))

    player_name_list = [{"name": player["name"]} for player in players]
    result = clean_data(players)
    
    balance = balance_teams(player_name_list, num_players_team)
    
    choice_pick = True

    while choice_pick:
        print("\n\nBASKETBALL TEAM STATS TOOL\n\n")
        print("      ----MENU----      \n")
        print("Here are your choices: ")
        print("A) Display Team Stats")
        print("B) Quit\n")
        first_choice = input("Enter an option: ").lower()

        if first_choice == "a":
            print("Here are the available teams:")
            for index, team_name in enumerate(TEAMS, start=1):
                print(f"{index}) {team_name}")

            # Optionally, let the user choose a team
            try:
                team_choice = int(input("Enter the number of the team: "))
                selected_team = TEAMS[team_choice - 1]  # Adjust the index to match user input
                players_in_team = balance[selected_team]
                num_players = len(players_in_team)
                print(f"\nTeam: {selected_team} stats\n")
                print("______________________\n")
                player_names = ", ".join([player["name"] for player in balance[selected_team]])
                print(f"Total number of players: {num_players}")
                print(player_names)
            except (ValueError, IndexError):
                print("Invalid team choice. Please enter a valid team number.")

        elif first_choice == "b":
            print("Exiting the program.")
            choice_pick = False  # Set the flag to False to exit the loop

        else:
            print("Invalid option. Please choose 'A' or 'B'.")