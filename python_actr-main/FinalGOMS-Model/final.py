from python_actr import *


# The following model is a model of the Tim Hortons store with features such as a
# tea brewing machine, coffee machine, sandwich toaster, and a fryer. The model also
# contains bread, potato wedges, and old-fashioned donuts which you can get in a plate
# along with coffee or tea in a cup.

class TimHortons(Model):
    coffee_machine = Model(isa='coffee_machine', button= 'up')
    tea_brewer = Model(isa='tea_brewer', button= 'up')
    sandwich_toaster = Model(isa= 'sandwich_toaster', button= 'up')
    fryer = Model(isa= 'fryer', button= 'up')
    bread = Model(isa= 'bread', state='not_toasted', location='sandwich_toaster')
    potato_wedges = Model(isa= 'potato_wedges', state='not_fried', location='fryer')
    old_fashioned_donut = Model(isa='old_fashioned_donut', state='not_fried', location='fryer')
    cup = Model(isa='cup', state='empty', location='storage')
    plate = Model(isa='plate', state='empty', location='storage')

class ActionModule(Model):
    

    #Generic Actions
        # Generic actions that are performed by either 1 or more agents. For example
        # push action would be performed on multiple appliances in the kitchen such as
        # coffee machine or sandwich toaster or tea brewer or fryer to change the state
        # of these machines.
    def push(self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 2
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)
        
    def grab(self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 3
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)
        
    def pour(self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 5
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)

    def plate(self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 5
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)

    def fry(self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, 'in_progress')
        yield 5
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)
        
    def reset(self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)

    #appliance/agent specific actions
    def toast(self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x,slot_name, 'in_progress')
        yield 10
        setattr(x, slot_name, slot_value)
        print('-object=',env_object)
        print('-slot=',slot_name)
        print('-value=',slot_value)


# The following classes define the methods and attributes for each of the different
# appliances in the Tim Hortons store.
class Coffee_Machine(ACTR):
    production_time=0.0
    focus=Buffer()
    focus.set('state:off')
    action=ActionModule()

    #the coffee machine can turn on and off. Once it is turned on an action of pouring
    #is performed and the state of the machine is reset when it is turned off
    def On(focus='state:off',coffee_machine='button:down'):
        print('COFFEE_MACHINE:pouring coffee')
        action.pour('cup', 'state', 'full')
        focus.set('state:on')

    def Off(focus='state:on',cup='state:full'):
        print('COFFEE_MACHINE:reset button')
        action.reset('coffee_machine', 'button', 'up')
        focus.set('state:off')

class Tea_Brewer(ACTR):
    production_time=0.0
    focus=Buffer()
    focus.set('state:off')
    action=ActionModule()

    #the brewer can turn on and off. Once it is turned on an action of pouring
    #is performed and the state of the machine is reset when it is turned off
    def On(focus='state:off',coffee_machine='button:down'):
        print('TEA_BREWER:pouring tea')
        action.pour('cup', 'state', 'full')
        focus.set('state:on')

    def Off(focus='state:on',cup='state:full'):
        print('TEA_BREWER:reset button')
        action.reset('tea_brewer', 'button', 'up')
        focus.set('state:off')


class Sandwich_Toaster(ACTR):
    production_time=0.0
    focus=Buffer()
    focus.set('state:off')
    action=ActionModule()

    #the toaster can turn on and off. Once it is turned on an action of toasting
    #is performed and the state of the machine is reset when it is turned off
    def On(focus='state:off', sandwich_toaster='button:down'):
        print('SANDWICH_TOASTER:toasting bread')
        action.toast('bread','state','toasted')
        focus.set('state:on')
        
    def Off(focus='state:on', bread='state:toasted' ):
        print('SANDWICH_TOASTER:reset button')
        action.reset('sandwich_toaster', 'button', 'up')
        focus.set('state:off')

#This fryer class determines the attributes and methods available to the fryer
class Fryer(ACTR):
    production_time=0.0
    focus=Buffer()
    focus.set('state:off')
    action=ActionModule()

    #the fryer can be turned on or off. Once it is turned on an action of frying a 
    #donut and poatato wedges is performed and the state of the machine is
    #reset when it is turned off
    def On(focus='state:off', fryer='button:down'):
        print('FRYER:frying potato wedges')
        action.fry('potato_wedges','state','fried')
        action.fry('old_fashioned_donut','state','fried')
        focus.set('state:on')
        
    def Off(focus='state:on', potato_wedges='state:fried', old_fashioned_donut='state:fried'):
        print('FRYER:reset button')
        action.reset('fryer', 'button', 'up')
        focus.set('state:off')

#This human class starts the model and brews coffeem then tea, toasts bread, and
#then proceeds to fry donuts and potato wedges before plating them and puting
#all of the food and drinks on the counter.
class Human(ACTR):
    focus=Buffer()
    focus.set('state:start')
    action=ActionModule()

    def START(focus='state:start', cup='state:empty'):
        print('HUMAN: pushing coffee machine buton')
        action.push('coffee_machine', 'button', 'down')

        print('HUMAN: pushing tea brewer button')
        action.push('tea_brewer', 'button', 'down')
        
        print('HUMAN: pushing sandwich toaster button')
        action.push('sandwich_toaster', 'button', 'down')

        print('HUMAN: pushing fryer button')
        action.push('fryer', 'button', 'down')

        focus.set('state:wait1')

    def Grab_coffee(focus='state:wait1',cup='state:full'):
        print('HUMAN:grabbing the coffee')
        action.grab('cup', 'location', 'hand')
        print('HUMAN:placing coffee on counter')
        action.grab('cup', 'location', 'counter')
        focus.set('state:wait2')


    def Plate_food(focus='state:wait2',plate='state:empty'):
        print('HUMAN:grabbing the plate')
        action.grab('plate', 'location', 'hand')
        print('HUMAN:plating the food')
        action.plate('plate', 'state', 'full')
        print('HUMAN:placing the plate on counter')
        action.grab('plate', 'location', 'counter')
        focus.set('state:stop')

    

#instantiating members of each class before calling their respective method. 
saurabh=Human()
machine1=Coffee_Machine()
machine2=Tea_Brewer()
machine3=Sandwich_Toaster()
machine4=Fryer()

env=TimHortons()
env.agent=saurabh
env.agent=machine1
env.agent=machine2
env.agent=machine3
env.agent=machine4

log_everything(env)

env.run()
        




