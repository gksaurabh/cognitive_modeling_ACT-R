#################### ham cheese production model ###################

# this is the simplest type of act-r model
# it uses only the production system and one buffer
# the buffer represents the focus of thought
# we call it the focus buffer but it is often called the task buffer
# productions fire if they match the focus buffer
# each production changes the contents of focus buffer so a different production will fire on the next cycle


from python_actr import *

class MyEnvironment(Model):
    something=Model(isa='something',state='not_done')

class MotorModule(Model):     
    def do_something(self):         
        #yield 2                   
        print("doing somethiing")
        self.parent.parent.something.state='done'
    def reset(self):         
        #yield 2                   
        print("doing reset")
        self.parent.parent.something.state='not_done'

class MyAgent(ACTR):
    motor=MotorModule()
    focus=Buffer()
    DMbuffer=Buffer() 
    DM=Memory(DMbuffer,threshold=-15)            
    DMNoise(DM,noise=0.1)
    DMBaseLevel(DM,decay=0.5)

    partial=Partial(DM,strength=1.0,limit=-1.0) 
    partial.similarity('mary','brian',-0.9)   
    partial.similarity('mary','tony',-0.01)
    partial.similarity('tony','minion',-0.9)   
    partial.similarity('minion','hairy',-0.01)
    partial.similarity('hairy','boney',-0.01)
    
    focus.set('task:sandwich object:bread_bottom')
    
    DM.add('customer:brian condiment:mustard')
    DM.add('customer:mary condiment:ketchup')
    DM.add('customer:tony condiment:mayonase')
    DM.add('customer:minion condiment:chipotle')
    DM.add('customer:hairy condiment:relish')
    DM.add('customer:boney condiment:ranch')
    

    def bread_bottom(focus='task:sandwich object:bread_bottom'):
        print("I have a piece of bread") 
        focus.set('task:sandwich object:cheese')
        motor.do_something()

    def cheese(focus='task:sandwich object:cheese', something='state:done'):          
        print("I have put cheese on the bread")      
        focus.set('task:sandwich object:ham')
##        DM.add('customer:brian condiment:mustard')
##        DM.add('customer:mary condiment:ketchup')
        motor.reset()
        motor.do_something()

    def ham(focus='task:sandwich object:ham', something='state:done'):
        print("I have put  ham on the cheese")
        focus.set('customer:mary object:condiment_choice') ###

    def condiment_DM_request(focus='customer:?customer object:condiment_choice'):
        print("recalling the condiment for...")
        print(customer)
        DM.request('customer:?customer condiment:?condiment')
        focus.set('task:recall') 

    def DM_retrieve(focus='task:recall',DMbuffer='condiment:?condiment'): 
        print("I recall they wanted.......")                            
        print(condiment)
        DMbuffer.set('state:empty')
        focus.set('task:sandwich object:bread_top')

    def forgot(focus='task:recall', DM='error:True',DMbuffer=None):
        print("I recall they wanted.......")
        print ("I forgot")
        focus.set('task:sandwich object:none')

    def bread_top(focus='task:sandwich object:bread_top'): ###
        print("I have put bread on the ham")
        print("I have made a ham and cheese sandwich")
        focus.set('task:sandwich object:none')


tim=MyAgent()                              # name the agent
subway=MyEnvironment()                     # name the environment
subway.agent=tim                           # put the agent in the environment
log_everything(subway)                 # print out what happens in the environment

subway.run()                               # run the environment
