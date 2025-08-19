import os
import yt_dlp
from system_specific import *

class Downloader:
    pass

class App:
    def __init__(self):
        self.selected_playlist = "None"
        self.selected_songs = ["No"]
        self.selected_folder_path = "None"

    def menu_print(self):
        print(f"[1] - Select a playlist | Selected playlist : {self.selected_playlist}")
        print(f'[2] - Select a song or multiple songs | Selected songs : {self.selected_songs}')
        print(f"[3] - Select a folder output of downloaded songs | Selected folder : {self.selected_folder_path}\n")
        print(f"[4] - Exit")

        print("Please select an option by pressing the corresponding number on your keyboard...")
    
    def select_playlist(self, input:str):
        self.selected_playlist = input

    def select_songs(self, input_list:list, input_str:str):
        if input_list is not None:
            self.selected_songs.extend(input_list)
        if input_str is not None:
            self.selected_songs.append(input_str)


def playlist_select():
    pass

def songs_select():
    pass

def folder_select():
    pass

if __name__ == '__main__':
    app = App()

    while True:
        clear_screen()
        app.menu_print()
        input = int(option_wait())

        if input == 1:
            playlist_select()
        elif input == 2:
            songs_select()
        elif input == 3:
            folder_select()
        elif input == 4:
            exit(0)
