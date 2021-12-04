from collections import namedtuple

#hp = held points
#bp = banked points
#num_dice = number of dice you are currently holding

WIN_POINTS = 10000
STATES = None #Implement later

State_key = namedtuple("State_key" ["your_hp", "your_bp", "opponent_hp", "opponent_bp", "num_dice"])

class GameState():
    def __init__(self, state_key):
        self.your_hp = state_key.your_hp
        self.your_bp = state_key.your_bp
        self.opponent_hp = state_key.opponent_hp
        self.opponent_bp = state_key.opponent_bp
        self.num_dice = state_key.num_dice
        if self.your_hp + self.your_bp >= WIN_POINTS:
            self.win_chance = 1
        else:
            self.win_chance = 0

    def update_state(self):
        self.win_chance = max(STATES[State_key(0, self)])

    def gen_key(self, your_hp=self.your_hp, your_bp = self.your_bp, opponent_hp = self.opponent_hp, opponent_bp = self.opponent_bp, num_dice = self.num_dice):
        return State_key(your_hp, your_bp, opponent_hp, opponent_bp, num_dice)


def initial_state_generator():
    pass