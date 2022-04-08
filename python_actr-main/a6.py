Python 3.9.5 (v3.9.5:0a7dcbdb13, May  3 2021, 13:17:02) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_DM.py
I have a piece of bread
I have put cheese on the bread
I have put  ham on the cheese
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
I have put bread on the ham
I have made a ham and cheese sandwich
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_DM.py
I have a piece of bread
I recall they wanted......
Traceback (most recent call last):
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_DM.py", line 59, in <module>
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
  File "<production-cheese>", line 3, in <module>
NameError: name 'cheese' is not defined
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_DM.py
I have a piece of bread
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_DM.py
I have a piece of bread
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_DM.py
I have a piece of bread
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_DM.py
Traceback (most recent call last):
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_DM.py", line 58, in <module>
    subway.agent=tim                           # put the agent in the environment
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/model.py", line 198, in __setattr__
    self._ensure_converted()
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/model.py", line 270, in _ensure_converted
    self.__convert()
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/model.py", line 185, in __convert
    v.__convert(parent=self)
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/model.py", line 133, in __convert
    self._convert_info(objects,methods)
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/production.py", line 67, in _convert_info
    p=Production(self,k,v)
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/production.py", line 31, in __init__
    self.pattern=pattern.Pattern(patterns)
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/pattern.py", line 49, in __init__
    self.funcs=parse(patterns,bound)
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/pattern.py", line 122, in parse
    raise PatternException("Found unnamed slot '%s' after named slot in pattern '%s'"%(text,pattern))
python_actr.pattern.PatternException: Found unnamed slot 'cheese' after named slot in pattern '['goal:sandwich cheese']'
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_DM.py
I have a piece of bread
recalling the order
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_DM.py
I have a piece of bread
recalling the order
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_DM.py
I have a piece of bread
recalling the order
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_DM.py
I have a piece of bread
recalling the order
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_DM.py
I have a piece of bread
recalling the order
I recall they wanted......
cheddar
I have put the cheese on the sandwich
I have put  ham on the cheese
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
I have put bread on the ham
I have made a ham and cheese sandwich
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_DM.py
I have a piece of bread
recalling the order
I recall they wanted......
swiss
I have put the cheese on the sandwich
I have put  ham on the cheese
recalling the order
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_DM.py
I have a piece of bread
recalling the order
I recall they wanted......
swiss
I have put the cheese on the sandwich
I have put  ham on the cheese
recalling the order
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_DM.py
I have a piece of bread
recalling the order
I recall they wanted......
cheddar
I have put the cheese on the sandwich
I have put  ham on the cheese
recalling the order
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_DM.py
I have a piece of bread
recalling the order
I recall they wanted......
cheddar
I have put the cheese on the sandwich
I have put  ham on the cheese
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
I have put bread on the ham
I have made a ham and cheese sandwich
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_DM.py
Traceback (most recent call last):
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_DM.py", line 58, in <module>
    subway.run()                               # run the environment
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/model.py", line 247, in run
    self.sch.run()
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/scheduler.py", line 116, in run
    self.do_event(heapq.heappop(self.queue))
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/scheduler.py", line 161, in do_event
    result=event.func(*event.args,**event.keys)
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/actr/core.py", line 16, in _process_productions
    self._calc_context()
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/production.py", line 90, in _calc_context
    raise ProductionException("Production is matching on an unknown module '%s'"%(keys))
python_actr.production.ProductionException: Production is matching on an unknown module '{'ocus'}'
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_DM.py
I have a piece of bread
I have put cheddar cheese on the bread
I have put  ham on the cheese
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
I have put bread on the ham
I have made a ham and cheese sandwich
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_DM.py
I have a piece of bread
I have put feta cheese on the bread
I have put  ham on the cheese
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
I have put bread on the ham
I have made a ham and cheese sandwich
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_DM.py
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_DM.py
I have a piece of bread
I have put cheddar cheese on the bread
I have put  ham on the cheese
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
I have put bread on the ham
I have made a ham and cheese sandwich
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_DM.py
I have a piece of bread
I have put cheddar cheese on the bread
I have put  ham on the cheese
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
I have put bread on the ham
I have made a ham and cheese sandwich
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_DM.py
I have a piece of bread
I have put feta cheese on the bread
I have put  ham on the cheese
recalling the order
Traceback (most recent call last):
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_DM.py", line 58, in <module>
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
  File "<production-recall_condiment>", line 3, in <module>
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/model.py", line 20, in __call__
    val=self.func(self.obj,*args,**keys)
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/actr/dm.py", line 64, in request
    pattern=Pattern(pattern,b,partial=partial)
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/pattern.py", line 49, in __init__
    self.funcs=parse(patterns,bound)
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/pattern.py", line 170, in parse
    raise PatternException("Unknown text '%s' in pattern '%s'"%(text,pattern))
python_actr.pattern.PatternException: Unknown text '?!ketchup' in pattern '['condiment:?!ketchup']'
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_DM.py
Traceback (most recent call last):
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_DM.py", line 57, in <module>
    subway.agent=tim                           # put the agent in the environment
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/model.py", line 198, in __setattr__
    self._ensure_converted()
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/model.py", line 270, in _ensure_converted
    self.__convert()
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/model.py", line 185, in __convert
    v.__convert(parent=self)
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/model.py", line 133, in __convert
    self._convert_info(objects,methods)
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/production.py", line 67, in _convert_info
    p=Production(self,k,v)
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/production.py", line 31, in __init__
    self.pattern=pattern.Pattern(patterns)
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/pattern.py", line 49, in __init__
    self.funcs=parse(patterns,bound)
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/python_actr/pattern.py", line 170, in parse
    raise PatternException("Unknown text '%s' in pattern '%s'"%(text,pattern))
python_actr.pattern.PatternException: Unknown text '?!ketchup' in pattern '['condiment:?!ketchup']'
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_DM.py
I have a piece of bread
I have put feta cheese on the bread
I have put  ham on the cheese
recalling the order
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_DM.py
I have a piece of bread
I have put cheddar cheese on the bread
I have put  ham on the cheese
recalling the order
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_DM.py
I have a piece of bread
I have put cheddar cheese on the bread
I have put  ham on the cheese
recalling the order
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_DM.py
I have a piece of bread
I have put feta cheese on the bread
I have put  ham on the cheese
recalling the order
I recall they wanted.......
Traceback (most recent call last):
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_DM.py", line 58, in <module>
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
  File "<production-condiment>", line 3, in <module>
NameError: name 'condiment' is not defined
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_DM.py
I have a piece of bread
I have put cheddar cheese on the bread
I have put  ham on the cheese
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
I have put bread on the ham
I have made a ham and cheese sandwich
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_DM.py
I have a piece of bread
I have put cheddar cheese on the bread
I have put  ham on the cheese
recalling the order
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_refraction.py
I have a piece of bread
I have put cheese on the bread
I have put  ham on the cheese
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
relish
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
relish
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
relish
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
relish
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
relish
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
relish
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
relish
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
relish
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
relish
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
relish
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
relish
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
relish
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
relish
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
relish
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
relish
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
relish
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
recalling the order
Traceback (most recent call last):
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_refraction.py", line 54, in <module>
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
  File "<production-recall_condiment>", line 2, in <module>
KeyboardInterrupt
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_refraction.py
I have a piece of bread
I have put cheese on the bread
I have put  ham on the cheese
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
relish
i have put the condiment on the sandwich
recalling the order
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_refraction.py
I have a piece of bread
I have put cheese on the bread
I have put  ham on the cheese
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
relish
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
relish
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
relish
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
relish
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
relish
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
relish
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
relish
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
relish
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
relish
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
relish
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
relish
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
relish
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
relish
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
relish
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
relish
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
relish
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
relish
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
relish
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
relish
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
relish
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
relishTraceback (most recent call last):
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_refraction.py", line 54, in <module>
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
  File "<production-condiment>", line 3, in <module>
KeyboardInterrupt
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_refraction.py
I have a piece of bread
I have put cheese on the bread
I have put  ham on the cheese
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
croutons
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
chipotle
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
light_mayo
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
honey_mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mayo
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
honey_mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
salt&pepper
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
relish
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
light_mayo
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
bbq_sauce
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
relish
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
light_mayo
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
honey_mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
light_mayo
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
bbq_sauce
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
honey_mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
croutons
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
bbq_sauce
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
chipotle
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
salt&pepper
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
bbq_sauce
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mayo
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
croutons
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
bbq_sauce
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mayo
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
relish
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
honey_mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mayo
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
chipotle
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
light_mayo
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
croutons
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
salt&pepper
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
light_mayo
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
salt&pepper
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mayo
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
croutons
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
chipotle
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
salt&pepper
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
croutons
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
light_mayo
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mayo
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
honey_mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
chipotle
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
light_mayo
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
croutons
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
relish
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
bbq_sauce
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
chipotle
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
honey_mustard
Traceback (most recent call last):
  File "/Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_refraction.py", line 61, in <module>
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
  File "<production-condiment>", line 3, in <module>
KeyboardInterrupt
>>> 
= RESTART: /Users/saurabhkishore/Desktop/Carleton/Winter2022/CGSC-4601/python_actr-main/simple_refraction.py
I have a piece of bread
I have put cheese on the bread
I have put  ham on the cheese
recalling the order
I recall they wanted.......
ketchup
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
light_mayo
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
relish
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
salt&pepper
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
croutons
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
bbq_sauce
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
honey_mustard
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
chipotle
i have put the condiment on the sandwich
recalling the order
I recall they wanted.......
mayo
i have put the condiment on the sandwich
recalling the order
>>> 