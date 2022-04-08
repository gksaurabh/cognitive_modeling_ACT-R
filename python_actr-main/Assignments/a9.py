Python 3.9.5 (v3.9.5:0a7dcbdb13, May  3 2021, 13:17:02) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_forget2.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.DM.error False
   0.000 agent.DM.busy False
   0.000 agent.DM.latency 0.05
   0.000 agent.DM.threshold 1
   0.000 agent.DM.maximum_time 10.0
   0.000 agent.DM.record_all_chunks False
   0.000 agent.DMbuffer.chunk None
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk object:cheese task:sandwich
   0.050 agent.production cheese
   0.100 agent.production None
I have put cheese on the bread
   0.100 agent.focus.chunk object:ham task:sandwich
   0.100 agent.production ham
   0.150 agent.production None
I have put  ham on the cheese
   0.150 agent.focus.chunk action:recall_condiment task:sandwich
   0.150 agent.production recall_condiment
   0.200 agent.production None
recalling the order
   0.200 agent.DM.busy True
   0.200 agent.focus.chunk object:condiment task:sandwich
   0.218 agent.DM.error True
   0.218 agent.DMbuffer.chunk None
   0.218 agent.DM.busy False
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_forget2.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.DM.error False
   0.000 agent.DM.busy False
   0.000 agent.DM.latency 0.05
   0.000 agent.DM.threshold 1
   0.000 agent.DM.maximum_time 10.0
   0.000 agent.DM.record_all_chunks False
   0.000 agent.DMbuffer.chunk None
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk object:cheese task:sandwich
   0.050 agent.production cheese
   0.100 agent.production None
I have put cheese on the bread
   0.100 agent.focus.chunk object:ham task:sandwich
   0.100 agent.production ham
   0.150 agent.production None
I have put  ham on the cheese
   0.150 agent.focus.chunk action:recall_condiment task:sandwich
   0.150 agent.production recall_condiment
   0.200 agent.production None
recalling the order
   0.200 agent.DM.busy True
   0.200 agent.focus.chunk object:condiment task:sandwich
   0.216 agent.DMbuffer.chunk condiment:mustard
   0.216 agent.DM.busy False
   0.216 agent.production condiment
   0.266 agent.production None
I recall they wanted.......
mustard
i have put the condiment on the sandwich
   0.266 agent.focus.chunk object:bread_top task:sandwich
   0.266 agent.production bread_top
   0.316 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   0.316 agent.focus.chunk sandwich_step:stop
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_forget2.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.DM.error False
   0.000 agent.DM.busy False
   0.000 agent.DM.latency 0.05
   0.000 agent.DM.threshold 1
   0.000 agent.DM.maximum_time 10.0
   0.000 agent.DM.record_all_chunks False
   0.000 agent.DMbuffer.chunk None
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk object:cheese task:sandwich
   0.050 agent.production cheese
   0.100 agent.production None
I have put cheese on the bread
   0.100 agent.focus.chunk object:ham task:sandwich
   0.100 agent.production ham
   0.150 agent.production None
I have put  ham on the cheese
   0.150 agent.focus.chunk action:recall_condiment task:sandwich
   0.150 agent.production recall_condiment
   0.200 agent.production None
recalling the order
   0.200 agent.DM.busy True
   0.200 agent.focus.chunk object:condiment task:sandwich
   0.208 agent.DMbuffer.chunk condiment:ketchup
   0.208 agent.DM.busy False
   0.208 agent.production condiment
   0.258 agent.production None
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
   0.258 agent.focus.chunk object:bread_top task:sandwich
   0.258 agent.production bread_top
   0.308 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   0.308 agent.focus.chunk sandwich_step:stop
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_forget2.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.DM.error False
   0.000 agent.DM.busy False
   0.000 agent.DM.latency 0.05
   0.000 agent.DM.threshold 1
   0.000 agent.DM.maximum_time 10.0
   0.000 agent.DM.record_all_chunks False
   0.000 agent.DMbuffer.chunk None
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk object:cheese task:sandwich
   0.050 agent.production cheese
   0.100 agent.production None
I have put cheese on the bread
   0.100 agent.focus.chunk object:ham task:sandwich
   0.100 agent.production ham
   0.150 agent.production None
I have put  ham on the cheese
   0.150 agent.focus.chunk action:recall_condiment task:sandwich
   0.150 agent.production recall_condiment
   0.200 agent.production None
recalling the order
   0.200 agent.DM.busy True
   0.200 agent.focus.chunk object:condiment task:sandwich
   0.218 agent.DM.error True
   0.218 agent.DMbuffer.chunk None
   0.218 agent.DM.busy False
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_forget2.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.DM.error False
   0.000 agent.DM.busy False
   0.000 agent.DM.latency 0.05
   0.000 agent.DM.threshold 1
   0.000 agent.DM.maximum_time 10.0
   0.000 agent.DM.record_all_chunks False
   0.000 agent.DMbuffer.chunk None
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk object:cheese task:sandwich
   0.050 agent.production cheese
   0.100 agent.production None
I have put cheese on the bread
   0.100 agent.focus.chunk object:ham task:sandwich
   0.100 agent.production ham
   0.150 agent.production None
I have put  ham on the cheese
   0.150 agent.focus.chunk action:recall_condiment task:sandwich
   0.150 agent.production recall_condiment
   0.200 agent.production None
recalling the order
   0.200 agent.DM.busy True
   0.200 agent.focus.chunk object:condiment task:sandwich
   0.217 agent.DMbuffer.chunk condiment:ketchup
   0.217 agent.DM.busy False
   0.217 agent.production condiment
   0.267 agent.production None
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
   0.267 agent.focus.chunk object:bread_top task:sandwich
   0.267 agent.production bread_top
   0.317 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   0.317 agent.focus.chunk sandwich_step:stop
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_forget2.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.DM.error False
   0.000 agent.DM.busy False
   0.000 agent.DM.latency 0.05
   0.000 agent.DM.threshold 1
   0.000 agent.DM.maximum_time 10.0
   0.000 agent.DM.record_all_chunks False
   0.000 agent.DMbuffer.chunk None
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk object:cheese task:sandwich
   0.050 agent.production cheese
   0.100 agent.production None
I have put cheese on the bread
   0.100 agent.focus.chunk object:ham task:sandwich
   0.100 agent.production ham
   0.150 agent.production None
I have put  ham on the cheese
   0.150 agent.focus.chunk action:recall_condiment task:sandwich
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_forget2.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.DM.error False
   0.000 agent.DM.busy False
   0.000 agent.DM.latency 0.05
   0.000 agent.DM.threshold 1
   0.000 agent.DM.maximum_time 10.0
   0.000 agent.DM.record_all_chunks False
   0.000 agent.DMbuffer.chunk None
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk object:cheese task:sandwich
   0.050 agent.production cheese
   0.100 agent.production None
I have put cheese on the bread
   0.100 agent.focus.chunk object:ham task:sandwich
   0.100 agent.production ham
   0.150 agent.production None
I have put  ham on the cheese
   0.150 agent.focus.chunk action:condiment task:sandwich
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_forget2.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.DM.error False
   0.000 agent.DM.busy False
   0.000 agent.DM.latency 0.05
   0.000 agent.DM.threshold 1
   0.000 agent.DM.maximum_time 10.0
   0.000 agent.DM.record_all_chunks False
   0.000 agent.DMbuffer.chunk None
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk object:cheese task:sandwich
   0.050 agent.production cheese
   0.100 agent.production None
I have put cheese on the bread
   0.100 agent.focus.chunk object:ham task:sandwich
   0.100 agent.production ham
   0.150 agent.production None
I have put  ham on the cheese
   0.150 agent.focus.chunk action:condiment task:sandwich
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_forget2.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.DM.error False
   0.000 agent.DM.busy False
   0.000 agent.DM.latency 0.05
   0.000 agent.DM.threshold 1
   0.000 agent.DM.maximum_time 10.0
   0.000 agent.DM.record_all_chunks False
   0.000 agent.DMbuffer.chunk None
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk object:cheese task:sandwich
   0.050 agent.production cheese
   0.100 agent.production None
I have put cheese on the bread
   0.100 agent.focus.chunk object:ham task:sandwich
   0.100 agent.production ham
   0.150 agent.production None
I have put  ham on the cheese
   0.150 agent.focus.chunk object:condiment task:sandwich
   0.150 agent.production condiment_DM_request
   0.200 agent.production None
recalling the condiment
   0.200 agent.DM.busy True
   0.200 agent.focus.chunk task:recall
   0.218 agent.DM.error True
   0.218 agent.DMbuffer.chunk None
   0.218 agent.DM.busy False
   0.218 agent.production forgot
   0.268 agent.production None
I recall they wanted.......
I forgot
   0.268 agent.focus.chunk stop
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_forget2.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.DM.error False
   0.000 agent.DM.busy False
   0.000 agent.DM.latency 0.05
   0.000 agent.DM.threshold 1
   0.000 agent.DM.maximum_time 10.0
   0.000 agent.DM.record_all_chunks False
   0.000 agent.DMbuffer.chunk None
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk object:cheese task:sandwich
   0.050 agent.production cheese
   0.100 agent.production None
I have put cheese on the bread
   0.100 agent.focus.chunk object:ham task:sandwich
   0.100 agent.production ham
   0.150 agent.production None
I have put  ham on the cheese
   0.150 agent.focus.chunk object:condiment task:sandwich
   0.150 agent.production condiment_DM_request
   0.200 agent.production None
recalling the condiment
   0.200 agent.DM.busy True
   0.200 agent.focus.chunk task:recall
   0.218 agent.DM.error True
   0.218 agent.DMbuffer.chunk None
   0.218 agent.DM.busy False
   0.218 agent.production forgot
   0.268 agent.production None
I recall they wanted.......
I forgot
   0.268 agent.focus.chunk stop
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_forget2.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.DM.error False
   0.000 agent.DM.busy False
   0.000 agent.DM.latency 0.05
   0.000 agent.DM.threshold 1
   0.000 agent.DM.maximum_time 10.0
   0.000 agent.DM.record_all_chunks False
   0.000 agent.DMbuffer.chunk None
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk object:cheese task:sandwich
   0.050 agent.production cheese
   0.100 agent.production None
I have put cheese on the bread
   0.100 agent.focus.chunk object:ham task:sandwich
   0.100 agent.production ham
   0.150 agent.production None
I have put  ham on the cheese
   0.150 agent.focus.chunk object:condiment task:sandwich
   0.150 agent.production condiment_DM_request
   0.200 agent.production None
recalling the condiment
   0.200 agent.DM.busy True
   0.200 agent.focus.chunk task:recall
   0.218 agent.DM.error True
   0.218 agent.DMbuffer.chunk None
   0.218 agent.DM.busy False
   0.218 agent.production forgot
   0.268 agent.production None
I recall they wanted.......
I forgot
   0.268 agent.focus.chunk stop
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_forget2.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.DM.error False
   0.000 agent.DM.busy False
   0.000 agent.DM.latency 0.05
   0.000 agent.DM.threshold 1
   0.000 agent.DM.maximum_time 10.0
   0.000 agent.DM.record_all_chunks False
   0.000 agent.DMbuffer.chunk None
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk object:cheese task:sandwich
   0.050 agent.production cheese
   0.100 agent.production None
I have put cheese on the bread
   0.100 agent.focus.chunk object:ham task:sandwich
   0.100 agent.production ham
   0.150 agent.production None
I have put  ham on the cheese
   0.150 agent.focus.chunk object:condiment task:sandwich
   0.150 agent.production condiment_DM_request
   0.200 agent.production None
recalling the condiment
   0.200 agent.DM.busy True
   0.200 agent.focus.chunk task:recall
   0.203 agent.DMbuffer.chunk condiment:ketchup
   0.203 agent.DM.busy False
   0.203 agent.production DM_retrieve
   0.253 agent.production None
I recall they wanted....
   0.253 agent.DM.busy True
   0.253 agent.DMbuffer.chunk state:empty
   0.253 agent.focus.chunk object:bread_top task:sandwich
   0.253 agent.production bread_top
   0.259 agent.DMbuffer.chunk condiment:ketchup
   0.259 agent.DM.busy False
   0.303 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   0.303 agent.focus.chunk sandwich_step:stop
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_forget2.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.DM.error False
   0.000 agent.DM.busy False
   0.000 agent.DM.latency 0.05
   0.000 agent.DM.threshold 1
   0.000 agent.DM.maximum_time 10.0
   0.000 agent.DM.record_all_chunks False
   0.000 agent.DMbuffer.chunk None
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk object:cheese task:sandwich
   0.050 agent.production cheese
   0.100 agent.production None
I have put cheese on the bread
   0.100 agent.focus.chunk object:ham task:sandwich
   0.100 agent.production ham
   0.150 agent.production None
I have put  ham on the cheese
   0.150 agent.focus.chunk object:condiment task:sandwich
   0.150 agent.production condiment_DM_request
   0.200 agent.production None
recalling the condiment
   0.200 agent.DM.busy True
   0.200 agent.focus.chunk task:recall
   0.201 agent.DMbuffer.chunk condiment:ketchup
   0.201 agent.DM.busy False
   0.201 agent.production DM_retrieve
   0.251 agent.production None
I recall they wanted....
ketchup
   0.251 agent.DM.busy True
   0.251 agent.DMbuffer.chunk state:empty
   0.251 agent.focus.chunk object:bread_top task:sandwich
   0.251 agent.production bread_top
   0.256 agent.DMbuffer.chunk condiment:ketchup
   0.256 agent.DM.busy False
   0.301 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   0.301 agent.focus.chunk sandwich_step:stop
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_forget2.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.DM.error False
   0.000 agent.DM.busy False
   0.000 agent.DM.latency 0.05
   0.000 agent.DM.threshold 1
   0.000 agent.DM.maximum_time 10.0
   0.000 agent.DM.record_all_chunks False
   0.000 agent.DMbuffer.chunk None
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk object:cheese task:sandwich
   0.050 agent.production cheese
   0.100 agent.production None
I have put cheese on the bread
   0.100 agent.focus.chunk object:ham task:sandwich
   0.100 agent.production ham
   0.150 agent.production None
I have put  ham on the cheese
   0.150 agent.focus.chunk object:condiment task:sandwich
   0.150 agent.production condiment_DM_request
   0.200 agent.production None
recalling the condiment
   0.200 agent.DM.busy True
   0.200 agent.focus.chunk task:recall
   0.203 agent.DMbuffer.chunk condiment:ketchup
   0.203 agent.DM.busy False
   0.203 agent.production DM_retrieve
   0.253 agent.production None
I recall they wanted....
ketchup
   0.253 agent.DM.busy True
   0.253 agent.DMbuffer.chunk state:empty
   0.253 agent.focus.chunk object:bread_top task:sandwich
   0.253 agent.production bread_top
   0.271 agent.DM.error True
   0.271 agent.DMbuffer.chunk None
   0.271 agent.DM.busy False
   0.303 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   0.303 agent.focus.chunk sandwich_step:stop
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_forget2.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.DM.error False
   0.000 agent.DM.busy False
   0.000 agent.DM.latency 0.05
   0.000 agent.DM.threshold 1
   0.000 agent.DM.maximum_time 10.0
   0.000 agent.DM.record_all_chunks False
   0.000 agent.DMbuffer.chunk None
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk object:cheese task:sandwich
   0.050 agent.production cheese
   0.100 agent.production None
I have put cheese on the bread
   0.100 agent.focus.chunk object:ham task:sandwich
   0.100 agent.production ham
   0.150 agent.production None
I have put  ham on the cheese
   0.150 agent.focus.chunk object:condiment task:sandwich
   0.150 agent.production condiment_DM_request
   0.200 agent.production None
recalling the condiment
   0.200 agent.DM.busy True
   0.200 agent.focus.chunk task:recall
   0.204 agent.DMbuffer.chunk condiment:ketchup
   0.204 agent.DM.busy False
   0.204 agent.production DM_retrieve
   0.254 agent.production None
I recall they wanted....
ketchup
   0.254 agent.DM.busy True
   0.254 agent.DMbuffer.chunk state:empty
   0.254 agent.focus.chunk object:bread_top task:sandwich
   0.254 agent.production bread_top
   0.272 agent.DM.error True
   0.272 agent.DMbuffer.chunk None
   0.272 agent.DM.busy False
   0.304 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   0.304 agent.focus.chunk sandwich_step:stop
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_forget2.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.DM.error False
   0.000 agent.DM.busy False
   0.000 agent.DM.latency 0.05
   0.000 agent.DM.threshold 1
   0.000 agent.DM.maximum_time 10.0
   0.000 agent.DM.record_all_chunks False
   0.000 agent.DMbuffer.chunk None
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk object:cheese task:sandwich
   0.050 agent.production cheese
   0.100 agent.production None
I have put cheese on the bread
   0.100 agent.focus.chunk object:ham task:sandwich
   0.100 agent.production ham
   0.150 agent.production None
I have put  ham on the cheese
   0.150 agent.focus.chunk object:condiment task:sandwich
   0.150 agent.production condiment_DM_request
   0.200 agent.production None
recalling the condiment
   0.200 agent.DM.busy True
   0.200 agent.focus.chunk task:recall
   0.201 agent.DMbuffer.chunk condiment:mustard
   0.201 agent.DM.busy False
   0.201 agent.production DM_retrieve
   0.251 agent.production None
I recall they wanted....
mustard
   0.251 agent.DM.busy True
   0.251 agent.DMbuffer.chunk state:empty
   0.251 agent.focus.chunk object:bread_top task:sandwich
   0.251 agent.production bread_top
   0.259 agent.DMbuffer.chunk condiment:mustard
   0.259 agent.DM.busy False
   0.301 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   0.301 agent.focus.chunk sandwich_step:stop
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_forget2.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.DM.error False
   0.000 agent.DM.busy False
   0.000 agent.DM.latency 0.05
   0.000 agent.DM.threshold 1
   0.000 agent.DM.maximum_time 10.0
   0.000 agent.DM.record_all_chunks False
   0.000 agent.DMbuffer.chunk None
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk object:cheese task:sandwich
   0.050 agent.production cheese
   0.100 agent.production None
I have put cheese on the bread
   0.100 agent.focus.chunk object:ham task:sandwich
   0.100 agent.production ham
   0.150 agent.production None
I have put  ham on the cheese
   0.150 agent.focus.chunk object:condiment task:sandwich
   0.150 agent.production condiment_DM_request
   0.200 agent.production None
recalling the condiment
   0.200 agent.DM.busy True
   0.200 agent.focus.chunk task:recall
   0.218 agent.DM.error True
   0.218 agent.DMbuffer.chunk None
   0.218 agent.DM.busy False
   0.218 agent.production forgot
   0.268 agent.production None
I recall they wanted.......
I forgot
   0.268 agent.focus.chunk stop
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_forget2.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.DM.error False
   0.000 agent.DM.busy False
   0.000 agent.DM.latency 0.05
   0.000 agent.DM.threshold 25
   0.000 agent.DM.maximum_time 10.0
   0.000 agent.DM.record_all_chunks False
   0.000 agent.DMbuffer.chunk None
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk object:cheese task:sandwich
   0.050 agent.production cheese
   0.100 agent.production None
I have put cheese on the bread
   0.100 agent.focus.chunk object:ham task:sandwich
   0.100 agent.production ham
   0.150 agent.production None
I have put  ham on the cheese
   0.150 agent.focus.chunk object:condiment task:sandwich
   0.150 agent.production condiment_DM_request
   0.200 agent.production None
recalling the condiment
   0.200 agent.DM.busy True
   0.200 agent.focus.chunk task:recall
   0.200 agent.DM.error True
   0.200 agent.DMbuffer.chunk None
   0.200 agent.DM.busy False
   0.200 agent.production forgot
   0.250 agent.production None
I recall they wanted.......
I forgot
   0.250 agent.focus.chunk stop
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_forget2.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.DM.error False
   0.000 agent.DM.busy False
   0.000 agent.DM.latency 0.05
   0.000 agent.DM.threshold 25
   0.000 agent.DM.maximum_time 10.0
   0.000 agent.DM.record_all_chunks False
   0.000 agent.DMbuffer.chunk None
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk object:cheese task:sandwich
   0.050 agent.production cheese
   0.100 agent.production None
I have put cheese on the bread
   0.100 agent.focus.chunk object:ham task:sandwich
   0.100 agent.production ham
   0.150 agent.production None
I have put  ham on the cheese
   0.150 agent.focus.chunk object:condiment task:sandwich
   0.150 agent.production condiment_DM_request
   0.200 agent.production None
recalling the condiment
   0.200 agent.DM.busy True
   0.200 agent.focus.chunk task:recall
   0.200 agent.DM.error True
   0.200 agent.DMbuffer.chunk None
   0.200 agent.DM.busy False
   0.200 agent.production forgot
   0.250 agent.production None
I recall they wanted.......
I forgot
   0.250 agent.focus.chunk stop
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_forget2.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.DM.error False
   0.000 agent.DM.busy False
   0.000 agent.DM.latency 0.05
   0.000 agent.DM.threshold 25
   0.000 agent.DM.maximum_time 10.0
   0.000 agent.DM.record_all_chunks False
   0.000 agent.DMbuffer.chunk None
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk object:cheese task:sandwich
   0.050 agent.production cheese
   0.100 agent.production None
I have put cheese on the bread
   0.100 agent.focus.chunk object:ham task:sandwich
   0.100 agent.production ham
   0.150 agent.production None
I have put  ham on the cheese
   0.150 agent.focus.chunk object:condiment task:sandwich
   0.150 agent.production condiment_DM_request
   0.200 agent.production None
recalling the condiment
   0.200 agent.DM.busy True
   0.200 agent.focus.chunk task:recall
   0.200 agent.DM.error True
   0.200 agent.DMbuffer.chunk None
   0.200 agent.DM.busy False
   0.200 agent.production forgot
   0.250 agent.production None
I recall they wanted.......
I forgot
   0.250 agent.focus.chunk stop
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_forget2.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.DM.error False
   0.000 agent.DM.busy False
   0.000 agent.DM.latency 0.05
   0.000 agent.DM.threshold 25
   0.000 agent.DM.maximum_time 10.0
   0.000 agent.DM.record_all_chunks False
   0.000 agent.DMbuffer.chunk None
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk object:cheese task:sandwich
   0.050 agent.production cheese
   0.100 agent.production None
I have put cheese on the bread
   0.100 agent.focus.chunk object:ham task:sandwich
   0.100 agent.production ham
   0.150 agent.production None
I have put  ham on the cheese
   0.150 agent.focus.chunk object:condiment task:sandwich
   0.150 agent.production condiment_DM_request
   0.200 agent.production None
recalling the condiment
   0.200 agent.DM.busy True
   0.200 agent.focus.chunk task:recall
   0.200 agent.DM.error True
   0.200 agent.DMbuffer.chunk None
   0.200 agent.DM.busy False
   0.200 agent.production forgot
   0.250 agent.production None
I recall they wanted.......
I forgot
   0.250 agent.focus.chunk stop
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_forget2.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.DM.error False
   0.000 agent.DM.busy False
   0.000 agent.DM.latency 0.05
   0.000 agent.DM.threshold 25
   0.000 agent.DM.maximum_time 10.0
   0.000 agent.DM.record_all_chunks False
   0.000 agent.DMbuffer.chunk None
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk object:cheese task:sandwich
   0.050 agent.production cheese
   0.100 agent.production None
I have put cheese on the bread
   0.100 agent.focus.chunk object:ham task:sandwich
   0.100 agent.production ham
   0.150 agent.production None
I have put  ham on the cheese
   0.150 agent.focus.chunk object:condiment task:sandwich
   0.150 agent.production condiment_DM_request
   0.200 agent.production None
recalling the condiment
   0.200 agent.DM.busy True
   0.200 agent.focus.chunk task:recall
   0.200 agent.DM.error True
   0.200 agent.DMbuffer.chunk None
   0.200 agent.DM.busy False
   0.200 agent.production forgot
   0.250 agent.production None
I recall they wanted.......
I forgot
   0.250 agent.focus.chunk stop
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_forget2.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.DM.error False
   0.000 agent.DM.busy False
   0.000 agent.DM.latency 0.05
   0.000 agent.DM.threshold 25
   0.000 agent.DM.maximum_time 10.0
   0.000 agent.DM.record_all_chunks False
   0.000 agent.DMbuffer.chunk None
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk object:cheese task:sandwich
   0.050 agent.production cheese
   0.100 agent.production None
I have put cheese on the bread
   0.100 agent.focus.chunk object:ham task:sandwich
   0.100 agent.production ham
   0.150 agent.production None
I have put  ham on the cheese
   0.150 agent.focus.chunk object:condiment task:sandwich
   0.150 agent.production condiment_DM_request
   0.200 agent.production None
recalling the condiment
   0.200 agent.DM.busy True
   0.200 agent.focus.chunk task:recall
   0.200 agent.DM.error True
   0.200 agent.DMbuffer.chunk None
   0.200 agent.DM.busy False
   0.200 agent.production forgot
   0.250 agent.production None
I recall they wanted.......
I forgot
   0.250 agent.focus.chunk stop
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_forget2.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.DM.error False
   0.000 agent.DM.busy False
   0.000 agent.DM.latency 0.05
   0.000 agent.DM.threshold 25
   0.000 agent.DM.maximum_time 10.0
   0.000 agent.DM.record_all_chunks False
   0.000 agent.DMbuffer.chunk None
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk object:cheese task:sandwich
   0.050 agent.production cheese
   0.100 agent.production None
I have put cheese on the bread
   0.100 agent.focus.chunk object:ham task:sandwich
   0.100 agent.production ham
   0.150 agent.production None
I have put  ham on the cheese
   0.150 agent.focus.chunk object:condiment task:sandwich
   0.150 agent.production condiment_DM_request
   0.200 agent.production None
recalling the condiment
   0.200 agent.DM.busy True
   0.200 agent.focus.chunk task:recall
   0.200 agent.DM.error True
   0.200 agent.DMbuffer.chunk None
   0.200 agent.DM.busy False
   0.200 agent.production forgot
   0.250 agent.production None
I recall they wanted.......
I forgot
   0.250 agent.focus.chunk stop
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_forget2.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.DM.error False
   0.000 agent.DM.busy False
   0.000 agent.DM.latency 0.05
   0.000 agent.DM.threshold 25
   0.000 agent.DM.maximum_time 10.0
   0.000 agent.DM.record_all_chunks False
   0.000 agent.DMbuffer.chunk None
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk object:cheese task:sandwich
   0.050 agent.production cheese
   0.100 agent.production None
I have put cheese on the bread
   0.100 agent.focus.chunk object:ham task:sandwich
   0.100 agent.production ham
   0.150 agent.production None
I have put  ham on the cheese
   0.150 agent.focus.chunk object:condiment task:sandwich
   0.150 agent.production condiment_DM_request
   0.200 agent.production None
recalling the condiment
   0.200 agent.DM.busy True
   0.200 agent.focus.chunk task:recall
   0.200 agent.DM.error True
   0.200 agent.DMbuffer.chunk None
   0.200 agent.DM.busy False
   0.200 agent.production forgot
   0.250 agent.production None
I recall they wanted.......
I forgot
   0.250 agent.focus.chunk stop
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_forget2.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.DM.error False
   0.000 agent.DM.busy False
   0.000 agent.DM.latency 0.05
   0.000 agent.DM.threshold 25
   0.000 agent.DM.maximum_time 10.0
   0.000 agent.DM.record_all_chunks False
   0.000 agent.DMbuffer.chunk None
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk object:cheese task:sandwich
   0.050 agent.production cheese
   0.100 agent.production None
I have put cheese on the bread
   0.100 agent.focus.chunk object:ham task:sandwich
   0.100 agent.production ham
   0.150 agent.production None
I have put  ham on the cheese
   0.150 agent.focus.chunk object:condiment task:sandwich
   0.150 agent.production condiment_DM_request
   0.200 agent.production None
recalling the condiment
   0.200 agent.DM.busy True
   0.200 agent.focus.chunk task:recall
   0.200 agent.DM.error True
   0.200 agent.DMbuffer.chunk None
   0.200 agent.DM.busy False
   0.200 agent.production forgot
   0.250 agent.production None
I recall they wanted.......
I forgot
   0.250 agent.focus.chunk stop
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_forget2.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.DM.error False
   0.000 agent.DM.busy False
   0.000 agent.DM.latency 0.05
   0.000 agent.DM.threshold 25
   0.000 agent.DM.maximum_time 10.0
   0.000 agent.DM.record_all_chunks False
   0.000 agent.DMbuffer.chunk None
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk object:cheese task:sandwich
   0.050 agent.production cheese
   0.100 agent.production None
I have put cheese on the bread
   0.100 agent.focus.chunk object:ham task:sandwich
   0.100 agent.production ham
   0.150 agent.production None
I have put  ham on the cheese
   0.150 agent.focus.chunk object:condiment task:sandwich
   0.150 agent.production condiment_DM_request
   0.200 agent.production None
recalling the condiment
   0.200 agent.DM.busy True
   0.200 agent.focus.chunk task:recall
   0.200 agent.DM.error True
   0.200 agent.DMbuffer.chunk None
   0.200 agent.DM.busy False
   0.200 agent.production forgot
   0.250 agent.production None
I recall they wanted.......
I forgot
   0.250 agent.focus.chunk stop
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_forget2.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.DM.error False
   0.000 agent.DM.busy False
   0.000 agent.DM.latency 0.05
   0.000 agent.DM.threshold 25
   0.000 agent.DM.maximum_time 10.0
   0.000 agent.DM.record_all_chunks False
   0.000 agent.DMbuffer.chunk None
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk object:cheese task:sandwich
   0.050 agent.production cheese
   0.100 agent.production None
I have put cheese on the bread
   0.100 agent.focus.chunk object:ham task:sandwich
   0.100 agent.production ham
   0.150 agent.production None
I have put  ham on the cheese
   0.150 agent.focus.chunk object:condiment task:sandwich
   0.150 agent.production condiment_DM_request
   0.200 agent.production None
recalling the condiment
   0.200 agent.DM.busy True
   0.200 agent.focus.chunk task:recall
   0.200 agent.DM.error True
   0.200 agent.DMbuffer.chunk None
   0.200 agent.DM.busy False
   0.200 agent.production forgot
   0.250 agent.production None
I recall they wanted.......
I forgot
   0.250 agent.focus.chunk stop
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_forget2.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.DM.error False
   0.000 agent.DM.busy False
   0.000 agent.DM.latency 0.05
   0.000 agent.DM.threshold 25
   0.000 agent.DM.maximum_time 10.0
   0.000 agent.DM.record_all_chunks False
   0.000 agent.DMbuffer.chunk None
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk object:cheese task:sandwich
   0.050 agent.production cheese
   0.100 agent.production None
I have put cheese on the bread
   0.100 agent.focus.chunk object:ham task:sandwich
   0.100 agent.production ham
   0.150 agent.production None
I have put  ham on the cheese
   0.150 agent.focus.chunk object:condiment task:sandwich
   0.150 agent.production condiment_DM_request
   0.200 agent.production None
recalling the condiment
   0.200 agent.DM.busy True
   0.200 agent.focus.chunk task:recall
   0.200 agent.DM.error True
   0.200 agent.DMbuffer.chunk None
   0.200 agent.DM.busy False
   0.200 agent.production forgot
   0.250 agent.production None
I recall they wanted.......
I forgot
   0.250 agent.focus.chunk stop
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_forget2.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.DM.error False
   0.000 agent.DM.busy False
   0.000 agent.DM.latency 0.05
   0.000 agent.DM.threshold 25
   0.000 agent.DM.maximum_time 10.0
   0.000 agent.DM.record_all_chunks False
   0.000 agent.DMbuffer.chunk None
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk object:cheese task:sandwich
   0.050 agent.production cheese
   0.100 agent.production None
I have put cheese on the bread
   0.100 agent.focus.chunk object:ham task:sandwich
   0.100 agent.production ham
   0.150 agent.production None
I have put  ham on the cheese
   0.150 agent.focus.chunk object:condiment task:sandwich
   0.150 agent.production condiment_DM_request
   0.200 agent.production None
recalling the condiment
   0.200 agent.DM.busy True
   0.200 agent.focus.chunk task:recall
   0.200 agent.DM.error True
   0.200 agent.DMbuffer.chunk None
   0.200 agent.DM.busy False
   0.200 agent.production forgot
   0.250 agent.production None
I recall they wanted.......
I forgot
   0.250 agent.focus.chunk stop
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_forget2.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.DM.error False
   0.000 agent.DM.busy False
   0.000 agent.DM.latency 0.05
   0.000 agent.DM.threshold 25
   0.000 agent.DM.maximum_time 10.0
   0.000 agent.DM.record_all_chunks False
   0.000 agent.DMbuffer.chunk None
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk object:cheese task:sandwich
   0.050 agent.production cheese
   0.100 agent.production None
I have put cheese on the bread
   0.100 agent.focus.chunk object:ham task:sandwich
   0.100 agent.production ham
   0.150 agent.production None
I have put  ham on the cheese
   0.150 agent.focus.chunk object:condiment task:sandwich
   0.150 agent.production condiment_DM_request
   0.200 agent.production None
recalling the condiment
   0.200 agent.DM.busy True
   0.200 agent.focus.chunk task:recall
   0.200 agent.DM.error True
   0.200 agent.DMbuffer.chunk None
   0.200 agent.DM.busy False
   0.200 agent.production forgot
   0.250 agent.production None
I recall they wanted.......
I forgot
   0.250 agent.focus.chunk stop
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_forget2.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.DM.error False
   0.000 agent.DM.busy False
   0.000 agent.DM.latency 0.05
   0.000 agent.DM.threshold 25
   0.000 agent.DM.maximum_time 10.0
   0.000 agent.DM.record_all_chunks False
   0.000 agent.DMbuffer.chunk None
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk object:cheese task:sandwich
   0.050 agent.production cheese
   0.100 agent.production None
I have put cheese on the bread
   0.100 agent.focus.chunk object:ham task:sandwich
   0.100 agent.production ham
   0.150 agent.production None
I have put  ham on the cheese
   0.150 agent.focus.chunk object:condiment task:sandwich
   0.150 agent.production condiment_DM_request
   0.200 agent.production None
recalling the condiment
   0.200 agent.DM.busy True
   0.200 agent.focus.chunk task:recall
   0.200 agent.DM.error True
   0.200 agent.DMbuffer.chunk None
   0.200 agent.DM.busy False
   0.200 agent.production forgot
   0.250 agent.production None
I recall they wanted.......
I forgot
   0.250 agent.focus.chunk stop
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_forget2.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.DM.error False
   0.000 agent.DM.busy False
   0.000 agent.DM.latency 0.05
   0.000 agent.DM.threshold 25
   0.000 agent.DM.maximum_time 10.0
   0.000 agent.DM.record_all_chunks False
   0.000 agent.DMbuffer.chunk None
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk object:cheese task:sandwich
   0.050 agent.production cheese
   0.100 agent.production None
I have put cheese on the bread
   0.100 agent.focus.chunk object:ham task:sandwich
   0.100 agent.production ham
   0.150 agent.production None
I have put  ham on the cheese
   0.150 agent.focus.chunk object:condiment task:sandwich
   0.150 agent.production condiment_DM_request
   0.200 agent.production None
recalling the condiment
   0.200 agent.DM.busy True
   0.200 agent.focus.chunk task:recall
   0.200 agent.DM.error True
   0.200 agent.DMbuffer.chunk None
   0.200 agent.DM.busy False
   0.200 agent.production forgot
   0.250 agent.production None
I recall they wanted.......
I forgot
   0.250 agent.focus.chunk stop
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_forget2.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.DM.error False
   0.000 agent.DM.busy False
   0.000 agent.DM.latency 0.05
   0.000 agent.DM.threshold 25
   0.000 agent.DM.maximum_time 10.0
   0.000 agent.DM.record_all_chunks False
   0.000 agent.DMbuffer.chunk None
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk object:cheese task:sandwich
   0.050 agent.production cheese
   0.100 agent.production None
I have put cheese on the bread
   0.100 agent.focus.chunk object:ham task:sandwich
   0.100 agent.production ham
   0.150 agent.production None
I have put  ham on the cheese
   0.150 agent.focus.chunk object:condiment task:sandwich
   0.150 agent.production condiment_DM_request
   0.200 agent.production None
recalling the condiment
   0.200 agent.DM.busy True
   0.200 agent.focus.chunk task:recall
   0.200 agent.DM.error True
   0.200 agent.DMbuffer.chunk None
   0.200 agent.DM.busy False
   0.200 agent.production forgot
   0.250 agent.production None
I recall they wanted.......
I forgot
   0.250 agent.focus.chunk stop
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_forget2.py
Traceback (most recent call last):
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_forget2.py", line 8, in <module>
    class MyAgent(ACTR):
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_forget2.py", line 13, in MyAgent
    DM=Memory(DMbuffer,latency=0.05,threshold=-s25,finst_size=10,finst_time=30.0)
NameError: name 's25' is not defined
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_forget2.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.DM.error False
   0.000 agent.DM.busy False
   0.000 agent.DM.latency 0.05
   0.000 agent.DM.threshold -25
   0.000 agent.DM.maximum_time 10.0
   0.000 agent.DM.record_all_chunks False
   0.000 agent.DMbuffer.chunk None
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk object:cheese task:sandwich
   0.050 agent.production cheese
   0.100 agent.production None
I have put cheese on the bread
   0.100 agent.focus.chunk object:ham task:sandwich
   0.100 agent.production ham
   0.150 agent.production None
I have put  ham on the cheese
   0.150 agent.focus.chunk object:condiment task:sandwich
   0.150 agent.production condiment_DM_request
   0.200 agent.production None
recalling the condiment
   0.200 agent.DM.busy True
   0.200 agent.focus.chunk task:recall
   0.201 agent.DMbuffer.chunk condiment:mustard
   0.201 agent.DM.busy False
   0.201 agent.production DM_retrieve
   0.251 agent.production None
I recall they wanted....
mustard
   0.251 agent.DM.busy True
   0.251 agent.DMbuffer.chunk state:empty
   0.251 agent.focus.chunk object:bread_top task:sandwich
   0.251 agent.production bread_top
   0.253 agent.DMbuffer.chunk condiment:mustard
   0.253 agent.DM.busy False
   0.301 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   0.301 agent.focus.chunk sandwich_step:stop
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_forget2.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.DM.error False
   0.000 agent.DM.busy False
   0.000 agent.DM.latency 0.05
   0.000 agent.DM.threshold -25
   0.000 agent.DM.maximum_time 10.0
   0.000 agent.DM.record_all_chunks False
   0.000 agent.DMbuffer.chunk None
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk object:cheese task:sandwich
   0.050 agent.production cheese
   0.100 agent.production None
I have put cheese on the bread
   0.100 agent.focus.chunk object:ham task:sandwich
   0.100 agent.production ham
   0.150 agent.production None
I have put  ham on the cheese
   0.150 agent.focus.chunk object:condiment task:sandwich
   0.150 agent.production condiment_DM_request
   0.200 agent.production None
recalling the condiment
   0.200 agent.DM.busy True
   0.200 agent.focus.chunk task:recall
   0.242 agent.DMbuffer.chunk condiment:mustard
   0.242 agent.DM.busy False
   0.242 agent.production DM_retrieve
   0.292 agent.production None
I recall they wanted....
mustard
   0.292 agent.DM.busy True
   0.292 agent.DMbuffer.chunk state:empty
   0.292 agent.focus.chunk object:bread_top task:sandwich
   0.292 agent.production bread_top
   0.303 agent.DMbuffer.chunk condiment:mustard
   0.303 agent.DM.busy False
   0.342 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   0.342 agent.focus.chunk sandwich_step:stop
>>> 