import csv

__all__ = ['PollsterBackendBase']


class PollsterBackendBase:
    """
    This is the base class for the PollsterBackend all PollserterBackend subclasses should have the methods in here.
    SubClasses:
        Pollster_Backend_Polls.py
        Pollster_Backend_Donors.py
        Pollster_Backend_Volunteers.py
    """
    def __init__(self, csv_file, poll_dict, poll_dict_keys):
        self.csv_file = csv_file
        # Every Pollster class should have a CSV file that contains the data it is reading from.
        self.poll_dict = poll_dict
        self.poll_dict_keys = poll_dict_keys
        # Gets all the user inputted data about the csv file
        with open(self.csv_file, 'rt') as f:
            csv_list = []
            csv_reader = csv.reader(f)
            count = 0
            for line in csv_reader:
                if count != 0:
                    csv_list.append(line)
                count += 1
        for line in csv_list:
            counter = 0
            for data in line:
                self.poll_dict[self.poll_dict_keys[counter]].append(data)
                counter += 1
        # Converts that csv file's data into a dictionary that stores each value by headers listed in poll_dict_keys
