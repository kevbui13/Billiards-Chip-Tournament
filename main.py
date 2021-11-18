import random

global active_player_tables
global active_players
global chips

# Team Numbers
teams = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]

# Table Location/Descriptions - currently 4 tables
pool_table = ['Table 01 L', 'Table 01 W', 'Table 02 L', 'Table 02 W', 'Table 03 L', 'Table 03 W', 'Table 04 L', 'Table 04 W']

# Players at the Tables - 4 tables, 8 positions
active_player_tables = []

# Players available
active_players = list.copy(teams)

# Chips team # has. Team 0 has 0 chips.
chips = [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

def print_pairings ():
    for i in range(0, len(active_player_tables), 2):
        print(pool_table[i], "<<", "Team #", active_player_tables[i], "===VS===" ,"Team #", active_player_tables[i+1], ">>", pool_table[i+1])

def print_available_players ():
    print("Available Players")
    print(active_players)

def print_chips ():
    for i in range(1,33):
        print("Team #", teams[i-1], "=== ", chips[i], "chips")

if __name__ == '__main__':

    active_player_tables = random.sample(active_players, 8)

    print("Starting Pairings")
    print_pairings()

    for i in active_player_tables:
        active_players.remove(i)

    print_available_players()

    table_num = 1 # initializes initial while loop

    while table_num != "done":

        table_num = input("Which table position lost? or chips, tables, or done. ")
        if table_num == "chips":
            print_chips()
        elif table_num == "tables":
            print_pairings()
            print_available_players()
        elif table_num != "done":
            table_num = int(table_num)
            table_num = table_num - 1 # Shifting by 1, real position vs position in list

            if (table_num % 2) == 0: # If on loser location and lost
                buffer = active_player_tables[table_num]
                chips[buffer] = chips[buffer] - 1 # Losing player loses a chip.

                b = random.sample(active_players, 1)
                while chips[b[0]] < 1:
                    b = random.sample(active_players, 1)

                active_player_tables[table_num] = b[0]
                print("Send player #", b[0], "to Table:", round((table_num+1)/2))
                active_players.append(buffer)
                active_players.remove(b[0])

            elif (table_num % 2) == 1: # If on winner location and lost
                buffer = active_player_tables[table_num]
                chips[buffer] = chips[buffer] - 1 # Losing player loses a chip.
                active_player_tables[table_num] = active_player_tables[table_num - 1]

                b = random.sample(active_players, 1)
                while chips[b[0]] < 1:
                    b = random.sample(active_players, 1)

                active_player_tables[table_num - 1] = b[0]
                print("Send player #", b[0], "to Table:", round((table_num+1)/2))
                active_players.append(buffer)
                active_players.remove(b[0])

            print_pairings()
            print_available_players()
        else:
            print_pairings()
            print_available_players()