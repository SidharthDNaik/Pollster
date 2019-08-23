from Pollster_Backend import PollsterBackendPolls
from flask import Flask
app = Flask(__name__)

p = PollsterBackendPolls.PollsterBackendPolls(csv_file='C:/Pollster/polls/president_primary_polls.csv',
                                              poll_dict={'question_id': [], 'poll_id': [], 'cycle': [], 'state': [],
                                                         'pollster_id': [],
                                                         'pollster': [], 'sponsor_ids': [], 'sponsors': [],
                                                         'display_name': [],
                                                         'pollster_rating_id': [], 'pollster_rating_name': [],
                                                         'fte_grade': [], 'sample_size': [],
                                                         'population': [], 'population_full': [], 'methodology': [],
                                                         'office_type': [],
                                                         'start_date': [], 'end_date:': [], 'sponsor_candidate': [],
                                                         'internal': [], 'partisan': [],
                                                         'tracking': [], 'nationwide_batch': [], 'created_at': [],
                                                         'notes': [], 'url': [], 'stage': [],
                                                         'party': [], 'answer': [], 'candidate_name': [], 'pct': []},
                                              poll_dict_keys=['question_id', 'poll_id', 'cycle', 'state', 'pollster_id',
                                                              'pollster', 'sponsor_ids', 'sponsors', 'display_name',
                                                              'pollster_rating_id', 'pollster_rating_name', 'fte_grade',
                                                              'sample_size',
                                                              'population', 'population_full', 'methodology',
                                                              'office_type',
                                                              'start_date', 'end_date:', 'sponsor_candidate',
                                                              'internal', 'partisan',
                                                              'tracking', 'nationwide_batch', 'created_at', 'notes',
                                                              'url', 'stage',
                                                              'party', 'answer', 'candidate_name', 'pct']
                                              )

print(p.reverse_array(p.get_poli_points("", "Sanders", '7/27/19', '8/20/2019')))
print(p.reverse_array(p.get_poli_points("", "Biden", '7/27/19', '8/20/2019')))
print(p.reverse_array(p.get_poli_points("", "Warren", '7/27/19', '8/20/2019')))
print(p.get_poli_avg("", "Biden", '7/27/19', '8/20/2019'))
print(p.get_poli_avg("", "Harris", '7/27/19', '8/20/2019'))
print(p.get_poli_avg("", "Sanders", '7/27/19', '8/20/2019'))
print(p.get_poli_avg("", "Warren", '7/27/19', '8/20/2019'))
print(p.get_poli_avg("", "Yang", '7/27/19', '8/20/2019'))
r = p.get_polls_list("", '8/15/19', '8/20/2019')
print(p.reverse_array(p.get_poll_dates("", '7/27/19', '8/20/2019')))

print(p.get_poli_avg("", "Yang", '7/27/19', '8/20/2019'))





