import pandas as pd
import numpy as np


# Stat_points Class Definition
# Instantiation from the Stat_points class, main team players



class Stat_points:
    # Define Doors: key/value <=> door_number / lvl_associated 
    doors = {1: 10, 2: 15, 3: 20, 4: 25, 5: 30, 6: 35, 7: 40,
             8: 45, 9: 50, 10: 60, 11: 70, 12: 80, 13: 100,
             14: 120, 15: 150, 16: 180, 17: 198}
    
    # Total of points available until level 190RB
    max_points = 3*289 + 5

    def __init__(self, name, STR=0, CON=0, INT=0, WIS=0, SPD=0):
        self.name = name
        self.STR = STR
        self.CON = CON
        self.INT = INT
        self.WIS = WIS
        self.SPD = SPD
    
    def __str__(self):
        objective_stat = self.get_all_objective_stats()
        returned_value = 'Level 289 stats objective:\n'
        for key, value in objective_stat.items():
            returned_value += f'{key}: {value}\n'
        return returned_value

    def __repr__(self) -> str:
        return str(self)

    def get_all_objective_stats(self):
        return {'STR': self.STR, 'CON': self.CON, 'INT': self.INT, 'WIS': self.WIS, 'SPD': self.SPD}
    
    def show_final_stats_with_PP(self):
        dict_ = self.get_all_objective_stats()
        for key in dict_.keys():
            dict_[key] += 48
        print('Final stats with PP:\n')
        for key, value in dict_.items():
            print(f'{key}: {value}')

    def check_stat_level_max(self, with_PP=False):
        total_points = self.STR + self.CON + self.INT + self.WIS + self.SPD
        max_points = 3*289+5
        if with_PP:
            max_points += 48*5
        if total_points != max_points:
            print(f'There are still {max_points - total_points} points to attribute.')
        else:
            print('Your previsions stats match the total points available.')
            return self.get_all_objective_stats()
    
    def reattribution(self, list_):
        self.STR, self.CON, self.INT, self.WIS, self.SPD = list_
        return None

    def prevision_for_specific_level(self, level=None, door=None):
        # If we enter a door number, convert it to level.
        if door != None:
            level = self.doors[door]

        print(f'At level {level}, your points should converge to:')
        objective_stat = self.get_all_objective_stats()
        available_points = 3*level + 5
        for key, value in objective_stat.items():
            points = int(available_points * value/self.max_points)
            print(f'{key}: {points}')
        
        return None
    



    def create_team(self, *players):
        '''
        A Refaire plus tard (stat <=> index; variables: player.name)
        '''
        data = []

        for player in players:
            player_data = player.get_all_objective_stats()
            player_data['Names'] = player.name
            data.append(player_data)
        
        team_df = pd.DataFrame(data)
        return team_df


    def player_limits(self, starting_door=8):
        columns = {'Stats': ['STR', 'CON', 'INT', 'WIS', 'SPD']}

        # Loop on door
        for door in range(8, max(list(self.doors.keys()))+1):
            objective_stat = self.get_all_objective_stats()
            available_points = 3*self.doors[door] + 5
            columns[f'door {door} (lvl {self.doors[door]})'] = []

            # Loop on stats of the door
            for value in objective_stat.values():
                columns[f'door {door} (lvl {self.doors[door]})'].append(int(available_points * value/self.max_points))

        player_evolution_df = pd.DataFrame(columns, index=None)
        return player_evolution_df






# Main team players
# Team 1
celto = Stat_points('celto', 0, 288, 532, 52, 0)
pulsaar = Stat_points('Pulsaar', 318, 318, 0, 102, 102)
loctra = Stat_points('loctra', 0, 452, 284, 102, 0)
harmisteas = Stat_points('Harmisteas', 0, 352, 352, 102, 52)
team_1 = [celto, pulsaar, loctra, harmisteas]

# Team 2
bosofishes = Stat_points('Bosofishes', 840, 0, 0, 0, 0)
colest = Stat_points('Colest', 0, 278, 208, 52, 302)
lapis = Stat_points('Lapis Lazuli', 0, 300, 488, 52, 0)
starSteel = Stat_points('starSteel', 154, 464,0, 52, 202)
team_2 = [bosofishes, colest, lapis, starSteel]


