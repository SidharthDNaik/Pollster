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

    def get_poli_points(self, st_or_nat, poli_name) -> list:
        poli_dict = self.poll_dict
        poli_points = []
        for i in range(0, len(poli_dict['answer'])):
            if poli_dict['answer'][i] == poli_name and poli_dict['state'][i] == st_or_nat:
                poli_points.append(poli_dict['pct'][i])
        return poli_points

    def get_poli_avg(self, st_or_nat, poli_name) -> float:
        poli_avg = 0
        poli_points = self.get_poli_points(st_or_nat, poli_name)
        for i in poli_points:
            poli_avg += float(i)
        return poli_avg/len(poli_points)
