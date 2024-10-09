import os

directory = 'save_games'

txt_files = [file for file in os.listdir(directory) if file.endswith('.txt')]

for file in txt_files:
    print(file)