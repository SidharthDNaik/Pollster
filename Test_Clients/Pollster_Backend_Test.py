from Pollster_Backend import PollsterBackendPolls

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
print(p.get_poli_points("", "Sanders"))
print(p.get_poli_avg('', 'Sanders'))
print(p.get_poli_avg('', 'Warren'))
print(p.get_poli_avg('', 'Harris'))
print(p.get_poli_avg('', 'Biden'))
