import csv

__all__ = ['PollsterBackendBase']


class PollsterBackendBase:
    """
    This is the base class for the PollsterBackend contains all the methods needed generically.
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

    def switch_month_day(self, date_1) -> list:
        """
        This method switches the month and day in the dates that get sent in. For example if I send in 8/4/19/ this
        returns 4/8/19.
        :param date_1: The date I want to switch
        :return: Returns the switched date value. This is needed because I parse through the array Year -> Month -> Day
        in the check_date_1_greater_o_eq method
        """
        date_1_array = date_1.split('/')
        a, b = date_1_array[0], date_1_array[1]
        date_1_array[0], date_1_array[1] = b, a
        return date_1_array

    def check_date_1_greater_o_eq(self, date_1, date_2, i=2) -> bool:
        """
        This method takes in two data values that will be used as the range for the polling data displayed. Once it has
        those values it checks if the date_1 value is greater than or equal to the date_2
        :param date_1: The date value that you want to check is greater than or equal to
        :param date_2: The date value that you are comparing date_1 to
        :param i: This is used because I wrote this as a recursive method so i represents the indexes in the array and
        is passed in recursively.
        :return: Returns T/F depending on if date_1 is greater than or equal to date_2
        """
        if i == 2:
            date_1[i] = date_1[i].replace('20', '')
            date_2[i] = date_2[i].replace('20', '')
        if i >= 0 and (int(date_1[i]) == int(date_2[i])):
            return self.check_date_1_greater_o_eq(date_1, date_2, i - 1)
        elif i >= 0 and int(date_1[i]) > int(date_2[i]):
            return True
        elif i >= 0 and int(date_1[i]) < int(date_2[i]):
            return False
        else:
            return True
