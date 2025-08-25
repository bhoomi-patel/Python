import pickle 
from datetime import datetime

class GameSave:
    def __init__(self,player_name):
            self.player_name = player_name
            self.level = 1
            self.score = 0
            self.inventory = []
            self.last_played = datetime.now()
    def save_game (self):
            filename = f"{self.player_name}_save.pkl"
            with open(filename,"wb") as f:
                  pickle.dump(self,f) # save entire object
            print(f"Game saved for {self.player_name}")
    @staticmethod 
    def load_game(player_name):
        filename = f"{player_name}_save.pkl"
        try :
             with open (filename,'rb') as f:
                    game = pickle.load(f)
             print(f"welcome back , {game.player_name} !") 
             return game 
        except FileNotFoundError:
               print("No save file found . starting new game!")
               return GameSave(player_name)   
game  = GameSave("Hero")
game.level = 5
game.score = 1500
game.inventory = ["sword","shield","key"]
game.save_game()

#Later.........
loaded_game = GameSave.load_game("Hero")
print(f'Level: {loaded_game.level}, Score: {loaded_game.score}, Inventory: {loaded_game.inventory}')