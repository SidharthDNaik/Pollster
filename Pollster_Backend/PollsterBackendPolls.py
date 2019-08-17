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

    def get_poli_points(self, st_or_nat, poli_name):
        poli_dict = self.poll_dict
        poli_name_positions = []
        for i in range(0, len(poli_dict['answer'])):
            if i == poli_name:
                poli_name_positions.append(poli_name_counter)
            poli_name_counter += 1

