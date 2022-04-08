from python_actr import *  


class MyEnvironment(Model):
    pass


class MyAgent(ACTR):
    
    focus=Buffer()
    DMbuffer=Buffer()

    DM=Memory(DMbuffer,latency=0.05,threshold=25,finst_size=10,finst_time=30.0)

    DMNoise(DM,noise=2.0)            # turn on for DM subsymbolic processing
    DMBaseLevel(DM,decay=0.5)       # turn on for DM subsymbolic processing

    focus.set('task:sandwich object:bread_bottom')

    DM.add('condiment:mustard')
    DM.add('condiment:ketchup')


    def bread_bottom(focus='task:sandwich object:bread_bottom'):# if focus buffer has this chunk then....
        print("I have a piece of bread")                 # print the action
        focus.set('task:sandwich object:cheese')

    def cheese(focus='task:sandwich object:cheese'):            # the rest of the productions are the same
        print("I have put cheese on the bread")          # but carry out different actions
        focus.set('task:sandwich object:ham')

    def ham(focus='task:sandwich object:ham'):
        print("I have put  ham on the cheese")
        focus.set('task:sandwich object:condiment')

    def condiment_DM_request(focus='task:sandwich object:condiment'):
        print("recalling the condiment")
        DM.request('condiment:?condiment')
        focus.set('task:recall')

    def DM_retrieve(focus='task:recall', DMbuffer='condiment:?condiment'):
        print("I recall they wanted....")
        print(condiment)
        DM.request('condiment:?condiment')
        DMbuffer.set('state:empty')
        focus.set('task:sandwich object:bread_top')

#    def recall_condiment(focus='task:sandwich action:recall_condiment'):
#        print("recalling the order")
#        DM.request('condiment:?')
#        focus.set('task:sandwich object:condiment') 

    def forgot(focus='task:recall', DMbuffer=None, DM='error:True'):
                                           # DMbuffer=none means the buffer is empty
                                           # DM='error:True' means the search was unsucessful
        print('I recall they wanted.......')
        print("I forgot")
        focus.set('stop')

    def condiment(focus='task:sandwich object:condiment', DMbuffer='condiment:?condiment'):  # match to DMbuffer as well
        print("I recall they wanted.......")        
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
log_everything(subway)
subway.run()                               # run the environment
