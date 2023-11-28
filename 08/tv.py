import random

class Television:
    def __init__(self, channel=1, volume=50, is_on=False):
        self.channel = channel
        self.volume = volume
        self.is_on = is_on
        self.channel_list = []

    def increase_volume(self):
        if self.is_on:
            self.volume += 1
            print("Volume increased:", self.volume)
        else:
            print("The TV is off. Please turn it on first.")

    def decrease_volume(self):
        if self.is_on:
            self.volume -= 1
            print("Volume decreased:", self.volume)
        else:
            print("The TV is off. Please turn it on first.")

    def change_channel(self, new_channel):
        if self.is_on:
            if new_channel in self.channel_list:
                self.channel = new_channel
                print("Channel changed to:", self.channel)
            else:
                print("Invalid channel. Please select a channel from the channel list.")
        else:
            print("The TV is off. Please turn it on first.")

    def display_info(self):
        if self.is_on:
            print("Current Channel:", self.channel)
            print("Current Volume:", self.volume)
        else:
            print("The TV is off. Please turn it on first.")

    def power_on_off(self):
        self.is_on = not self.is_on
        if self.is_on:
            print("TV is now on.")
        else:
            print("TV is now off.")

    def add_channel(self, channel):
        self.channel_list.append(channel)
        print("Channel", channel, "added to the channel list.")

    def select_channel(self):
        if self.is_on:
            if self.channel_list:
                self.channel = random.choice(self.channel_list)
                print("Channel selected:", self.channel)
            else:
                print("No channels available. Please add channels to the channel list.")
        else:
            print("The TV is off. Please turn it on first.")



tv = Television()
tv.channel_list = [3, 5, 7, 9, 11, 13]  # Channel list set

# test methods
tv.power_on_off()  
tv.increase_volume()  
tv.decrease_volume()   
tv.add_channel(2)  
tv.select_channel() 
tv.display_info()  
tv.power_on_off()  