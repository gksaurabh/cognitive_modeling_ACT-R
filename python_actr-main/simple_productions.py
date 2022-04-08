from python_actr import *  


class MyEnvironment(Model):
    pass


class MyAgent(ACTR):
    
    focus=Buffer()
    # focus.set('sandwich_step:bread_bottom')

    # def bread_bottom(focus='sandwich_step:bread_bottom'):# if focus buffer has this chunk then....
    #     print("I have a piece of bread")                 # print the action
    #     focus.set('sandwich_step:cheese')                # change chunk in focus buffer

    # def cheese(focus='sandwich_step:cheese'):            # the rest of the productions are the same
    #     print("I have put cheese on the bread")          # but carry out different actions
    #     focus.set('sandwich_step:ham')

    # def ham(focus='sandwich_step:ham'):
    #     print("I have put  ham on the cheese")
    #     focus.set('sandwich_step:bread_top')

    # def bread_top(focus='sandwich_step:bread_top'):
    #     print("I have put bread on the ham")
    #     print("I have made a ham and cheese sandwich")
    #     focus.set('sandwich_step:stop')   

    focus.set('travel_step:wake_up')

    def wake_up(focus='travel_step:wake_up'):
        print("I have just woken up")
        focus.set('travel_step:brush_teeth')
    
    def brush_teeth(focus='travel_step:brush_teeth'):
        print("I brushed my teet")
        focus.set('travel_step:poop')
        
    def poop(focus='travel_step:poop'):
        print("I finished pooping")
        focus.set('travel_step:shower')
    
    def shower(focus='travel_step:shower'):
        print("I finished showering")
        focus.set('travel_step:get_dressed')
    
    def get_dressed(focus='travel_step:get_dressed'):
        print("I am wearing my best outfit")
        focus.set('travel_step:walk_to_car')
    
    def walk_to_car(focus='travel_step:walk_to_car'):
        print("I walked to my car")
        focus.set('travel_step:get_in_car')
    
    def get_in_car(focus='travel_step:get_in_car'):
        print("I just got in my car")
        focus.set('travel_step:wear_seatbelt')

    def wear_seatbelt(focus='travel_step:wear_seatbelt'):
        print("Safety first, I wear my seatbelt")
        focus.set('travel_step:drive')

    def drive(focus='travel_step:drive'):
        print("I drive to the airport")
        focus.set('travel_step:check_in_baggage')

    def check_in_baggage(focus='travel_step:check_in_baggage'):
        print("I checkin my baggage")
        focus.set('travel_step:security_check')

    def security_check(focus='travel_step:security_check'):
        print("I have completed security check.")
        focus.set('travel_step:board_flight')

    def board_flight(focus='travel_step:board_flight'):
        print("I just boarded my flight! Excited to travel!")
        focus.set('travel_step:fly_to_narnia')
        
    def fly_to_narnia(focus='travel_step:fly_to_narnia'):
        print("I flew to Narnia!")
        focus.set('travel_step:go_to_sleep')

    def go_to_sleep(focus='travel_step:go_to_sleep'):
        print("I am tired. I am going to sleep.")
        focus.set('travel_step:dream')
    
    def dream(focus='travel_step:dream'):
        print("It was all a dream. I just woke up!")
        focus.set('travel_step:stop')

    x

bob=MyAgent()                              # name the agent
travel=MyEnvironment()                     # name the environment
travel.agent=bob                           # put the agent in the environment
travel.run()                               # run the environment
