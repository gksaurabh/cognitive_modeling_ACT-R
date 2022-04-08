from python_actr import *  

class Subway(Model):        
    bread=Model(isa='bread',location='on_counter')
    cheese=Model(isa='cheese',location='on_counter')
    ham=Model(isa='ham',location='on_counter')
    bread_top=Model(isa='bread_top',location='on_counter')

class MotorModule(Model):     
    def do_bread_bottom(self):         
        yield 2                   
        print("done the bread")
        self.parent.parent.bread.location='on_plate'    
    def do_cheese(self):     
        yield 3                   
        print("done the cheese")
        self.parent.parent.cheese.location='on_plate'   
    def do_ham(self):     
        yield 2.5
        print("done the ham")
        self.parent.parent.ham.location='on_plate'
    def do_bread_top(self):         
        yield 2                   
        print("done the bread")
        self.parent.parent.bread_top.location='on_plate' 
        
class MyAgent(ACTR):    
    focus=Buffer()
    focus.set('goal:sandwich object:bread_bottom')
    motor=MotorModule()

    def bread_bottom(focus='goal:sandwich object:bread_bottom'):
        print("I will do bread on bottom") 
        motor.do_bread_bottom()
        focus.set('goal:sandwich object:cheese')
        
    def cheese(focus='goal:sandwich object:cheese', bread='location:on_plate'):          
        print("I will do cheese")      
        motor.do_cheese()
        focus.set('goal:sandwich object:ham')
        
    def maple_ham(focus='goal:sandwich object:ham', cheese='location:on_plate'):
        print("I will do ham")
        motor.do_ham()
        focus.set('goal:sandwich object:bread_top')

    def bread_top(focus='goal:sandwich object:bread_top', ham='location:on_plate'):
        print("I will do bread on top")
        focus.set('goal:sandwich object:none state:finished')
        motor.do_bread_top()

    def finished(focus='goal:sandwich object:none state:finished', bread_top='location:on_plate'):
        print("I have made a ham and cheese sandwich")
        focus.set('goal:sandwich state:simulation_over')
        

tim=MyAgent()
env=Subway()
env.agent=tim 
log_everything(env)

env.run()

