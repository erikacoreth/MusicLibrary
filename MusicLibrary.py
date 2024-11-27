class User:
    def __init__(self, name):
        self.name = name
        self.songs = {}

    def add_song(self, title, artist):
        self.songs[title] = artist
        print('song added')

    def get_song(self, title):
        artist = self.songs.get(title)
        if artist:
            print(f"Song: '{title}', Artist: {artist}")
        else:
            print('song not found')

    def update_song(self, title, new_artist):
        if title in self.songs:
            self.songs[title] = new_artist
            print('Updated song')
        else:
            print('song not found')


    def delete_song(self, title):
        if title in self.songs:
            del self.songs[title]
            print('Song was removed')
        else:
            print('song not found')


    def display_songs(self):
        if self.songs:
            print(f"{self.name}'s music collection: ")
            for title, artist in self.songs.items():
                print(f'    "{title}" by {artist}')
        else:
            print(f"{self.name}'s collection is empty.")


class MusicOrganizer:
    def __init__(self):
        self.users = {}

    def add_user(self, name):
        if name in self.users:
            print(f"User '{name}' already exists.")
        else:
            self.users[name] = User(name)

    def change_user(self, name):
        if name in self.users:
            return self.users[name]
        else:
            print(f"User '{name}' not found. Please add the user first")
            return None
#main program
    def main(self):
        current_user = None

        while True:
            if len(self.users) == 0:
                print("No users found. Please add a new user to get started.")
                name = input("Enter user name: ")
                self.add_user(name)
                current_user = self.users[name] #set the new user as current_user
                print(f"User '{current_user.name}' is now active. \n")
                continue #go back to the beginning of the loop

            #display options and perform actions now that we have users
            print("Options: [1] Add User, [2] Change User, [3] Add song, [4] Retrieve song details, [5] Update song details, [6] Delete a song, [7] Display all songs, [8] Exit")
            choice = input("Choose an option: ")

            if choice == '1': #add user
                name = input("Enter user name: ")
                self.add_user(name)

            elif choice == '2': #change user
                name = input("Enter user name to switch to: ")
                if name in self.users:
                    current_user = self.users[name]
                    print(f"Switched to '{current_user.name}'.")
                else:
                    print('User not found')

            elif choice == '3': #add song
                if current_user:
                    title = input("Enter song title: ")
                    artist = input("Enter the artist of the song")
                    current_user.add_song(title, artist)
            elif choice == '4': #get song
                if current_user:
                    title = input('Enter song title to retrieve: ')
                    current_user.get_song(title)

            elif choice == '5': #update song details
                if current_user:
                    title = input('Enter song title to update: ')
                    new_artist = input("Enter new artist name: ")
                    current_user.update_song(title, new_artist)
            elif choice == '6': #del song
                if current_user:
                    title = input('Enter song you want to delete: ')
                    current_user.delete_song(title)

            elif choice == '7': #display all songs
                if current_user:
                    current_user.display_songs()

            elif choice == '8': #exit
                print('Exiting program.')
                break

            else:
                print('invalid option. Please try agan')

#run program
organizer = MusicOrganizer()
organizer.main()














