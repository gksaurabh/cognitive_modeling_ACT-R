Python 3.9.5 (v3.9.5:0a7dcbdb13, May  3 2021, 13:17:02) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/a11.py
Traceback (most recent call last):
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/a11.py", line 4, in <module>
    class MyEnvironment(ccm.Model):
NameError: name 'ccm' is not defined
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/a11.py
Traceback (most recent call last):
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/a11.py", line 4, in <module>
    class MyEnvironment(Model):
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/a11.py", line 5, in MyEnvironment
    something=ccm.Model(isa='something',state='not_done')
NameError: name 'ccm' is not defined
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/a11.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.DM.error False
   0.000 agent.DM.busy False
   0.000 agent.DM.latency 0.05
   0.000 agent.DM.threshold 0
   0.000 agent.DM.maximum_time 10.0
   0.000 agent.DM.record_all_chunks False
   0.000 agent.DMbuffer.chunk None
   0.000 something.isa something
   0.000 something.state not_done
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk goal:sandwich object:cheese
   0.050 agent.production cheese
   0.100 agent.production None
I have put cheese on the bread
   0.100 agent.focus.chunk goal:sandwich object:ham
   0.100 agent.production ham
   0.150 agent.production None
I have put  ham on the cheese
   0.150 agent.focus.chunk action:recall_condiment goal:sandwich
   0.150 agent.production recall_condiment
   0.200 agent.production None
recalling the order
   0.200 agent.DM.busy True
   0.200 agent.focus.chunk goal:sandwich object:condiment
   0.218 agent.DMbuffer.chunk condiment:ketchup
   0.218 agent.DM.busy False
   0.218 agent.production condiment
   0.268 agent.production None
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
   0.268 agent.focus.chunk goal:sandwich object:bread_top
   0.268 agent.production bread_top
   0.318 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   0.318 agent.focus.chunk sandwich_step:stop
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/a11.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.DM.error False
   0.000 agent.DM.busy False
   0.000 agent.DM.latency 0.05
   0.000 agent.DM.threshold 0
   0.000 agent.DM.maximum_time 10.0
   0.000 agent.DM.record_all_chunks False
   0.000 agent.DMbuffer.chunk None
   0.000 something.isa something
   0.000 something.state not_done
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk goal:sandwich object:cheese
   0.050 agent.production cheese
   0.100 agent.production None
I have put cheese on the bread
   0.100 agent.focus.chunk goal:sandwich object:ham
doing something
   2.100 something.state done
   2.100 agent.production ham
   2.150 agent.production None
reset doing something
   2.150 something.state not_done
I have put  ham on the cheese
   2.150 agent.focus.chunk action:recall_condiment goal:sandwich
   2.150 agent.production recall_condiment
   2.200 agent.production None
recalling the order
   2.200 agent.DM.busy True
   2.200 agent.focus.chunk goal:sandwich object:condiment
   2.218 agent.DMbuffer.chunk condiment:ketchup
   2.218 agent.DM.busy False
   2.218 agent.production condiment
   2.268 agent.production None
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
   2.268 agent.focus.chunk goal:sandwich object:bread_top
   2.268 agent.production bread_top
   2.318 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   2.318 agent.focus.chunk sandwich_step:stop
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/a11.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.DM.error False
   0.000 agent.DM.busy False
   0.000 agent.DM.latency 0.05
   0.000 agent.DM.threshold 0
   0.000 agent.DM.maximum_time 10.0
   0.000 agent.DM.record_all_chunks False
   0.000 agent.DMbuffer.chunk None
   0.000 something.isa something
   0.000 something.state not_done
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk goal:sandwich object:cheese
   0.050 agent.production cheese
   0.100 agent.production None
I have put cheese on the bread
   0.100 agent.focus.chunk goal:sandwich object:ham
doing something
   2.100 something.state done
   2.100 agent.production ham
   2.150 agent.production None
reset doing something
   2.150 something.state not_done
I have put  ham on the cheese
   2.150 agent.focus.chunk action:recall_condiment goal:sandwich
   2.150 agent.production recall_condiment
   2.200 agent.production None
recalling the order
   2.200 agent.DM.busy True
   2.200 agent.focus.chunk goal:sandwich object:condiment
   2.210 agent.DMbuffer.chunk condiment:mustard customer:lary
   2.210 agent.DM.busy False
   2.210 agent.production condiment
   2.260 agent.production None
I recall they wanted.......
mustard
i have put the condiment on the sandwich
   2.260 agent.focus.chunk goal:sandwich object:bread_top
doing something
   4.260 something.state done
   4.260 agent.production bread_top
   4.310 agent.production None
reset doing something
   4.310 something.state not_done
I have put bread on the ham
I have made a ham and cheese sandwich
   4.310 agent.focus.chunk sandwich_step:stop
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_spreadingactivation.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.DM.error False
   0.000 agent.DM.busy False
   0.000 agent.DM.latency 0.05
   0.000 agent.DM.threshold 0
   0.000 agent.DM.maximum_time 10.0
   0.000 agent.DM.record_all_chunks False
   0.000 agent.DMbuffer.chunk None
   0.000 something.isa something
   0.000 something.state not_done
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk object:cheese task:sandwich
doing somethiing
   2.050 something.state done
   2.050 agent.production cheese
   2.100 agent.production None
I have put cheese on the bread
   2.100 agent.focus.chunk object:ham task:sandwich
doing reset
   2.100 something.state not_done
doing somethiing
   4.100 something.state done
   4.100 agent.production ham
   4.150 agent.production None
I have put  ham on the cheese
   4.150 agent.focus.chunk customer:very_tall_male object:condiment
   4.150 agent.focus.chunk customer:very_tall_female object:condiment
   4.150 agent.production condiment_DM_request
   4.200 agent.production None
recalling the condiment
   4.200 agent.DM.busy True
   4.200 agent.focus.chunk task:recall
   4.234 agent.DMbuffer.chunk condiment:chipotle customer:very_tall_female
   4.234 agent.DM.busy False
   4.234 agent.production DM_retrieve
   4.284 agent.production None
I recall they wanted.......
chipotle
   4.284 agent.DMbuffer.chunk state:empty
   4.284 agent.focus.chunk object:bread_top task:sandwich
   4.284 agent.production bread_top
   4.334 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   4.334 agent.focus.chunk object:none task:sandwich
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_spreadingactivation.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.DM.error False
   0.000 agent.DM.busy False
   0.000 agent.DM.latency 0.05
   0.000 agent.DM.threshold 0
   0.000 agent.DM.maximum_time 10.0
   0.000 agent.DM.record_all_chunks False
   0.000 agent.DMbuffer.chunk None
   0.000 something.isa something
   0.000 something.state not_done
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk object:cheese task:sandwich
doing somethiing
   2.050 something.state done
   2.050 agent.production cheese
   2.100 agent.production None
I have put cheese on the bread
   2.100 agent.focus.chunk object:ham task:sandwich
doing reset
   2.100 something.state not_done
doing somethiing
   4.100 something.state done
   4.100 agent.production ham
   4.150 agent.production None
I have put  ham on the cheese
   4.150 agent.focus.chunk customer:very_tall_male object:condiment
   4.150 agent.focus.chunk customer:very_tall_female object:condiment
   4.150 agent.production condiment_DM_request
   4.200 agent.production None
recalling the condiment
   4.200 agent.DM.busy True
   4.200 agent.focus.chunk task:recall
   4.238 agent.DMbuffer.chunk condiment:chipotle customer:very_tall_female
   4.238 agent.DM.busy False
   4.238 agent.production DM_retrieve
   4.288 agent.production None
I recall they wanted.......
chipotle
   4.288 agent.DMbuffer.chunk state:empty
   4.288 agent.focus.chunk object:bread_top task:sandwich
   4.288 agent.production bread_top
   4.338 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   4.338 agent.focus.chunk object:none task:sandwich
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_spreadingactivation.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.DM.error False
   0.000 agent.DM.busy False
   0.000 agent.DM.latency 0.05
   0.000 agent.DM.threshold 0
   0.000 agent.DM.maximum_time 10.0
   0.000 agent.DM.record_all_chunks False
   0.000 agent.DMbuffer.chunk None
   0.000 something.isa something
   0.000 something.state not_done
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk object:cheese task:sandwich
doing somethiing
   2.050 something.state done
   2.050 agent.production cheese
   2.100 agent.production None
I have put cheese on the bread
   2.100 agent.focus.chunk object:ham task:sandwich
doing reset
   2.100 something.state not_done
doing somethiing
   4.100 something.state done
   4.100 agent.production ham
   4.150 agent.production None
I have put  ham on the cheese
   4.150 agent.focus.chunk customer:very_tall_male object:condiment
   4.150 agent.focus.chunk customer:very_tall_female object:condiment
   4.150 agent.production condiment_DM_request
   4.200 agent.production None
recalling the condiment
   4.200 agent.DM.busy True
   4.200 agent.focus.chunk task:recall
   4.225 agent.DMbuffer.chunk condiment:chipotle customer:very_tall_female
   4.225 agent.DM.busy False
   4.225 agent.production DM_retrieve
   4.275 agent.production None
I recall they wanted.......
chipotle
   4.275 agent.DMbuffer.chunk state:empty
   4.275 agent.focus.chunk object:bread_top task:sandwich
   4.275 agent.production bread_top
   4.325 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   4.325 agent.focus.chunk object:none task:sandwich
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_spreadingactivation.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.DM.error False
   0.000 agent.DM.busy False
   0.000 agent.DM.latency 0.05
   0.000 agent.DM.threshold 0
   0.000 agent.DM.maximum_time 10.0
   0.000 agent.DM.record_all_chunks False
   0.000 agent.DMbuffer.chunk None
   0.000 something.isa something
   0.000 something.state not_done
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk object:cheese task:sandwich
doing somethiing
   2.050 something.state done
   2.050 agent.production cheese
   2.100 agent.production None
I have put cheese on the bread
   2.100 agent.focus.chunk object:ham task:sandwich
doing reset
   2.100 something.state not_done
doing somethiing
   4.100 something.state done
   4.100 agent.production ham
   4.150 agent.production None
I have put  ham on the cheese
   4.150 agent.focus.chunk customer:very_tall_male object:condiment
   4.150 agent.focus.chunk customer:very_tall_female object:condiment
   4.150 agent.production condiment_DM_request
   4.200 agent.production None
recalling the condiment
   4.200 agent.DM.busy True
   4.200 agent.focus.chunk task:recall
   4.229 agent.DMbuffer.chunk condiment:chipotle customer:very_tall_female
   4.229 agent.DM.busy False
   4.229 agent.production DM_retrieve
   4.279 agent.production None
I recall they wanted.......
chipotle
   4.279 agent.DMbuffer.chunk state:empty
   4.279 agent.focus.chunk object:bread_top task:sandwich
   4.279 agent.production bread_top
   4.329 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   4.329 agent.focus.chunk object:none task:sandwich
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_spreadingactivation.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.DM.error False
   0.000 agent.DM.busy False
   0.000 agent.DM.latency 0.05
   0.000 agent.DM.threshold 0
   0.000 agent.DM.maximum_time 10.0
   0.000 agent.DM.record_all_chunks False
   0.000 agent.DMbuffer.chunk None
   0.000 something.isa something
   0.000 something.state not_done
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk object:cheese task:sandwich
doing somethiing
   2.050 something.state done
   2.050 agent.production cheese
   2.100 agent.production None
I have put cheese on the bread
   2.100 agent.focus.chunk object:ham task:sandwich
doing reset
   2.100 something.state not_done
doing somethiing
   4.100 something.state done
   4.100 agent.production ham
   4.150 agent.production None
I have put  ham on the cheese
   4.150 agent.focus.chunk customer:very_tall_male object:condiment
   4.150 agent.focus.chunk customer:very_tall_female object:condiment
   4.150 agent.production condiment_DM_request
   4.200 agent.production None
recalling the condiment
   4.200 agent.DM.busy True
   4.200 agent.focus.chunk task:recall
   4.219 agent.DMbuffer.chunk condiment:chipotle customer:very_tall_female
   4.219 agent.DM.busy False
   4.219 agent.production DM_retrieve
   4.269 agent.production None
I recall they wanted.......
chipotle
   4.269 agent.DMbuffer.chunk state:empty
   4.269 agent.focus.chunk object:bread_top task:sandwich
   4.269 agent.production bread_top
   4.319 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   4.319 agent.focus.chunk object:none task:sandwich
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_spreadingactivation.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.DM.error False
   0.000 agent.DM.busy False
   0.000 agent.DM.latency 0.05
   0.000 agent.DM.threshold 0
   0.000 agent.DM.maximum_time 10.0
   0.000 agent.DM.record_all_chunks False
   0.000 agent.DMbuffer.chunk None
   0.000 something.isa something
   0.000 something.state not_done
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk object:cheese task:sandwich
doing somethiing
   2.050 something.state done
   2.050 agent.production cheese
   2.100 agent.production None
I have put cheese on the bread
   2.100 agent.focus.chunk object:ham task:sandwich
doing reset
   2.100 something.state not_done
doing somethiing
   4.100 something.state done
   4.100 agent.production ham
   4.150 agent.production None
I have put  ham on the cheese
   4.150 agent.focus.chunk customer:very_tall_male object:condiment
   4.150 agent.focus.chunk customer:very_tall_female object:condiment
   4.150 agent.production condiment_DM_request
   4.200 agent.production None
recalling the condiment
   4.200 agent.DM.busy True
   4.200 agent.focus.chunk task:recall
   4.250 agent.DM.error True
   4.250 agent.DMbuffer.chunk None
   4.250 agent.DM.busy False
   4.250 agent.production forgot
   4.300 agent.production None
I recall they wanted.......
I forgot
   4.300 agent.focus.chunk object:none task:sandwich
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_spreadingactivation.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.DM.error False
   0.000 agent.DM.busy False
   0.000 agent.DM.latency 0.05
   0.000 agent.DM.threshold 0
   0.000 agent.DM.maximum_time 10.0
   0.000 agent.DM.record_all_chunks False
   0.000 agent.DMbuffer.chunk None
   0.000 something.isa something
   0.000 something.state not_done
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk object:cheese task:sandwich
doing somethiing
   2.050 something.state done
   2.050 agent.production cheese
   2.100 agent.production None
I have put cheese on the bread
   2.100 agent.focus.chunk object:ham task:sandwich
doing reset
   2.100 something.state not_done
doing somethiing
   4.100 something.state done
   4.100 agent.production ham
   4.150 agent.production None
I have put  ham on the cheese
   4.150 agent.focus.chunk customer:very_tall_male object:condiment
   4.150 agent.focus.chunk customer:very_tall_female object:condiment
   4.150 agent.production condiment_DM_request
   4.200 agent.production None
recalling the condiment
   4.200 agent.DM.busy True
   4.200 agent.focus.chunk task:recall
   4.219 agent.DMbuffer.chunk condiment:chipotle customer:very_tall_female
   4.219 agent.DM.busy False
   4.219 agent.production DM_retrieve
   4.269 agent.production None
I recall they wanted.......
chipotle
   4.269 agent.DMbuffer.chunk state:empty
   4.269 agent.focus.chunk object:bread_top task:sandwich
   4.269 agent.production bread_top
   4.319 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   4.319 agent.focus.chunk object:none task:sandwich
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_spreadingactivation.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.DM.error False
   0.000 agent.DM.busy False
   0.000 agent.DM.latency 0.05
   0.000 agent.DM.threshold 0
   0.000 agent.DM.maximum_time 10.0
   0.000 agent.DM.record_all_chunks False
   0.000 agent.DMbuffer.chunk None
   0.000 something.isa something
   0.000 something.state not_done
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk object:cheese task:sandwich
doing somethiing
   2.050 something.state done
   2.050 agent.production cheese
   2.100 agent.production None
I have put cheese on the bread
   2.100 agent.focus.chunk object:ham task:sandwich
doing reset
   2.100 something.state not_done
doing somethiing
   4.100 something.state done
   4.100 agent.production ham
   4.150 agent.production None
I have put  ham on the cheese
   4.150 agent.focus.chunk customer:very_tall_male object:condiment
   4.150 agent.focus.chunk customer:very_tall_female object:condiment
   4.150 agent.production condiment_DM_request
   4.200 agent.production None
recalling the condiment
   4.200 agent.DM.busy True
   4.200 agent.focus.chunk task:recall
   4.224 agent.DMbuffer.chunk condiment:chipotle customer:very_tall_female
   4.224 agent.DM.busy False
   4.224 agent.production DM_retrieve
   4.274 agent.production None
I recall they wanted.......
chipotle
   4.274 agent.DMbuffer.chunk state:empty
   4.274 agent.focus.chunk object:bread_top task:sandwich
   4.274 agent.production bread_top
   4.324 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   4.324 agent.focus.chunk object:none task:sandwich
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_spreadingactivation.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.DM.error False
   0.000 agent.DM.busy False
   0.000 agent.DM.latency 0.05
   0.000 agent.DM.threshold 0
   0.000 agent.DM.maximum_time 10.0
   0.000 agent.DM.record_all_chunks False
   0.000 agent.DMbuffer.chunk None
   0.000 something.isa something
   0.000 something.state not_done
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk object:cheese task:sandwich
doing somethiing
   2.050 something.state done
   2.050 agent.production cheese
   2.100 agent.production None
I have put cheese on the bread
   2.100 agent.focus.chunk object:ham task:sandwich
doing reset
   2.100 something.state not_done
doing somethiing
   4.100 something.state done
   4.100 agent.production ham
   4.150 agent.production None
I have put  ham on the cheese
   4.150 agent.focus.chunk customer:very_tall_male object:condiment
   4.150 agent.focus.chunk customer:very_tall_female object:condiment
   4.150 agent.production condiment_DM_request
   4.200 agent.production None
recalling the condiment
   4.200 agent.DM.busy True
   4.200 agent.focus.chunk task:recall
   4.229 agent.DMbuffer.chunk condiment:chipotle customer:very_tall_female
   4.229 agent.DM.busy False
   4.229 agent.production DM_retrieve
   4.279 agent.production None
I recall they wanted.......
chipotle
   4.279 agent.DMbuffer.chunk state:empty
   4.279 agent.focus.chunk object:bread_top task:sandwich
   4.279 agent.production bread_top
   4.329 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   4.329 agent.focus.chunk object:none task:sandwich
>>> 