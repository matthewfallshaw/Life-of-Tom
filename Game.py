import json

class Game:
    def __init__(self,json_file_path):
        json_file = open(json_file_path)
        config = json.load(json_file)
        self.scenes = []
        for scene_config in config["scenes"]:
            scene = Scene(scene_config)
            self.scenes.append(scene)
        self.current_scene = self.scenes[0]

    def play(self):
        self.current_scene.play()

class Scene:
    def __init__(self, scene_config):
        self.config = scene_config

    def play(self):
        print(self.config)

Game('game.json').play()
        
import sys
def ask(question):  # Plays a question in the code.
    print(question['prompt'])
    for ii in range(len(question['options'])):
        option = question['options'][ii]
        print('[' + str(int(ii) + 1) + '] ' + option['description'])
    answer = input('Type the number of your answer: ')
    if answer == 'quit':
        sys.exit()
    while answer != '1' and answer != '2' and answer != '3':
        answer = input('Please type the number of your answer: ')
    choice = question['options'][int(answer) - 1]
    reward = choice['reward']
    print(choice['response']+"\n")
