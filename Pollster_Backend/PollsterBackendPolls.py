from Pollster_Backend import PollsterBackendBase

__all__ = ['PollsterBackendPolls']


class PollsterBackendPolls(PollsterBackendBase.PollsterBackendBase):
    """
    This is the class for the polling graph backend.
    This class will deal with the graphs for both the national and state wide polling graphs.
    Methods within this class
        get_poli_avg(st_or_nat)
        get_poli_points(st_or_nat, poli_name)
    """

    def __init__(self, csv_file, poll_dict, poll_dict_keys):
        super().__init__(csv_file, poll_dict, poll_dict_keys)

    def get_poli_points(self, st_or_nat, poli_name, start_date, end_date) -> list:
        poli_dict = self.poll_dict
        poli_points = []
        for i in range(0, len(poli_dict['answer'])):
            if self.check_date_1_greater_o_eq(self.switch_month_day(end_date),
                                              self.switch_month_day(poli_dict['end_date:'][i])) \
                    and self.check_date_1_greater_o_eq(self.switch_month_day(poli_dict['end_date:'][i]),
                                                       self.switch_month_day(start_date)) \
                    and poli_dict['notes'][i] != 'head-to-head poll':
                if poli_dict['answer'][i] == poli_name and poli_dict['state'][i] == st_or_nat:
                    poli_points.append(poli_dict['pct'][i])
        return poli_points

    def get_poli_avg(self, st_or_nat, poli_name, start_date, end_date) -> float:
        poli_avg = 0
        poli_points = self.get_poli_points(st_or_nat, poli_name, start_date, end_date)
        for i in poli_points:
            poli_avg += float(i)
        return poli_avg / len(poli_points)

    def switch_month_day(self, date_1) -> list:
        date_1_array = date_1.split('/')
        a, b = date_1_array[0], date_1_array[1]
        date_1_array[0], date_1_array[1] = b, a
        return date_1_array

    def check_date_1_greater_o_eq(self, date_1, date_2, i=2) -> bool:
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
