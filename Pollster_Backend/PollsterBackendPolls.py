from Pollster_Backend import PollsterBackendBase

__all__ = ['PollsterBackendPolls']


class PollsterBackendPolls(PollsterBackendBase.PollsterBackendBase):
    """
    This is the class for the polling graph backend.
    This class will deal with the graphs for both the national and state wide polling graphs.
    Methods within this class
        get_poli_avg(self, st_or_nat, poli_name, start_date, end_date)
        get_poli_points(self, st_or_nat, poli_name, start_date, end_date)
    """

    def __init__(self, csv_file, poll_dict, poll_dict_keys):
        super().__init__(csv_file, poll_dict, poll_dict_keys)

    def get_poli_points(self, st_or_nat, poli_name, start_date, end_date) -> list:
        """
        This method gets all the pct points a politician garnered in a specific time range and state v national poll
        :param st_or_nat: Specifies if you want to look at a particular states polls vs. national polls
        :param poli_name: Specifies the name of the candidate you want
        :param start_date: Specifies the date of polls you want to start from
        :param end_date: Specifies the date of polls you want to end with
        :return: All the pct points
        """
        poli_dict = self.poll_dict
        poli_points = []
        for i in range(0, len(poli_dict['answer'])):
            if self.check_date_1_greater_o_eq(self.switch_month_day(end_date),
                                              self.switch_month_day(poli_dict['end_date:'][i])) \
                    and self.check_date_1_greater_o_eq(self.switch_month_day(poli_dict['end_date:'][i]),
                                                       self.switch_month_day(start_date)) \
                    and poli_dict['notes'][i] != 'head-to-head poll' and poli_dict['answer'][i] == poli_name \
                    and poli_dict['state'][i] == st_or_nat:
                poli_points.append(poli_dict['pct'][i])
        return poli_points

    def get_polls_list(self, st_or_nat, start_date, end_date) -> list:
        """
        Gets a list of polls in a specific date range. The list of polls contains key values such as the poll_id,
        end_date:, display_name, sample_size, population, url, and an array of dictionaries that have candidate and pct
        :param st_or_nat: Specifies if you want to look at a particular states polls vs. national polls
        :param start_date: Specifies the date of polls you want to start from
        :param end_date: Specifies the date of polls you want to end with
        :return:
        """
        poli_dict = self.poll_dict
        polls_list = []
        poll_list_counter = -1
        for i in range(0, len(poli_dict['end_date:'])):
            if self.check_date_1_greater_o_eq(self.switch_month_day(end_date),
                                              self.switch_month_day(poli_dict['end_date:'][i])) \
                    and self.check_date_1_greater_o_eq(self.switch_month_day(poli_dict['end_date:'][i]),
                                                       self.switch_month_day(start_date)) \
                    and poli_dict['notes'][i] != 'head-to-head poll'\
                    and poli_dict['state'][i] == st_or_nat:
                if poli_dict['state'][i] == "":
                    poll_state = "National"
                else:
                    poll_state = poli_dict['state'][i]
                if i == 0 or (poli_dict['poll_id'][i] != poli_dict['poll_id'][i-1]):
                    polls_list.append([poli_dict['poll_id'][i], poll_state, poli_dict['end_date:'][i],
                                       poli_dict['display_name'][i], poli_dict['sample_size'][i],
                                       poli_dict['population'][i], poli_dict['url'][i],
                                       [{'{poli_name}'.format(poli_name=poli_dict['answer'][i]): poli_dict['pct'][i]}]]
                                      )
                    poll_list_counter += 1
                else:
                    polls_list[poll_list_counter][7].append(
                        {'{poli_name}'.format(poli_name=poli_dict['answer'][i]): poli_dict['pct'][i]}
                    )
        return polls_list

    def get_poli_avg(self, st_or_nat, poli_name, start_date, end_date) -> float:
        """
        This method gets the average pct of polling data for a candidate.
        :param st_or_nat: Specifies if you want to look at a particular states polls vs. national polls
        :param poli_name: Specifies the name of the candidate you want
        :param start_date: Specifies the date of polls you want to start from
        :param end_date: Specifies the date of polls you want to end with
        :return: The average pct of polling data for the candidate at the specific time range
        """
        poli_avg = 0
        poli_points = self.get_poli_points(st_or_nat, poli_name, start_date, end_date)
        for i in poli_points:
            poli_avg += float(i)
        return poli_avg / len(poli_points)
