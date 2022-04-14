Python 3.9.5 (v3.9.5:0a7dcbdb13, May  3 2021, 13:17:02) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_partialmatching.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.DM.error False
   0.000 agent.DM.busy False
   0.000 agent.DM.latency 0.05
   0.000 agent.DM.threshold -15
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
   0.050 something.state done
   0.050 agent.production cheese
   0.100 agent.production None
I have put cheese on the bread
   0.100 agent.focus.chunk object:ham task:sandwich
doing reset
   0.100 something.state not_done
doing somethiing
   0.100 something.state done
   0.100 agent.production ham
   0.150 agent.production None
I have put  ham on the cheese
   0.150 agent.focus.chunk customer:mary object:condiment_choice
   0.150 agent.production condiment_DM_request
   0.200 agent.production None
recalling the condiment for...
mary
   0.200 agent.DM.busy True
   0.200 agent.focus.chunk task:recall
   0.216 agent.DMbuffer.chunk condiment:mayonase customer:tony
   0.216 agent.DM.busy False
   0.216 agent.production DM_retrieve
   0.266 agent.production None
I recall they wanted.......
mayonase
   0.266 agent.DMbuffer.chunk state:empty
   0.266 agent.focus.chunk object:bread_top task:sandwich
   0.266 agent.production bread_top
   0.316 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   0.316 agent.focus.chunk object:none task:sandwich
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_partialmatching.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.DM.error False
   0.000 agent.DM.busy False
   0.000 agent.DM.latency 0.05
   0.000 agent.DM.threshold -15
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
   0.050 something.state done
   0.050 agent.production cheese
   0.100 agent.production None
I have put cheese on the bread
   0.100 agent.focus.chunk object:ham task:sandwich
doing reset
   0.100 something.state not_done
doing somethiing
   0.100 something.state done
   0.100 agent.production ham
   0.150 agent.production None
I have put  ham on the cheese
   0.150 agent.focus.chunk customer:mary object:condiment_choice
   0.150 agent.production condiment_DM_request
   0.200 agent.production None
recalling the condiment for...
mary
   0.200 agent.DM.busy True
   0.200 agent.focus.chunk task:recall
   0.227 agent.DMbuffer.chunk condiment:ketchup customer:mary
   0.227 agent.DM.busy False
   0.227 agent.production DM_retrieve
   0.277 agent.production None
I recall they wanted.......
ketchup
   0.277 agent.DMbuffer.chunk state:empty
   0.277 agent.focus.chunk object:bread_top task:sandwich
   0.277 agent.production bread_top
   0.327 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   0.327 agent.focus.chunk object:none task:sandwich
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_utility.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.pm_new.alpha 0.2
   0.000 agent.pm_new.clearFlag False
   0.000 agent.pm_noise.noise 0.1
   0.000 agent.pm_noise.baseNoise 0
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk goal:sandwich object:cheese
   0.050 agent.production cheese
   0.100 agent.production None
I have put cheese on the bread
   0.100 agent.focus.chunk goal:sandwich object:ham
   0.100 agent.production parma_ham
   0.150 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   0.150 agent.focus.chunk goal:sandwich object:bread_top
   0.150 agent.pm_new.clearFlag True
   0.150 agent.pm_new.clearFlag False
   0.150 agent.production bread_top
   0.200 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   0.200 agent.focus.chunk goal:sandwich object:bread_bottom
   0.200 agent.production bread_bottom
   0.250 agent.production None
I have a piece of bread
   0.250 agent.focus.chunk goal:sandwich object:cheese
   0.250 agent.production cheese
   0.300 agent.production None
I have put cheese on the bread
   0.300 agent.focus.chunk goal:sandwich object:ham
   0.300 agent.production parma_ham
   0.350 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   0.350 agent.focus.chunk goal:sandwich object:bread_top
   0.350 agent.pm_new.clearFlag True
   0.350 agent.pm_new.clearFlag False
   0.350 agent.production bread_top
   0.400 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   0.400 agent.focus.chunk goal:sandwich object:bread_bottom
   0.400 agent.production bread_bottom
   0.450 agent.production None
I have a piece of bread
   0.450 agent.focus.chunk goal:sandwich object:cheese
   0.450 agent.production cheese
   0.500 agent.production None
I have put cheese on the bread
   0.500 agent.focus.chunk goal:sandwich object:ham
   0.500 agent.production parma_ham
   0.550 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   0.550 agent.focus.chunk goal:sandwich object:bread_top
   0.550 agent.pm_new.clearFlag True
   0.550 agent.pm_new.clearFlag False
   0.550 agent.production bread_top
   0.600 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   0.600 agent.focus.chunk goal:sandwich object:bread_bottom
   0.600 agent.production bread_bottom
   0.650 agent.production None
I have a piece of bread
   0.650 agent.focus.chunk goal:sandwich object:cheese
   0.650 agent.production cheese
   0.700 agent.production None
I have put cheese on the bread
   0.700 agent.focus.chunk goal:sandwich object:ham
   0.700 agent.production maple_ham
   0.750 agent.production None
I have put maple ham on the cheese
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
   0.750 agent.focus.chunk goal:sandwich object:bread_top
   0.750 agent.pm_new.clearFlag True
   0.750 agent.pm_new.clearFlag False
   0.750 agent.production bread_top
   0.800 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   0.800 agent.focus.chunk goal:sandwich object:bread_bottom
   0.800 agent.production bread_bottom
   0.850 agent.production None
I have a piece of bread
   0.850 agent.focus.chunk goal:sandwich object:cheese
   0.850 agent.production cheese
   0.900 agent.production None
I have put cheese on the bread
   0.900 agent.focus.chunk goal:sandwich object:ham
   0.900 agent.production parma_ham
   0.950 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   0.950 agent.focus.chunk goal:sandwich object:bread_top
   0.950 agent.pm_new.clearFlag True
   0.950 agent.pm_new.clearFlag False
   0.950 agent.production bread_top
   1.000 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   1.000 agent.focus.chunk goal:sandwich object:bread_bottom
   1.000 agent.production bread_bottom
   1.050 agent.production None
I have a piece of bread
   1.050 agent.focus.chunk goal:sandwich object:cheese
   1.050 agent.production cheese
   1.100 agent.production None
I have put cheese on the bread
   1.100 agent.focus.chunk goal:sandwich object:ham
   1.100 agent.production maple_ham
   1.150 agent.production None
I have put maple ham on the cheese
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
   1.150 agent.focus.chunk goal:sandwich object:bread_top
   1.150 agent.pm_new.clearFlag True
   1.150 agent.pm_new.clearFlag False
   1.150 agent.production bread_top
   1.200 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   1.200 agent.focus.chunk goal:sandwich object:bread_bottom
   1.200 agent.production bread_bottom
   1.250 agent.production None
I have a piece of bread
   1.250 agent.focus.chunk goal:sandwich object:cheese
   1.250 agent.production cheese
   1.300 agent.production None
I have put cheese on the bread
   1.300 agent.focus.chunk goal:sandwich object:ham
   1.300 agent.production maple_ham
   1.350 agent.production None
I have put maple ham on the cheese
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
   1.350 agent.focus.chunk goal:sandwich object:bread_top
   1.350 agent.pm_new.clearFlag True
   1.350 agent.pm_new.clearFlag False
   1.350 agent.production bread_top
   1.400 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   1.400 agent.focus.chunk goal:sandwich object:bread_bottom
   1.400 agent.production bread_bottom
   1.450 agent.production None
I have a piece of bread
   1.450 agent.focus.chunk goal:sandwich object:cheese
   1.450 agent.production cheese
   1.500 agent.production None
I have put cheese on the bread
   1.500 agent.focus.chunk goal:sandwich object:ham
   1.500 agent.production parma_ham
   1.550 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   1.550 agent.focus.chunk goal:sandwich object:bread_top
   1.550 agent.pm_new.clearFlag True
   1.550 agent.pm_new.clearFlag False
   1.550 agent.production bread_top
   1.600 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   1.600 agent.focus.chunk goal:sandwich object:bread_bottom
   1.600 agent.production bread_bottom
   1.650 agent.production None
I have a piece of bread
   1.650 agent.focus.chunk goal:sandwich object:cheese
   1.650 agent.production cheese
   1.700 agent.production None
I have put cheese on the bread
   1.700 agent.focus.chunk goal:sandwich object:ham
   1.700 agent.production parma_ham
   1.750 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   1.750 agent.focus.chunk goal:sandwich object:bread_top
   1.750 agent.pm_new.clearFlag True
   1.750 agent.pm_new.clearFlag False
   1.750 agent.production bread_top
   1.800 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   1.800 agent.focus.chunk goal:sandwich object:bread_bottom
   1.800 agent.production bread_bottom
   1.850 agent.production None
I have a piece of bread
   1.850 agent.focus.chunk goal:sandwich object:cheese
   1.850 agent.production cheese
   1.900 agent.production None
I have put cheese on the bread
   1.900 agent.focus.chunk goal:sandwich object:ham
   1.900 agent.production parma_ham
   1.950 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   1.950 agent.focus.chunk goal:sandwich object:bread_top
   1.950 agent.pm_new.clearFlag True
   1.950 agent.pm_new.clearFlag False
   1.950 agent.production bread_top
   2.000 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   2.000 agent.focus.chunk goal:sandwich object:bread_bottom
   2.000 agent.production bread_bottom
   2.050 agent.production None
I have a piece of bread
   2.050 agent.focus.chunk goal:sandwich object:cheese
   2.050 agent.production cheese
   2.100 agent.production None
I have put cheese on the bread
   2.100 agent.focus.chunk goal:sandwich object:ham
   2.100 agent.production parma_ham
   2.150 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   2.150 agent.focus.chunk goal:sandwich object:bread_top
   2.150 agent.pm_new.clearFlag True
   2.150 agent.pm_new.clearFlag False
   2.150 agent.production bread_top
   2.200 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   2.200 agent.focus.chunk goal:sandwich object:bread_bottom
   2.200 agent.production bread_bottom
   2.250 agent.production None
I have a piece of bread
   2.250 agent.focus.chunk goal:sandwich object:cheese
   2.250 agent.production cheese
   2.300 agent.production None
I have put cheese on the bread
   2.300 agent.focus.chunk goal:sandwich object:ham
   2.300 agent.production maple_ham
   2.350 agent.production None
I have put maple ham on the cheese
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
   2.350 agent.focus.chunk goal:sandwich object:bread_top
   2.350 agent.pm_new.clearFlag True
   2.350 agent.pm_new.clearFlag False
   2.350 agent.production bread_top
   2.400 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   2.400 agent.focus.chunk goal:sandwich object:bread_bottom
   2.400 agent.production bread_bottom
   2.450 agent.production None
I have a piece of bread
   2.450 agent.focus.chunk goal:sandwich object:cheese
   2.450 agent.production cheese
   2.500 agent.production None
I have put cheese on the bread
   2.500 agent.focus.chunk goal:sandwich object:ham
   2.500 agent.production parma_ham
   2.550 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   2.550 agent.focus.chunk goal:sandwich object:bread_top
   2.550 agent.pm_new.clearFlag True
   2.550 agent.pm_new.clearFlag False
   2.550 agent.production bread_top
   2.600 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   2.600 agent.focus.chunk goal:sandwich object:bread_bottom
   2.600 agent.production bread_bottom
   2.650 agent.production None
I have a piece of bread
   2.650 agent.focus.chunk goal:sandwich object:cheese
   2.650 agent.production cheese
   2.700 agent.production None
I have put cheese on the bread
   2.700 agent.focus.chunk goal:sandwich object:ham
   2.700 agent.production parma_ham
   2.750 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   2.750 agent.focus.chunk goal:sandwich object:bread_top
   2.750 agent.pm_new.clearFlag True
   2.750 agent.pm_new.clearFlag False
   2.750 agent.production bread_top
   2.800 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   2.800 agent.focus.chunk goal:sandwich object:bread_bottom
   2.800 agent.production bread_bottom
   2.850 agent.production None
I have a piece of bread
   2.850 agent.focus.chunk goal:sandwich object:cheese
   2.850 agent.production cheese
   2.900 agent.production None
I have put cheese on the bread
   2.900 agent.focus.chunk goal:sandwich object:ham
   2.900 agent.production parma_ham
   2.950 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   2.950 agent.focus.chunk goal:sandwich object:bread_top
   2.950 agent.pm_new.clearFlag True
   2.950 agent.pm_new.clearFlag False
   2.950 agent.production bread_top
   3.000 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   3.000 agent.focus.chunk goal:sandwich object:bread_bottom
   3.000 agent.production bread_bottom
   3.050 agent.production None
I have a piece of bread
   3.050 agent.focus.chunk goal:sandwich object:cheese
   3.050 agent.production cheese
   3.100 agent.production None
I have put cheese on the bread
   3.100 agent.focus.chunk goal:sandwich object:ham
   3.100 agent.production parma_ham
   3.150 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   3.150 agent.focus.chunk goal:sandwich object:bread_top
   3.150 agent.pm_new.clearFlag True
   3.150 agent.pm_new.clearFlag False
   3.150 agent.production bread_top
   3.200 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   3.200 agent.focus.chunk goal:sandwich object:bread_bottom
   3.200 agent.production bread_bottom
   3.250 agent.production None
I have a piece of bread
   3.250 agent.focus.chunk goal:sandwich object:cheese
   3.250 agent.production cheese
   3.300 agent.production None
I have put cheese on the bread
   3.300 agent.focus.chunk goal:sandwich object:ham
   3.300 agent.production maple_ham
   3.350 agent.production None
I have put maple ham on the cheese
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
   3.350 agent.focus.chunk goal:sandwich object:bread_top
   3.350 agent.pm_new.clearFlag True
   3.350 agent.pm_new.clearFlag False
   3.350 agent.production bread_top
   3.400 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   3.400 agent.focus.chunk goal:sandwich object:bread_bottom
   3.400 agent.production bread_bottom
   3.450 agent.production None
I have a piece of bread
   3.450 agent.focus.chunk goal:sandwich object:cheese
   3.450 agent.production cheese
   3.500 agent.production None
I have put cheese on the bread
   3.500 agent.focus.chunk goal:sandwich object:ham
   3.500 agent.production maple_ham
   3.550 agent.production None
I have put maple ham on the cheese
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
   3.550 agent.focus.chunk goal:sandwich object:bread_top
   3.550 agent.pm_new.clearFlag True
   3.550 agent.pm_new.clearFlag False
   3.550 agent.production bread_top
   3.600 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   3.600 agent.focus.chunk goal:sandwich object:bread_bottom
   3.600 agent.production bread_bottom
   3.650 agent.production None
I have a piece of bread
   3.650 agent.focus.chunk goal:sandwich object:cheese
   3.650 agent.production cheese
   3.700 agent.production None
I have put cheese on the bread
   3.700 agent.focus.chunk goal:sandwich object:ham
   3.700 agent.production parma_ham
   3.750 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   3.750 agent.focus.chunk goal:sandwich object:bread_top
   3.750 agent.pm_new.clearFlag True
   3.750 agent.pm_new.clearFlag False
   3.750 agent.production bread_top
   3.800 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   3.800 agent.focus.chunk goal:sandwich object:bread_bottom
   3.800 agent.production bread_bottom
   3.850 agent.production None
I have a piece of bread
   3.850 agent.focus.chunk goal:sandwich object:cheese
   3.850 agent.production cheese
   3.900 agent.production None
I have put cheese on the bread
   3.900 agent.focus.chunk goal:sandwich object:ham
   3.900 agent.production parma_ham
   3.950 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   3.950 agent.focus.chunk goal:sandwich object:bread_top
   3.950 agent.pm_new.clearFlag True
   3.950 agent.pm_new.clearFlag False
   3.950 agent.production bread_top
   4.000 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   4.000 agent.focus.chunk goal:sandwich object:bread_bottom
   4.000 agent.production bread_bottom
   4.050 agent.production None
I have a piece of bread
   4.050 agent.focus.chunk goal:sandwich object:cheese
   4.050 agent.production cheese
   4.100 agent.production None
I have put cheese on the bread
   4.100 agent.focus.chunk goal:sandwich object:ham
   4.100 agent.production parma_ham
   4.150 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   4.150 agent.focus.chunk goal:sandwich object:bread_top
   4.150 agent.pm_new.clearFlag True
   4.150 agent.pm_new.clearFlag False
   4.150 agent.production bread_top
   4.200 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   4.200 agent.focus.chunk goal:sandwich object:bread_bottom
   4.200 agent.production bread_bottom
   4.250 agent.production None
I have a piece of bread
   4.250 agent.focus.chunk goal:sandwich object:cheese
   4.250 agent.production cheese
   4.300 agent.production None
I have put cheese on the bread
   4.300 agent.focus.chunk goal:sandwich object:ham
   4.300 agent.production parma_ham
   4.350 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   4.350 agent.focus.chunk goal:sandwich object:bread_top
   4.350 agent.pm_new.clearFlag True
   4.350 agent.pm_new.clearFlag False
   4.350 agent.production bread_top
   4.400 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   4.400 agent.focus.chunk goal:sandwich object:bread_bottom
   4.400 agent.production bread_bottom
   4.450 agent.production None
I have a piece of bread
   4.450 agent.focus.chunk goal:sandwich object:cheese
   4.450 agent.production cheese
   4.500 agent.production None
I have put cheese on the bread
   4.500 agent.focus.chunk goal:sandwich object:ham
   4.500 agent.production parma_ham
   4.550 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   4.550 agent.focus.chunk goal:sandwich object:bread_top
   4.550 agent.pm_new.clearFlag True
   4.550 agent.pm_new.clearFlag False
   4.550 agent.production bread_top
   4.600 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   4.600 agent.focus.chunk goal:sandwich object:bread_bottom
   4.600 agent.production bread_bottom
   4.650 agent.production None
I have a piece of bread
   4.650 agent.focus.chunk goal:sandwich object:cheese
   4.650 agent.production cheese
   4.700 agent.production None
I have put cheese on the bread
   4.700 agent.focus.chunk goal:sandwich object:ham
   4.700 agent.production parma_ham
   4.750 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   4.750 agent.focus.chunk goal:sandwich object:bread_top
   4.750 agent.pm_new.clearFlag True
   4.750 agent.pm_new.clearFlag False
   4.750 agent.production bread_top
   4.800 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   4.800 agent.focus.chunk goal:sandwich object:bread_bottom
   4.800 agent.production bread_bottom
   4.850 agent.production None
I have a piece of bread
   4.850 agent.focus.chunk goal:sandwich object:cheese
   4.850 agent.production cheese
   4.900 agent.production None
I have put cheese on the bread
   4.900 agent.focus.chunk goal:sandwich object:ham
   4.900 agent.production parma_ham
   4.950 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   4.950 agent.focus.chunk goal:sandwich object:bread_top
   4.950 agent.pm_new.clearFlag True
   4.950 agent.pm_new.clearFlag False
   4.950 agent.production bread_top
   5.000 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   5.000 agent.focus.chunk goal:sandwich object:bread_bottom
   5.000 agent.production bread_bottom
   5.050 agent.production None
I have a piece of bread
   5.050 agent.focus.chunk goal:sandwich object:cheese
   5.050 agent.production cheese
   5.100 agent.production None
I have put cheese on the bread
   5.100 agent.focus.chunk goal:sandwich object:ham
   5.100 agent.production parma_ham
Traceback (most recent call last):
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_utility.py", line 65, in <module>
    subway.run()                               # run the environment
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/model.py", line 247, in run
    self.sch.run()
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/scheduler.py", line 116, in run
    self.do_event(heapq.heappop(self.queue))
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/scheduler.py", line 161, in do_event
    result=event.func(*event.args,**event.keys)
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/actr/core.py", line 40, in _process_productions
    self.log.production=choice.name
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/logger.py", line 173, in __setattr__
    getattr(self,key)._set(value)
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/logger.py", line 201, in _set
    self._log.set(self._prefix,value)
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/logger.py", line 112, in set
    self.display_value(key,value)
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/logger.py", line 120, in display_value
    print('%8.3f %s %s'%(self.time,key,value))
KeyboardInterrupt
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_utility.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.pm_new.alpha 0.2
   0.000 agent.pm_new.clearFlag False
   0.000 agent.pm_noise.noise 0.1
   0.000 agent.pm_noise.baseNoise 0
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk goal:sandwich object:cheese
   0.050 agent.production cheddar_cheese
   0.100 agent.production None
I have put cheese on the bread
   0.100 agent.focus.chunk goal:sandwich object:ham
   0.100 agent.pm_new.clearFlag True
   0.100 agent.pm_new.clearFlag False
   0.100 agent.production parma_ham
   0.150 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   0.150 agent.focus.chunk goal:sandwich object:bread_top
   0.150 agent.pm_new.clearFlag True
   0.150 agent.pm_new.clearFlag False
   0.150 agent.production bread_top
   0.200 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   0.200 agent.focus.chunk goal:sandwich object:bread_bottom
   0.200 agent.production bread_bottom
   0.250 agent.production None
I have a piece of bread
   0.250 agent.focus.chunk goal:sandwich object:cheese
   0.250 agent.production cheddar_cheese
   0.300 agent.production None
I have put cheese on the bread
   0.300 agent.focus.chunk goal:sandwich object:ham
   0.300 agent.pm_new.clearFlag True
   0.300 agent.pm_new.clearFlag False
   0.300 agent.production maple_ham
   0.350 agent.production None
I have put maple ham on the cheese
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
   0.350 agent.focus.chunk goal:sandwich object:bread_top
   0.350 agent.pm_new.clearFlag True
   0.350 agent.pm_new.clearFlag False
   0.350 agent.production bread_top
   0.400 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   0.400 agent.focus.chunk goal:sandwich object:bread_bottom
   0.400 agent.production bread_bottom
   0.450 agent.production None
I have a piece of bread
   0.450 agent.focus.chunk goal:sandwich object:cheese
   0.450 agent.production cheddar_cheese
   0.500 agent.production None
I have put cheese on the bread
   0.500 agent.focus.chunk goal:sandwich object:ham
   0.500 agent.pm_new.clearFlag True
   0.500 agent.pm_new.clearFlag False
   0.500 agent.production maple_ham
   0.550 agent.production None
I have put maple ham on the cheese
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
   0.550 agent.focus.chunk goal:sandwich object:bread_top
   0.550 agent.pm_new.clearFlag True
   0.550 agent.pm_new.clearFlag False
   0.550 agent.production bread_top
   0.600 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   0.600 agent.focus.chunk goal:sandwich object:bread_bottom
   0.600 agent.production bread_bottom
   0.650 agent.production None
I have a piece of bread
   0.650 agent.focus.chunk goal:sandwich object:cheese
   0.650 agent.production cheddar_cheese
   0.700 agent.production None
I have put cheese on the bread
   0.700 agent.focus.chunk goal:sandwich object:ham
   0.700 agent.pm_new.clearFlag True
   0.700 agent.pm_new.clearFlag False
   0.700 agent.production parma_ham
   0.750 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   0.750 agent.focus.chunk goal:sandwich object:bread_top
   0.750 agent.pm_new.clearFlag True
   0.750 agent.pm_new.clearFlag False
   0.750 agent.production bread_top
   0.800 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   0.800 agent.focus.chunk goal:sandwich object:bread_bottom
   0.800 agent.production bread_bottom
   0.850 agent.production None
I have a piece of bread
   0.850 agent.focus.chunk goal:sandwich object:cheese
   0.850 agent.production swiss_cheese
   0.900 agent.production None
I have put cheese on the bread
   0.900 agent.focus.chunk goal:sandwich object:ham
   0.900 agent.pm_new.clearFlag True
   0.900 agent.pm_new.clearFlag False
   0.900 agent.production maple_ham
   0.950 agent.production None
I have put maple ham on the cheese
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
   0.950 agent.focus.chunk goal:sandwich object:bread_top
   0.950 agent.pm_new.clearFlag True
   0.950 agent.pm_new.clearFlag False
   0.950 agent.production bread_top
   1.000 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   1.000 agent.focus.chunk goal:sandwich object:bread_bottom
   1.000 agent.production bread_bottom
   1.050 agent.production None
I have a piece of bread
   1.050 agent.focus.chunk goal:sandwich object:cheese
   1.050 agent.production cheddar_cheese
   1.100 agent.production None
I have put cheese on the bread
   1.100 agent.focus.chunk goal:sandwich object:ham
   1.100 agent.pm_new.clearFlag True
   1.100 agent.pm_new.clearFlag False
   1.100 agent.production maple_ham
   1.150 agent.production None
I have put maple ham on the cheese
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
   1.150 agent.focus.chunk goal:sandwich object:bread_top
   1.150 agent.pm_new.clearFlag True
   1.150 agent.pm_new.clearFlag False
   1.150 agent.production bread_top
   1.200 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   1.200 agent.focus.chunk goal:sandwich object:bread_bottom
   1.200 agent.production bread_bottom
   1.250 agent.production None
I have a piece of bread
   1.250 agent.focus.chunk goal:sandwich object:cheese
   1.250 agent.production cheddar_cheese
   1.300 agent.production None
I have put cheese on the bread
   1.300 agent.focus.chunk goal:sandwich object:ham
   1.300 agent.pm_new.clearFlag True
   1.300 agent.pm_new.clearFlag False
   1.300 agent.production maple_ham
   1.350 agent.production None
I have put maple ham on the cheese
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
   1.350 agent.focus.chunk goal:sandwich object:bread_top
   1.350 agent.pm_new.clearFlag True
   1.350 agent.pm_new.clearFlag False
   1.350 agent.production bread_top
   1.400 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   1.400 agent.focus.chunk goal:sandwich object:bread_bottom
   1.400 agent.production bread_bottom
   1.450 agent.production None
I have a piece of bread
   1.450 agent.focus.chunk goal:sandwich object:cheese
   1.450 agent.production cheddar_cheese
   1.500 agent.production None
I have put cheese on the bread
   1.500 agent.focus.chunk goal:sandwich object:ham
   1.500 agent.pm_new.clearFlag True
   1.500 agent.pm_new.clearFlag False
   1.500 agent.production parma_ham
   1.550 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   1.550 agent.focus.chunk goal:sandwich object:bread_top
   1.550 agent.pm_new.clearFlag True
   1.550 agent.pm_new.clearFlag False
   1.550 agent.production bread_top
   1.600 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   1.600 agent.focus.chunk goal:sandwich object:bread_bottom
   1.600 agent.production bread_bottom
   1.650 agent.production None
I have a piece of bread
   1.650 agent.focus.chunk goal:sandwich object:cheese
   1.650 agent.production cheddar_cheese
   1.700 agent.production None
I have put cheese on the bread
   1.700 agent.focus.chunk goal:sandwich object:ham
   1.700 agent.pm_new.clearFlag True
   1.700 agent.pm_new.clearFlag False
   1.700 agent.production parma_ham
   1.750 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   1.750 agent.focus.chunk goal:sandwich object:bread_top
   1.750 agent.pm_new.clearFlag True
   1.750 agent.pm_new.clearFlag False
   1.750 agent.production bread_top
   1.800 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   1.800 agent.focus.chunk goal:sandwich object:bread_bottom
   1.800 agent.production bread_bottom
   1.850 agent.production None
I have a piece of bread
   1.850 agent.focus.chunk goal:sandwich object:cheese
   1.850 agent.production swiss_cheese
   1.900 agent.production None
I have put cheese on the bread
   1.900 agent.focus.chunk goal:sandwich object:ham
   1.900 agent.pm_new.clearFlag True
   1.900 agent.pm_new.clearFlag False
   1.900 agent.production parma_ham
   1.950 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   1.950 agent.focus.chunk goal:sandwich object:bread_top
   1.950 agent.pm_new.clearFlag True
   1.950 agent.pm_new.clearFlag False
   1.950 agent.production bread_top
   2.000 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   2.000 agent.focus.chunk goal:sandwich object:bread_bottom
   2.000 agent.production bread_bottom
   2.050 agent.production None
I have a piece of bread
   2.050 agent.focus.chunk goal:sandwich object:cheese
   2.050 agent.production swiss_cheese
   2.100 agent.production None
I have put cheese on the bread
   2.100 agent.focus.chunk goal:sandwich object:ham
   2.100 agent.pm_new.clearFlag True
   2.100 agent.pm_new.clearFlag False
   2.100 agent.production parma_ham
   2.150 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   2.150 agent.focus.chunk goal:sandwich object:bread_top
   2.150 agent.pm_new.clearFlag True
   2.150 agent.pm_new.clearFlag False
   2.150 agent.production bread_top
   2.200 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   2.200 agent.focus.chunk goal:sandwich object:bread_bottom
   2.200 agent.production bread_bottom
   2.250 agent.production None
I have a piece of bread
   2.250 agent.focus.chunk goal:sandwich object:cheese
   2.250 agent.production swiss_cheese
   2.300 agent.production None
I have put cheese on the bread
   2.300 agent.focus.chunk goal:sandwich object:ham
   2.300 agent.pm_new.clearFlag True
   2.300 agent.pm_new.clearFlag False
   2.300 agent.production parma_ham
   2.350 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   2.350 agent.focus.chunk goal:sandwich object:bread_top
   2.350 agent.pm_new.clearFlag True
   2.350 agent.pm_new.clearFlag False
   2.350 agent.production bread_top
   2.400 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   2.400 agent.focus.chunk goal:sandwich object:bread_bottom
   2.400 agent.production bread_bottom
   2.450 agent.production None
I have a piece of bread
   2.450 agent.focus.chunk goal:sandwich object:cheese
   2.450 agent.production cheddar_cheese
   2.500 agent.production None
I have put cheese on the bread
   2.500 agent.focus.chunk goal:sandwich object:ham
   2.500 agent.pm_new.clearFlag True
   2.500 agent.pm_new.clearFlag False
   2.500 agent.production parma_ham
   2.550 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   2.550 agent.focus.chunk goal:sandwich object:bread_top
   2.550 agent.pm_new.clearFlag True
   2.550 agent.pm_new.clearFlag False
   2.550 agent.production bread_top
   2.600 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   2.600 agent.focus.chunk goal:sandwich object:bread_bottom
   2.600 agent.production bread_bottom
   2.650 agent.production None
I have a piece of bread
   2.650 agent.focus.chunk goal:sandwich object:cheese
   2.650 agent.production swiss_cheese
   2.700 agent.production None
I have put cheese on the bread
   2.700 agent.focus.chunk goal:sandwich object:ham
   2.700 agent.pm_new.clearFlag True
   2.700 agent.pm_new.clearFlag False
   2.700 agent.production parma_ham
   2.750 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   2.750 agent.focus.chunk goal:sandwich object:bread_top
   2.750 agent.pm_new.clearFlag True
   2.750 agent.pm_new.clearFlag False
   2.750 agent.production bread_top
   2.800 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   2.800 agent.focus.chunk goal:sandwich object:bread_bottom
   2.800 agent.production bread_bottom
   2.850 agent.production None
I have a piece of bread
   2.850 agent.focus.chunk goal:sandwich object:cheese
   2.850 agent.production swiss_cheese
   2.900 agent.production None
Traceback (most recent call last):
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_utility.py", line 71, in <module>
    subway.run()                               # run the environment
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/model.py", line 247, in run
    self.sch.run()
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/scheduler.py", line 116, in run
    self.do_event(heapq.heappop(self.queue))
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/scheduler.py", line 161, in do_event
    result=event.func(*event.args,**event.keys)
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/actr/core.py", line 55, in _process_productions
    self.log.production=None
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/logger.py", line 173, in __setattr__
    getattr(self,key)._set(value)
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/logger.py", line 201, in _set
    self._log.set(self._prefix,value)
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/logger.py", line 112, in set
    self.display_value(key,value)
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/logger.py", line 120, in display_value
    print('%8.3f %s %s'%(self.time,key,value))
KeyboardInterrupt
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_utility.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.pm_new.alpha 0.2
   0.000 agent.pm_new.clearFlag False
   0.000 agent.pm_noise.noise 0.1
   0.000 agent.pm_noise.baseNoise 0
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk goal:sandwich object:cheese
   0.050 agent.production swiss_cheese
   0.100 agent.production None
I have put swiss cheese on the bread
   0.100 agent.focus.chunk goal:sandwich object:ham
   0.100 agent.pm_new.clearFlag True
   0.100 agent.pm_new.clearFlag False
   0.100 agent.production parma_ham
   0.150 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   0.150 agent.focus.chunk goal:sandwich object:bread_top
   0.150 agent.pm_new.clearFlag True
   0.150 agent.pm_new.clearFlag False
   0.150 agent.production bread_top
   0.200 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   0.200 agent.focus.chunk goal:sandwich object:bread_bottom
   0.200 agent.production bread_bottom
   0.250 agent.production None
I have a piece of bread
   0.250 agent.focus.chunk goal:sandwich object:cheese
   0.250 agent.production cheddar_cheese
   0.300 agent.production None
I have put cheddar cheese on the bread
   0.300 agent.focus.chunk goal:sandwich object:ham
   0.300 agent.pm_new.clearFlag True
   0.300 agent.pm_new.clearFlag False
   0.300 agent.production parma_ham
   0.350 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   0.350 agent.focus.chunk goal:sandwich object:bread_top
   0.350 agent.pm_new.clearFlag True
   0.350 agent.pm_new.clearFlag False
   0.350 agent.production bread_top
   0.400 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   0.400 agent.focus.chunk goal:sandwich object:bread_bottom
   0.400 agent.production bread_bottom
   0.450 agent.production None
I have a piece of bread
   0.450 agent.focus.chunk goal:sandwich object:cheese
   0.450 agent.production cheddar_cheese
   0.500 agent.production None
I have put cheddar cheese on the bread
   0.500 agent.focus.chunk goal:sandwich object:ham
   0.500 agent.pm_new.clearFlag True
   0.500 agent.pm_new.clearFlag False
   0.500 agent.production maple_ham
   0.550 agent.production None
I have put maple ham on the cheese
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
   0.550 agent.focus.chunk goal:sandwich object:bread_top
   0.550 agent.pm_new.clearFlag True
   0.550 agent.pm_new.clearFlag False
   0.550 agent.production bread_top
   0.600 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   0.600 agent.focus.chunk goal:sandwich object:bread_bottom
   0.600 agent.production bread_bottom
   0.650 agent.production None
I have a piece of bread
   0.650 agent.focus.chunk goal:sandwich object:cheese
   0.650 agent.production cheddar_cheese
   0.700 agent.production None
I have put cheddar cheese on the bread
   0.700 agent.focus.chunk goal:sandwich object:ham
   0.700 agent.pm_new.clearFlag True
   0.700 agent.pm_new.clearFlag False
   0.700 agent.production parma_ham
   0.750 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   0.750 agent.focus.chunk goal:sandwich object:bread_top
   0.750 agent.pm_new.clearFlag True
   0.750 agent.pm_new.clearFlag False
   0.750 agent.production bread_top
   0.800 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   0.800 agent.focus.chunk goal:sandwich object:bread_bottom
   0.800 agent.production bread_bottom
   0.850 agent.production None
I have a piece of bread
   0.850 agent.focus.chunk goal:sandwich object:cheese
   0.850 agent.production cheddar_cheese
   0.900 agent.production None
I have put cheddar cheese on the bread
   0.900 agent.focus.chunk goal:sandwich object:ham
   0.900 agent.pm_new.clearFlag True
   0.900 agent.pm_new.clearFlag False
   0.900 agent.production maple_ham
   0.950 agent.production None
I have put maple ham on the cheese
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
   0.950 agent.focus.chunk goal:sandwich object:bread_top
   0.950 agent.pm_new.clearFlag True
   0.950 agent.pm_new.clearFlag False
   0.950 agent.production bread_top
   1.000 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   1.000 agent.focus.chunk goal:sandwich object:bread_bottom
   1.000 agent.production bread_bottom
   1.050 agent.production None
I have a piece of bread
   1.050 agent.focus.chunk goal:sandwich object:cheese
   1.050 agent.production cheddar_cheeseTraceback (most recent call last):
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_utility.py", line 71, in <module>
    subway.run()                               # run the environment
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/model.py", line 247, in run
    self.sch.run()
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/scheduler.py", line 116, in run
    self.do_event(heapq.heappop(self.queue))
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/scheduler.py", line 161, in do_event
    result=event.func(*event.args,**event.keys)
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/actr/core.py", line 40, in _process_productions
    self.log.production=choice.name
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/logger.py", line 173, in __setattr__
    getattr(self,key)._set(value)
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/logger.py", line 201, in _set
    self._log.set(self._prefix,value)
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/logger.py", line 112, in set
    self.display_value(key,value)
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/logger.py", line 120, in display_value
    print('%8.3f %s %s'%(self.time,key,value))
KeyboardInterrupt
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_utility.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.pm_new.alpha 0.2
   0.000 agent.pm_new.clearFlag False
   0.000 agent.pm_noise.noise 0.1
   0.000 agent.pm_noise.baseNoise 0
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk goal:sandwich object:cheese
   0.050 agent.production cheddar_cheese
   0.100 agent.production None
I have put cheddar cheese on the bread
   0.100 agent.focus.chunk goal:sandwich object:ham
   0.100 agent.pm_new.clearFlag True
   0.100 agent.pm_new.clearFlag False
   0.100 agent.production maple_ham
   0.150 agent.production None
I have put maple ham on the cheese
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
   0.150 agent.focus.chunk goal:sandwich object:bread_top
   0.150 agent.pm_new.clearFlag True
   0.150 agent.pm_new.clearFlag False
   0.150 agent.production bread_top
   0.200 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   0.200 agent.focus.chunk goal:sandwich object:bread_bottom
   0.200 agent.production bread_bottom
   0.250 agent.production None
I have a piece of bread
   0.250 agent.focus.chunk goal:sandwich object:cheese
   0.250 agent.production swiss_cheese
   0.300 agent.production None
I have put swiss cheese on the bread
   0.300 agent.focus.chunk goal:sandwich object:ham
   0.300 agent.pm_new.clearFlag True
   0.300 agent.pm_new.clearFlag False
   0.300 agent.production maple_ham
   0.350 agent.production None
I have put maple ham on the cheese
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
   0.350 agent.focus.chunk goal:sandwich object:bread_top
   0.350 agent.pm_new.clearFlag True
   0.350 agent.pm_new.clearFlag False
   0.350 agent.production bread_top
   0.400 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   0.400 agent.focus.chunk goal:sandwich object:bread_bottom
   0.400 agent.production bread_bottom
   0.450 agent.production None
I have a piece of bread
   0.450 agent.focus.chunk goal:sandwich object:cheese
   0.450 agent.production cheddar_cheese
   0.500 agent.production None
I have put cheddar cheese on the bread
   0.500 agent.focus.chunk goal:sandwich object:ham
   0.500 agent.pm_new.clearFlag True
   0.500 agent.pm_new.clearFlag False
   0.500 agent.production maple_ham
   0.550 agent.production None
I have put maple ham on the cheese
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
   0.550 agent.focus.chunk goal:sandwich object:bread_top
   0.550 agent.pm_new.clearFlag True
   0.550 agent.pm_new.clearFlag False
   0.550 agent.production bread_top
   0.600 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   0.600 agent.focus.chunk goal:sandwich object:bread_bottom
   0.600 agent.production bread_bottom
   0.650 agent.production None
I have a piece of bread
   0.650 agent.focus.chunk goal:sandwich object:cheese
   0.650 agent.production swiss_cheese
   0.700 agent.production None
I have put swiss cheese on the bread
   0.700 agent.focus.chunk goal:sandwich object:ham
   0.700 agent.pm_new.clearFlag True
   0.700 agent.pm_new.clearFlag False
   0.700 agent.production parma_ham
   0.750 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   0.750 agent.focus.chunk goal:sandwich object:bread_top
   0.750 agent.pm_new.clearFlag True
   0.750 agent.pm_new.clearFlag False
   0.750 agent.production bread_top
   0.800 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   0.800 agent.focus.chunk goal:sandwich object:bread_bottom
   0.800 agent.production bread_bottom
   0.850 agent.production None
I have a piece of bread
   0.850 agent.focus.chunk goal:sandwich object:cheese
   0.850 agent.production cheddar_cheese
   0.900 agent.production None
I have put cheddar cheese on the bread
   0.900 agent.focus.chunk goal:sandwich object:ham
   0.900 agent.pm_new.clearFlag True
   0.900 agent.pm_new.clearFlag False
   0.900 agent.production parma_ham
   0.950 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   0.950 agent.focus.chunk goal:sandwich object:bread_top
   0.950 agent.pm_new.clearFlag True
   0.950 agent.pm_new.clearFlag False
   0.950 agent.production bread_top
   1.000 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   1.000 agent.focus.chunk goal:sandwich object:bread_bottom
   1.000 agent.production bread_bottom
   1.050 agent.production None
I have a piece of bread
   1.050 agent.focus.chunk goal:sandwich object:cheese
   1.050 agent.production cheddar_cheese
   1.100 agent.production None
I have put cheddar cheese on the bread
   1.100 agent.focus.chunk goal:sandwich object:ham
   1.100 agent.pm_new.clearFlag True
   1.100 agent.pm_new.clearFlag False
   1.100 agent.production parma_ham
   1.150 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   1.150 agent.focus.chunk goal:sandwich object:bread_top
   1.150 agent.pm_new.clearFlag True
   1.150 agent.pm_new.clearFlag False
   1.150 agent.production bread_top
   1.200 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   1.200 agent.focus.chunk goal:sandwich object:bread_bottom
   1.200 agent.production bread_bottom
   1.250 agent.production None
I have a piece of bread
   1.250 agent.focus.chunk goal:sandwich object:cheese
   1.250 agent.production cheddar_cheese
   1.300 agent.production None
I have put cheddar cheese on the bread
   1.300 agent.focus.chunk goal:sandwich object:ham
   1.300 agent.pm_new.clearFlag True
   1.300 agent.pm_new.clearFlag False
   1.300 agent.production parma_ham
   1.350 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   1.350 agent.focus.chunk goal:sandwich object:bread_top
   1.350 agent.pm_new.clearFlag True
   1.350 agent.pm_new.clearFlag False
   1.350 agent.production bread_top
   1.400 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   1.400 agent.focus.chunk goal:sandwich object:bread_bottom
   1.400 agent.production bread_bottom
   1.450 agent.production None
I have a piece of bread
   1.450 agent.focus.chunk goal:sandwich object:cheese
   1.450 agent.production swiss_cheese
   1.500 agent.production None
I have put swiss cheese on the bread
   1.500 agent.focus.chunk goal:sandwich object:ham
   1.500 agent.pm_new.clearFlag True
   1.500 agent.pm_new.clearFlag False
   1.500 agent.production maple_ham
   1.550 agent.production None
I have put maple ham on the cheese
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
   1.550 agent.focus.chunk goal:sandwich object:bread_top
   1.550 agent.pm_new.clearFlag True
   1.550 agent.pm_new.clearFlag False
   1.550 agent.production bread_top
   1.600 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   1.600 agent.focus.chunk goal:sandwich object:bread_bottom
   1.600 agent.production bread_bottom
   1.650 agent.production None
I have a piece of bread
   1.650 agent.focus.chunk goal:sandwich object:cheese
   1.650 agent.production cheddar_cheese
   1.700 agent.production None
I have put cheddar cheese on the bread
   1.700 agent.focus.chunk goal:sandwich object:ham
   1.700 agent.pm_new.clearFlag True
   1.700 agent.pm_new.clearFlag False
   1.700 agent.production parma_ham
   1.750 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   1.750 agent.focus.chunk goal:sandwich object:bread_top
   1.750 agent.pm_new.clearFlag True
   1.750 agent.pm_new.clearFlag False
   1.750 agent.production bread_top
   1.800 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   1.800 agent.focus.chunk goal:sandwich object:bread_bottom
   1.800 agent.production bread_bottom
   1.850 agent.production None
I have a piece of bread
   1.850 agent.focus.chunk goal:sandwich object:cheese
   1.850 agent.production cheddar_cheese
   1.900 agent.production None
I have put cheddar cheese on the bread
   1.900 agent.focus.chunk goal:sandwich object:ham
   1.900 agent.pm_new.clearFlag True
   1.900 agent.pm_new.clearFlag False
   1.900 agent.production maple_ham
   1.950 agent.production None
I have put maple ham on the cheese
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
   1.950 agent.focus.chunk goal:sandwich object:bread_top
   1.950 agent.pm_new.clearFlag True
   1.950 agent.pm_new.clearFlag False
   1.950 agent.production bread_top
   2.000 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   2.000 agent.focus.chunk goal:sandwich object:bread_bottom
   2.000 agent.production bread_bottom
   2.050 agent.production None
I have a piece of bread
   2.050 agent.focus.chunk goal:sandwich object:cheese
   2.050 agent.production swiss_cheese
   2.100 agent.production None
I have put swiss cheese on the bread
   2.100 agent.focus.chunk goal:sandwich object:ham
   2.100 agent.pm_new.clearFlag True
   2.100 agent.pm_new.clearFlag False
   2.100 agent.production parma_ham
   2.150 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   2.150 agent.focus.chunk goal:sandwich object:bread_top
   2.150 agent.pm_new.clearFlag True
   2.150 agent.pm_new.clearFlag False
   2.150 agent.production bread_top
   2.200 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   2.200 agent.focus.chunk goal:sandwich object:bread_bottom
   2.200 agent.production bread_bottom
   2.250 agent.production None
I have a piece of bread
   2.250 agent.focus.chunk goal:sandwich object:cheese
   2.250 agent.production cheddar_cheese
   2.300 agent.production None
I have put cheddar cheese on the bread
   2.300 agent.focus.chunk goal:sandwich object:ham
   2.300 agent.pm_new.clearFlag True
   2.300 agent.pm_new.clearFlag False
   2.300 agent.production parma_ham
   2.350 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   2.350 agent.focus.chunk goal:sandwich object:bread_top
   2.350 agent.pm_new.clearFlag True
   2.350 agent.pm_new.clearFlag False
   2.350 agent.production bread_top
   2.400 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   2.400 agent.focus.chunk goal:sandwich object:bread_bottom
   2.400 agent.production bread_bottom
   2.450 agent.production None
I have a piece of bread
   2.450 agent.focus.chunk goal:sandwich object:cheese
   2.450 agent.production swiss_cheese
   2.500 agent.production None
I have put swiss cheese on the bread
   2.500 agent.focus.chunk goal:sandwich object:ham
   2.500 agent.pm_new.clearFlag True
   2.500 agent.pm_new.clearFlag False
   2.500 agent.production parma_ham
   2.550 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   2.550 agent.focus.chunk goal:sandwich object:bread_top
   2.550 agent.pm_new.clearFlag True
   2.550 agent.pm_new.clearFlag False
   2.550 agent.production bread_top
   2.600 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   2.600 agent.focus.chunk goal:sandwich object:bread_bottom
   2.600 agent.production bread_bottom
   2.650 agent.production None
I have a piece of bread
   2.650 agent.focus.chunk goal:sandwich object:cheese
   2.650 agent.production cheddar_cheese
   2.700 agent.production None
I have put cheddar cheese on the bread
   2.700 agent.focus.chunk goal:sandwich object:ham
   2.700 agent.pm_new.clearFlag True
   2.700 agent.pm_new.clearFlag False
   2.700 agent.production parma_ham
   2.750 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   2.750 agent.focus.chunk goal:sandwich object:bread_top
   2.750 agent.pm_new.clearFlag True
   2.750 agent.pm_new.clearFlag False
   2.750 agent.production bread_top
   2.800 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   2.800 agent.focus.chunk goal:sandwich object:bread_bottom
   2.800 agent.production bread_bottom
   2.850 agent.production None
I have a piece of bread
   2.850 agent.focus.chunk goal:sandwich object:cheese
   2.850 agent.production swiss_cheese
   2.900 agent.production None
I have put swiss cheese on the bread
   2.900 agent.focus.chunk goal:sandwich object:ham
   2.900 agent.pm_new.clearFlag True
   2.900 agent.pm_new.clearFlag False
   2.900 agent.production maple_ham
   2.950 agent.production None
I have put maple ham on the cheese
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
   2.950 agent.focus.chunk goal:sandwich object:bread_top
   2.950 agent.pm_new.clearFlag True
   2.950 agent.pm_new.clearFlag False
   2.950 agent.production bread_top
   3.000 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   3.000 agent.focus.chunk goal:sandwich object:bread_bottom
   3.000 agent.production bread_bottom
   3.050 agent.production None
I have a piece of bread
   3.050 agent.focus.chunk goal:sandwich object:cheese
   3.050 agent.production swiss_cheese
   3.100 agent.production None
I have put swiss cheese on the bread
   3.100 agent.focus.chunk goal:sandwich object:ham
   3.100 agent.pm_new.clearFlag True
   3.100 agent.pm_new.clearFlag False
   3.100 agent.production maple_ham
   3.150 agent.production None
I have put maple ham on the cheese
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
   3.150 agent.focus.chunk goal:sandwich object:bread_top
   3.150 agent.pm_new.clearFlag True
   3.150 agent.pm_new.clearFlag False
   3.150 agent.production bread_top
   3.200 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   3.200 agent.focus.chunk goal:sandwich object:bread_bottom
   3.200 agent.production bread_bottom
   3.250 agent.production None
I have a piece of bread
   3.250 agent.focus.chunk goal:sandwich object:cheese
   3.250 agent.production cheddar_cheese
   3.300 agent.production None
I have put cheddar cheese on the bread
   3.300 agent.focus.chunk goal:sandwich object:ham
   3.300 agent.pm_new.clearFlag True
   3.300 agent.pm_new.clearFlag False
   3.300 agent.production parma_ham
   3.350 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   3.350 agent.focus.chunk goal:sandwich object:bread_top
   3.350 agent.pm_new.clearFlag True
   3.350 agent.pm_new.clearFlag False
   3.350 agent.production bread_top
   3.400 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   3.400 agent.focus.chunk goal:sandwich object:bread_bottom
   3.400 agent.production bread_bottom
   3.450 agent.production None
I have a piece of bread
   3.450 agent.focus.chunk goal:sandwich object:cheese
   3.450 agent.production swiss_cheese
   3.500 agent.production None
I have put swiss cheese on the bread
   3.500 agent.focus.chunk goal:sandwich object:ham
   3.500 agent.pm_new.clearFlag True
   3.500 agent.pm_new.clearFlag False
   3.500 agent.production parma_ham
   3.550 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   3.550 agent.focus.chunk goal:sandwich object:bread_top
   3.550 agent.pm_new.clearFlag True
   3.550 agent.pm_new.clearFlag False
   3.550 agent.production bread_top
   3.600 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   3.600 agent.focus.chunk goal:sandwich object:bread_bottom
   3.600 agent.production bread_bottom
   3.650 agent.production None
I have a piece of bread
   3.650 agent.focus.chunk goal:sandwich object:cheese
   3.650 agent.production swiss_cheese
   3.700 agent.production None
I have put swiss cheese on the bread
   3.700 agent.focus.chunk goal:sandwich object:ham
   3.700 agent.pm_new.clearFlag True
   3.700 agent.pm_new.clearFlag False
   3.700 agent.production parma_ham
   3.750 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   3.750 agent.focus.chunk goal:sandwich object:bread_top
   3.750 agent.pm_new.clearFlag True
   3.750 agent.pm_new.clearFlag False
   3.750 agent.production bread_top
   3.800 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   3.800 agent.focus.chunk goal:sandwich object:bread_bottom
   3.800 agent.production bread_bottom
   3.850 agent.production None
I have a piece of bread
   3.850 agent.focus.chunk goal:sandwich object:cheese
   3.850 agent.production swiss_cheese
   3.900 agent.production None
I have put swiss cheese on the bread
   3.900 agent.focus.chunk goal:sandwich object:ham
   3.900 agent.pm_new.clearFlag True
   3.900 agent.pm_new.clearFlag False
   3.900 agent.production parma_ham
   3.950 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   3.950 agent.focus.chunk goal:sandwich object:bread_top
   3.950 agent.pm_new.clearFlag True
   3.950 agent.pm_new.clearFlag False
   3.950 agent.production bread_top
   4.000 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   4.000 agent.focus.chunk goal:sandwich object:bread_bottom
   4.000 agent.production bread_bottom
   4.050 agent.production None
I have a piece of bread
   4.050 agent.focus.chunk goal:sandwich object:cheese
   4.050 agent.production swiss_cheese
   4.100 agent.production None
I have put swiss cheese on the bread
   4.100 agent.focus.chunk goal:sandwich object:ham
   4.100 agent.pm_new.clearFlag True
   4.100 agent.pm_new.clearFlag False
   4.100 agent.production parma_ham
   4.150 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   4.150 agent.focus.chunk goal:sandwich object:bread_top
   4.150 agent.pm_new.clearFlag True
   4.150 agent.pm_new.clearFlag False
   4.150 agent.production bread_top
   4.200 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   4.200 agent.focus.chunk goal:sandwich object:bread_bottom
   4.200 agent.production bread_bottom
   4.250 agent.production None
I have a piece of bread
   4.250 agent.focus.chunk goal:sandwich object:cheese
   4.250 agent.production swiss_cheese
   4.300 agent.production None
I have put swiss cheese on the bread
   4.300 agent.focus.chunk goal:sandwich object:ham
   4.300 agent.pm_new.clearFlag True
   4.300 agent.pm_new.clearFlag False
   4.300 agent.production parma_ham
   4.350 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   4.350 agent.focus.chunk goal:sandwich object:bread_top
   4.350 agent.pm_new.clearFlag True
   4.350 agent.pm_new.clearFlag False
   4.350 agent.production bread_top
   4.400 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   4.400 agent.focus.chunk goal:sandwich object:bread_bottom
   4.400 agent.production bread_bottom
   4.450 agent.production None
I have a piece of bread
   4.450 agent.focus.chunk goal:sandwich object:cheese
   4.450 agent.production swiss_cheese
   4.500 agent.production None
I have put swiss cheese on the bread
   4.500 agent.focus.chunk goal:sandwich object:ham
   4.500 agent.pm_new.clearFlag True
   4.500 agent.pm_new.clearFlag False
   4.500 agent.production parma_ham
   4.550 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   4.550 agent.focus.chunk goal:sandwich object:bread_top
   4.550 agent.pm_new.clearFlag True
   4.550 agent.pm_new.clearFlag False
   4.550 agent.production bread_top
   4.600 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   4.600 agent.focus.chunk goal:sandwich object:bread_bottom
   4.600 agent.production bread_bottom
   4.650 agent.production None
I have a piece of bread
   4.650 agent.focus.chunk goal:sandwich object:cheese
   4.650 agent.production cheddar_cheese
   4.700 agent.production None
I have put cheddar cheese on the bread
   4.700 agent.focus.chunk goal:sandwich object:ham
   4.700 agent.pm_new.clearFlag True
   4.700 agent.pm_new.clearFlag False
   4.700 agent.production parma_ham
   4.750 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   4.750 agent.focus.chunk goal:sandwich object:bread_top
   4.750 agent.pm_new.clearFlag True
   4.750 agent.pm_new.clearFlag False
   4.750 agent.production bread_top
   4.800 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   4.800 agent.focus.chunk goal:sandwich object:bread_bottom
   4.800 agent.production bread_bottom
   4.850 agent.production None
I have a piece of bread
   4.850 agent.focus.chunk goal:sandwich object:cheese
   4.850 agent.production swiss_cheese
   4.900 agent.production None
I have put swiss cheese on the bread
   4.900 agent.focus.chunk goal:sandwich object:ham
   4.900 agent.pm_new.clearFlag True
   4.900 agent.pm_new.clearFlag False
   4.900 agent.production parma_ham
   4.950 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   4.950 agent.focus.chunk goal:sandwich object:bread_top
   4.950 agent.pm_new.clearFlag True
   4.950 agent.pm_new.clearFlag False
   4.950 agent.production bread_top
   5.000 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   5.000 agent.focus.chunk goal:sandwich object:bread_bottom
   5.000 agent.production bread_bottom
   5.050 agent.production None
I have a piece of bread
   5.050 agent.focus.chunk goal:sandwich object:cheese
   5.050 agent.production swiss_cheese
   5.100 agent.production None
I have put swiss cheese on the bread
   5.100 agent.focus.chunk goal:sandwich object:ham
   5.100 agent.pm_new.clearFlag True
   5.100 agent.pm_new.clearFlag False
   5.100 agent.production maple_ham
   5.150 agent.production None
I have put maple ham on the cheese
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
   5.150 agent.focus.chunk goal:sandwich object:bread_top
   5.150 agent.pm_new.clearFlag True
   5.150 agent.pm_new.clearFlag False
   5.150 agent.production bread_top
   5.200 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   5.200 agent.focus.chunk goal:sandwich object:bread_bottom
   5.200 agent.production bread_bottom
   5.250 agent.production None
I have a piece of bread
   5.250 agent.focus.chunk goal:sandwich object:cheese
   5.250 agent.production cheddar_cheese
   5.300 agent.production None
I have put cheddar cheese on the bread
   5.300 agent.focus.chunk goal:sandwich object:ham
   5.300 agent.pm_new.clearFlag True
   5.300 agent.pm_new.clearFlag False
   5.300 agent.production maple_ham
   5.350 agent.production None
I have put maple ham on the cheese
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
   5.350 agent.focus.chunk goal:sandwich object:bread_top
   5.350 agent.pm_new.clearFlag True
   5.350 agent.pm_new.clearFlag False
   5.350 agent.production bread_top
   5.400 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   5.400 agent.focus.chunk goal:sandwich object:bread_bottom
   5.400 agent.production bread_bottom
   5.450 agent.production None
I have a piece of bread
   5.450 agent.focus.chunk goal:sandwich object:cheese
   5.450 agent.production swiss_cheese
   5.500 agent.production None
I have put swiss cheese on the bread
   5.500 agent.focus.chunk goal:sandwich object:ham
   5.500 agent.pm_new.clearFlag True
   5.500 agent.pm_new.clearFlag False
   5.500 agent.production maple_ham
   5.550 agent.production None
I have put maple ham on the cheese
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
   5.550 agent.focus.chunk goal:sandwich object:bread_top
   5.550 agent.pm_new.clearFlag True
   5.550 agent.pm_new.clearFlag False
   5.550 agent.production bread_top
   5.600 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   5.600 agent.focus.chunk goal:sandwich object:bread_bottom
   5.600 agent.production bread_bottom
   5.650 agent.production None
I have a piece of bread
   5.650 agent.focus.chunk goal:sandwich object:cheese
   5.650 agent.production swiss_cheese
   5.700 agent.production None
I have put swiss cheese on the bread
   5.700 agent.focus.chunk goal:sandwich object:ham
   5.700 agent.pm_new.clearFlag True
   5.700 agent.pm_new.clearFlag False
   5.700 agent.production parma_ham
   5.750 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   5.750 agent.focus.chunk goal:sandwich object:bread_top
   5.750 agent.pm_new.clearFlag True
   5.750 agent.pm_new.clearFlag False
   5.750 agent.production bread_top
   5.800 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   5.800 agent.focus.chunk goal:sandwich object:bread_bottom
   5.800 agent.production bread_bottom
   5.850 agent.production None
I have a piece of bread
   5.850 agent.focus.chunk goal:sandwich object:cheese
   5.850 agent.production swiss_cheese
   5.900 agent.production None
I have put swiss cheese on the bread
   5.900 agent.focus.chunk goal:sandwich object:ham
   5.900 agent.pm_new.clearFlag True
   5.900 agent.pm_new.clearFlag False
   5.900 agent.production parma_ham
   5.950 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   5.950 agent.focus.chunk goal:sandwich object:bread_top
   5.950 agent.pm_new.clearFlag True
   5.950 agent.pm_new.clearFlag False
   5.950 agent.production bread_top
   6.000 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   6.000 agent.focus.chunk goal:sandwich object:bread_bottom
   6.000 agent.production bread_bottom
   6.050 agent.production None
I have a piece of bread
   6.050 agent.focus.chunk goal:sandwich object:cheese
   6.050 agent.production swiss_cheese
   6.100 agent.production None
I have put swiss cheese on the bread
   6.100 agent.focus.chunk goal:sandwich object:ham
   6.100 agent.pm_new.clearFlag True
   6.100 agent.pm_new.clearFlag False
   6.100 agent.production maple_ham
   6.150 agent.production None
I have put maple ham on the cheese
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
   6.150 agent.focus.chunk goal:sandwich object:bread_top
   6.150 agent.pm_new.clearFlag True
   6.150 agent.pm_new.clearFlag False
   6.150 agent.production bread_top
   6.200 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   6.200 agent.focus.chunk goal:sandwich object:bread_bottom
   6.200 agent.production bread_bottom
   6.250 agent.production None
Traceback (most recent call last):
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_utility.py", line 71, in <module>
    subway.run()                               # run the environment
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/model.py", line 247, in run
    self.sch.run()
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/scheduler.py", line 116, in run
    self.do_event(heapq.heappop(self.queue))
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/scheduler.py", line 161, in do_event
    result=event.func(*event.args,**event.keys)
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/actr/core.py", line 55, in _process_productions
    self.log.production=None
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/logger.py", line 173, in __setattr__
    getattr(self,key)._set(value)
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/logger.py", line 201, in _set
    self._log.set(self._prefix,value)
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/logger.py", line 112, in set
    self.display_value(key,value)
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/logger.py", line 120, in display_value
    print('%8.3f %s %s'%(self.time,key,value))
KeyboardInterrupt
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_utility.py
   0.000 agent.production_match_delay 0
   0.000 agent.production_threshold None
   0.000 agent.production_time 0.05
   0.000 agent.production_time_sd None
   0.000 agent.pm_new.alpha 0.2
   0.000 agent.pm_new.clearFlag False
   0.000 agent.pm_noise.noise 0.1
   0.000 agent.pm_noise.baseNoise 0
   0.000 agent.production bread_bottom
   0.050 agent.production None
I have a piece of bread
   0.050 agent.focus.chunk goal:sandwich object:cheese
   0.050 agent.production swiss_cheese
   0.100 agent.production None
I have put swiss cheese on the bread
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
   0.100 agent.focus.chunk goal:sandwich object:ham
   0.100 agent.pm_new.clearFlag True
   0.100 agent.pm_new.clearFlag False
   0.100 agent.production maple_ham
   0.150 agent.production None
I have put maple ham on the cheese
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
   0.150 agent.focus.chunk goal:sandwich object:bread_top
   0.150 agent.pm_new.clearFlag True
   0.150 agent.pm_new.clearFlag False
   0.150 agent.production bread_top
   0.200 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   0.200 agent.focus.chunk goal:sandwich object:bread_bottom
   0.200 agent.production bread_bottom
   0.250 agent.production None
I have a piece of bread
   0.250 agent.focus.chunk goal:sandwich object:cheese
   0.250 agent.production cheddar_cheese
   0.300 agent.production None
I have put cheddar cheese on the bread
CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
   0.300 agent.focus.chunk goal:sandwich object:ham
   0.300 agent.pm_new.clearFlag True
   0.300 agent.pm_new.clearFlag False
   0.300 agent.production maple_ham
   0.350 agent.production None
I have put maple ham on the cheese
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
   0.350 agent.focus.chunk goal:sandwich object:bread_top
   0.350 agent.pm_new.clearFlag True
   0.350 agent.pm_new.clearFlag False
   0.350 agent.production bread_top
   0.400 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   0.400 agent.focus.chunk goal:sandwich object:bread_bottom
   0.400 agent.production bread_bottom
   0.450 agent.production None
I have a piece of bread
   0.450 agent.focus.chunk goal:sandwich object:cheese
   0.450 agent.production swiss_cheese
   0.500 agent.production None
I have put swiss cheese on the bread
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
   0.500 agent.focus.chunk goal:sandwich object:ham
   0.500 agent.pm_new.clearFlag True
   0.500 agent.pm_new.clearFlag False
   0.500 agent.production maple_ham
   0.550 agent.production None
I have put maple ham on the cheese
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
   0.550 agent.focus.chunk goal:sandwich object:bread_top
   0.550 agent.pm_new.clearFlag True
   0.550 agent.pm_new.clearFlag False
   0.550 agent.production bread_top
   0.600 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   0.600 agent.focus.chunk goal:sandwich object:bread_bottom
   0.600 agent.production bread_bottom
   0.650 agent.production None
I have a piece of bread
   0.650 agent.focus.chunk goal:sandwich object:cheese
   0.650 agent.production swiss_cheese
   0.700 agent.production None
I have put swiss cheese on the bread
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
   0.700 agent.focus.chunk goal:sandwich object:ham
   0.700 agent.pm_new.clearFlag True
   0.700 agent.pm_new.clearFlag False
   0.700 agent.production parma_ham
   0.750 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   0.750 agent.focus.chunk goal:sandwich object:bread_top
   0.750 agent.pm_new.clearFlag True
   0.750 agent.pm_new.clearFlag False
   0.750 agent.production bread_top
   0.800 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   0.800 agent.focus.chunk goal:sandwich object:bread_bottom
   0.800 agent.production bread_bottom
   0.850 agent.production None
I have a piece of bread
   0.850 agent.focus.chunk goal:sandwich object:cheese
   0.850 agent.production swiss_cheese
   0.900 agent.production None
I have put swiss cheese on the bread
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
   0.900 agent.focus.chunk goal:sandwich object:ham
   0.900 agent.pm_new.clearFlag True
   0.900 agent.pm_new.clearFlag False
   0.900 agent.production maple_ham
   0.950 agent.production None
I have put maple ham on the cheese
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
   0.950 agent.focus.chunk goal:sandwich object:bread_top
   0.950 agent.pm_new.clearFlag True
   0.950 agent.pm_new.clearFlag False
   0.950 agent.production bread_top
   1.000 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   1.000 agent.focus.chunk goal:sandwich object:bread_bottom
   1.000 agent.production bread_bottom
   1.050 agent.production None
I have a piece of bread
   1.050 agent.focus.chunk goal:sandwich object:cheese
   1.050 agent.production swiss_cheese
   1.100 agent.production None
I have put swiss cheese on the bread
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
   1.100 agent.focus.chunk goal:sandwich object:ham
   1.100 agent.pm_new.clearFlag True
   1.100 agent.pm_new.clearFlag False
   1.100 agent.production parma_ham
   1.150 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   1.150 agent.focus.chunk goal:sandwich object:bread_top
   1.150 agent.pm_new.clearFlag True
   1.150 agent.pm_new.clearFlag False
   1.150 agent.production bread_top
   1.200 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   1.200 agent.focus.chunk goal:sandwich object:bread_bottom
   1.200 agent.production bread_bottom
   1.250 agent.production None
I have a piece of bread
   1.250 agent.focus.chunk goal:sandwich object:cheese
   1.250 agent.production swiss_cheese
   1.300 agent.production None
I have put swiss cheese on the bread
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
   1.300 agent.focus.chunk goal:sandwich object:ham
   1.300 agent.pm_new.clearFlag True
   1.300 agent.pm_new.clearFlag False
   1.300 agent.production parma_ham
   1.350 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   1.350 agent.focus.chunk goal:sandwich object:bread_top
   1.350 agent.pm_new.clearFlag True
   1.350 agent.pm_new.clearFlag False
   1.350 agent.production bread_top
   1.400 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   1.400 agent.focus.chunk goal:sandwich object:bread_bottom
   1.400 agent.production bread_bottom
   1.450 agent.production None
I have a piece of bread
   1.450 agent.focus.chunk goal:sandwich object:cheese
   1.450 agent.production cheddar_cheese
   1.500 agent.production None
I have put cheddar cheese on the bread
CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
   1.500 agent.focus.chunk goal:sandwich object:ham
   1.500 agent.pm_new.clearFlag True
   1.500 agent.pm_new.clearFlag False
   1.500 agent.production parma_ham
   1.550 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   1.550 agent.focus.chunk goal:sandwich object:bread_top
   1.550 agent.pm_new.clearFlag True
   1.550 agent.pm_new.clearFlag False
   1.550 agent.production bread_top
   1.600 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   1.600 agent.focus.chunk goal:sandwich object:bread_bottom
   1.600 agent.production bread_bottom
   1.650 agent.production None
I have a piece of bread
   1.650 agent.focus.chunk goal:sandwich object:cheese
   1.650 agent.production swiss_cheese
   1.700 agent.production None
I have put swiss cheese on the bread
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
   1.700 agent.focus.chunk goal:sandwich object:ham
   1.700 agent.pm_new.clearFlag True
   1.700 agent.pm_new.clearFlag False
   1.700 agent.production maple_ham
   1.750 agent.production None
I have put maple ham on the cheese
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
   1.750 agent.focus.chunk goal:sandwich object:bread_top
   1.750 agent.pm_new.clearFlag True
   1.750 agent.pm_new.clearFlag False
   1.750 agent.production bread_top
   1.800 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   1.800 agent.focus.chunk goal:sandwich object:bread_bottom
   1.800 agent.production bread_bottom
   1.850 agent.production None
I have a piece of bread
   1.850 agent.focus.chunk goal:sandwich object:cheese
   1.850 agent.production swiss_cheese
   1.900 agent.production None
I have put swiss cheese on the bread
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
   1.900 agent.focus.chunk goal:sandwich object:ham
   1.900 agent.pm_new.clearFlag True
   1.900 agent.pm_new.clearFlag False
   1.900 agent.production maple_ham
   1.950 agent.production None
I have put maple ham on the cheese
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
   1.950 agent.focus.chunk goal:sandwich object:bread_top
   1.950 agent.pm_new.clearFlag True
   1.950 agent.pm_new.clearFlag False
   1.950 agent.production bread_top
   2.000 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   2.000 agent.focus.chunk goal:sandwich object:bread_bottom
   2.000 agent.production bread_bottom
   2.050 agent.production None
I have a piece of bread
   2.050 agent.focus.chunk goal:sandwich object:cheese
   2.050 agent.production swiss_cheese
   2.100 agent.production None
I have put swiss cheese on the bread
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
   2.100 agent.focus.chunk goal:sandwich object:ham
   2.100 agent.pm_new.clearFlag True
   2.100 agent.pm_new.clearFlag False
   2.100 agent.production parma_ham
   2.150 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   2.150 agent.focus.chunk goal:sandwich object:bread_top
   2.150 agent.pm_new.clearFlag True
   2.150 agent.pm_new.clearFlag False
   2.150 agent.production bread_top
   2.200 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   2.200 agent.focus.chunk goal:sandwich object:bread_bottom
   2.200 agent.production bread_bottom
   2.250 agent.production None
I have a piece of bread
   2.250 agent.focus.chunk goal:sandwich object:cheese
   2.250 agent.production swiss_cheese
   2.300 agent.production None
I have put swiss cheese on the bread
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
   2.300 agent.focus.chunk goal:sandwich object:ham
   2.300 agent.pm_new.clearFlag True
   2.300 agent.pm_new.clearFlag False
   2.300 agent.production parma_ham
   2.350 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   2.350 agent.focus.chunk goal:sandwich object:bread_top
   2.350 agent.pm_new.clearFlag True
   2.350 agent.pm_new.clearFlag False
   2.350 agent.production bread_top
   2.400 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   2.400 agent.focus.chunk goal:sandwich object:bread_bottom
   2.400 agent.production bread_bottom
   2.450 agent.production None
I have a piece of bread
   2.450 agent.focus.chunk goal:sandwich object:cheese
   2.450 agent.production cheddar_cheese
   2.500 agent.production None
I have put cheddar cheese on the bread
CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
   2.500 agent.focus.chunk goal:sandwich object:ham
   2.500 agent.pm_new.clearFlag True
   2.500 agent.pm_new.clearFlag False
   2.500 agent.production parma_ham
   2.550 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   2.550 agent.focus.chunk goal:sandwich object:bread_top
   2.550 agent.pm_new.clearFlag True
   2.550 agent.pm_new.clearFlag False
   2.550 agent.production bread_top
   2.600 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   2.600 agent.focus.chunk goal:sandwich object:bread_bottom
   2.600 agent.production bread_bottom
   2.650 agent.production None
I have a piece of bread
   2.650 agent.focus.chunk goal:sandwich object:cheese
   2.650 agent.production swiss_cheese
   2.700 agent.production None
I have put swiss cheese on the bread
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
   2.700 agent.focus.chunk goal:sandwich object:ham
   2.700 agent.pm_new.clearFlag True
   2.700 agent.pm_new.clearFlag False
   2.700 agent.production parma_ham
   2.750 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   2.750 agent.focus.chunk goal:sandwich object:bread_top
   2.750 agent.pm_new.clearFlag True
   2.750 agent.pm_new.clearFlag False
   2.750 agent.production bread_top
   2.800 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   2.800 agent.focus.chunk goal:sandwich object:bread_bottom
   2.800 agent.production bread_bottom
   2.850 agent.production None
I have a piece of bread
   2.850 agent.focus.chunk goal:sandwich object:cheese
   2.850 agent.production swiss_cheese
   2.900 agent.production None
I have put swiss cheese on the bread
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
   2.900 agent.focus.chunk goal:sandwich object:ham
   2.900 agent.pm_new.clearFlag True
   2.900 agent.pm_new.clearFlag False
   2.900 agent.production parma_ham
   2.950 agent.production None
I have put parma ham on the cheese
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
   2.950 agent.focus.chunk goal:sandwich object:bread_top
   2.950 agent.pm_new.clearFlag True
   2.950 agent.pm_new.clearFlag False
   2.950 agent.production bread_top
   3.000 agent.production None
I have put bread on the ham
I have made a ham and cheese sandwich
   3.000 agent.focus.chunk goal:sandwich object:bread_bottom
   3.000 agent.production bread_bottom
   3.050 agent.production None
I have a piece of bread
   3.050 agent.focus.chunk goal:sandwich object:cheese
   3.050 agent.production cheddar_cheese
   3.100 agent.production None
I have put cheddar cheese on the bread
CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
   3.100 agent.focus.chunk goal:sandwich object:ham
Traceback (most recent call last):
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_utility.py", line 73, in <module>
    subway.run()                               # run the environment
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/model.py", line 247, in run
    self.sch.run()
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/scheduler.py", line 116, in run
    self.do_event(heapq.heappop(self.queue))
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/scheduler.py", line 161, in do_event
    result=event.func(*event.args,**event.keys)
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/actr/core.py", line 57, in _process_productions
    choice.fire(self._context)
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/production.py", line 49, in fire
    exec(self.func, context,self.bound)
  File "<production-cheddar_cheese>", line 4, in <module>
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/model.py", line 20, in __call__
    val=self.func(self.obj,*args,**keys)
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/actr/buffer.py", line 48, in set
    self.chunk=Chunk(chunk,self.sch.bound)
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/model.py", line 226, in __setattr__
    if self.log: setattr(self.log,key,value)
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/logger.py", line 173, in __setattr__
    getattr(self,key)._set(value)
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/logger.py", line 201, in _set
    self._log.set(self._prefix,value)
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/logger.py", line 112, in set
    self.display_value(key,value)
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/logger.py", line 120, in display_value
    print('%8.3f %s %s'%(self.time,key,value))
KeyboardInterrupt
>>> 