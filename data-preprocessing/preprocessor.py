import json
from pprint import pprint
from collections import Counter, OrderedDict
import csv

#   Load characters.json file
training_set_part1 = []

with open("input/characters.json") as input_file1:
        characters_data = json.load(input_file1)

#   For each object in the array "characters", extract "characterName", sizeOf array "killed" and (if sizeOf array "killedBy" > 1, enter 1 else 0)
#       into variables named as "name", "killCount" and "Dead"
        for character in characters_data['characters']:
                training_row = OrderedDict()

                training_row['character_name'] = str(character['characterName']) if 'characterName' in character else ' '
                training_row['kill_count'] = len(character['killed']) if 'killed' in character else 0
                training_row['dead'] = 1 if 'killedBy' in character else 0

                training_set_part1.append(training_row)

# pprint(training_set_part1)

#   Load episodes.json file
training_set_part2 = []

with open("input/episodes.json") as input_file2:
        episodes_data = json.load(input_file2)

#   Create a disctionary of the form <name, episodeAppearanceCount>
#   For each object in the array "episodes", if a "characterName" appears, increase its count in dictionary by 1
        episode_counter = Counter()
        for episode in episodes_data['episodes']:
                characters = []
                for scene in episode['scenes']:
                        for character in scene['characters']:
                                characters.append(character['name'])
                characters = set(characters)

                for character in characters:
                        episode_counter[character] += 1

        for character_name, episode_appearance_count in episode_counter.items():
                training_row = OrderedDict()

                training_row['character_name'] = str(character_name)
                training_row['episode_appearance_count'] = episode_appearance_count

                training_set_part2.append(training_row)

# pprint(training_set_part2)

# Extract only rows with data in all columns
# i.e. for each character name, only if values exist in both training set parts, construct a new final training set that we would work on
count = 0
training_set = []

for character_row in training_set_part1:
        for episode_row in training_set_part2:
                if character_row['character_name'] == episode_row['character_name']:
                        training_row = OrderedDict()

                        training_row['character_name'] = str(character_row['character_name'])
                        training_row['episode_appearance_count'] = episode_row['episode_appearance_count']
                        training_row['kill_count'] = character_row['kill_count']
                        training_row['dead'] = character_row['dead']

                        training_set.append(training_row)
                        count += 1
                        break
        # break
print count
pprint(training_set)
# Write 2 training sets into 2 csv files
with open('output/characters.csv', 'w') as output_file1:
        writer = csv.DictWriter(output_file1, training_set_part1[0].keys())
        writer.writeheader()
        writer.writerows(training_set_part1)

with open('output/episodes.csv', 'w') as output_file2:
        writer = csv.DictWriter(output_file2, training_set_part2[0].keys())
        writer.writeheader()
        writer.writerows(training_set_part2)

# Goal: After this exercise, we have training set with characters that "died" by end of Season 8 Episode 2.
#       Our test data would be constructed in the form <name, episodeAppearanceCount, killCount> to obtain a prediction for "Dead"
#               Initially, just a row from existing training set would be taken.
#               Ideally, it should be a character that after Season 8 Episode 2 makes more episode appearances and/or increases its kill count