from python_actr import *  


class MyEnvironment(Model):
    pass


class MyAgent(ACTR):
    
    focus=Buffer()
    DMbuffer=Buffer()

    DM=Memory(DMbuffer,latency=0.05,threshold=2,finst_size=10,finst_time=30.0)

    dm_n=DMNoise(DM,noise=0.0)            # turn on for DM subsymbolic processing
    dm_bl=DMBaseLevel(DM,decay=0.5)       # turn on for DM subsymbolic processing

    focus.set('goal:sandwich object:bread_bottom')

    DM.add('condiment:mustard')
    DM.add('condiment:ketchup',baselevel=1)


    def bread_bottom(focus='goal:sandwich object:bread_bottom'):# if focus buffer has this chunk then....
        print("I have a piece of bread")                 # print the action
        focus.set('goal:sandwich object:cheese')
        DM.add('customer:mary condiment:ketcup')
        DM.add('customer:lary condiment:mustard')
        DM.add('customer:pary condiment:ketcup')
        DM.add('customer:bary condiment:mustard')
        DM.add('customer:tary condiment:ketcup')
        DM.add('customer:shary condiment:mustard')
        DM.add('customer:faary condiment:ketcup')
        DM.add('customer:gary condiment:mustard')

    def cheese(focus='goal:sandwich object:cheese'):            # the rest of the productions are the same
        print("I have put cheese on the bread")          # but carry out different actions
        focus.set('goal:sandwich object:ham')
        DM.add('customer:mary condiment:ketcup')
        DM.add('customer:lary condiment:mustard')
        DM.add('customer:pary condiment:ketcup')
        DM.add('customer:bary condiment:mustard')
        DM.add('customer:tary condiment:ketcup')
        DM.add('customer:shary condiment:mustard')
        DM.add('customer:faary condiment:ketcup')
        DM.add('customer:gary condiment:mustard')
        

    def ham(focus='goal:sandwich object:ham'):
        print("I have put  ham on the cheese")
        focus.set('goal:sandwich action:recall_condiment')
        DM.add('customer:mary condiment:ketcup')
        DM.add('customer:lary condiment:mustard')
        DM.add('customer:pary condiment:ketcup')
        DM.add('customer:bary condiment:mustard')
        DM.add('customer:tary condiment:ketcup')
        DM.add('customer:shary condiment:mustard')
        DM.add('customer:faary condiment:ketcup')
        DM.add('customer:gary condiment:mustard')

    def recall_condiment(focus='goal:sandwich action:recall_condiment'):
        print("recalling the order")
        DM.request('condiment:?')
        focus.set('goal:sandwich object:condiment') 

    def forgot(focus='sandwich condiment', DMbuffer=None, DM='error:True'):
                                           # DMbuffer=none means the buffer is empty
                                           # DM='error:True' means the search was unsucessful
        print('I recall they wanted.......')
        print("I forgot")
        focus.set('stop')

    def condiment(focus='goal:sandwich object:condiment', DMbuffer='condiment:?condiment'):  # match to DMbuffer as well
        print("I recall they wanted.......")        
        print (condiment)             
        print("i have put the condiment on the sandwich")
        focus.set('goal:sandwich object:bread_top')

    def bread_top(focus='goal:sandwich object:bread_top'):
        print("I have put bread on the ham")
        print("I have made a ham and cheese sandwich")
        focus.set('sandwich_step:stop')   

tim=MyAgent()                              # name the agent
subway=MyEnvironment()                     # name the environment
subway.agent=tim                           # put the agent in the environment
log_everything(subway)
subway.run()                               # run the environment
