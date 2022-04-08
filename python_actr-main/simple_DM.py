from python_actr import *  


class MyEnvironment(Model):
    pass


class MyAgent(ACTR):
    
    focus=Buffer()
    DMbuffer=Buffer()

    DM=Memory(DMbuffer)
    
    focus.set('task:sandwich object:bread_bottom')
    DMbuffer.set('state:empty')
    

    DM.add('condiment:mustard taste:good')
    DM.add('condiment:ketchup taste:bad')
    

    def bread_bottom(focus='task:sandwich object:bread_bottom'):# if focus buffer has this chunk then....
        print("I have a piece of bread")                 # print the action
        focus.set('task:sandwich object:cheese')                # change chunk in focus buffer

    def cheddar_cheese(focus='task:sandwich object:cheese'):            # the rest of the productions are the same
        print("I have put cheddar cheese on the bread")          # but carry out different actions
        focus.set('task:sandwich object:ham')

    def feta_cheese(focus='task:sandwich object:cheese'):            # the rest of the productions are the same
        print("I have put feta cheese on the bread")          # but carry out different actions
        focus.set('task:sandwich object:ham')

    def ham(focus='task:sandwich object:ham'):
        print("I have put  ham on the cheese")
        focus.set('task:sandwich action:recall_condiment')

    def recall_condiment(focus='task:sandwich action:recall_condiment'):
        print("recalling the order")
        DM.request('condiment:?x')                # retrieve a chunk from DM into the DM buffer
        focus.set('sandwich condiment')         # ? means that slot can match any content

    def condiment(focus='sandwich condiment', DMbuffer='condiment:!ketchup?condiment'):  # match to DMbuffer as well
        print("I recall they wanted.......")                                # put slot 2 value in ?condiment
        print (condiment)             
        print("i have put the condiment on the sandwich")
        focus.set('task:sandwich object:bread_top')

    def bread_top(focus='task:sandwich object:bread_top'):
        print("I have put bread on the ham")
        print("I have made a ham and cheese sandwich")
        focus.set('sandwich_step:stop')   

tim=MyAgent()                              # name the agent
subway=MyEnvironment()                     # name the environment
subway.agent=tim                           # put the agent in the environment
subway.run()                               # run the environment
