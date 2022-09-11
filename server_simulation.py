import random

# Agent class
class ServerAgent(object):
    def __init__(self, small_count=10, medium_count=10, large_count=10):
        self.small_count = small_count
        self.medium_count = medium_count
        self.large_count = large_count
    
    # return a water bottle
    def select_action(self, percept):

        #return a large bottle
        if (percept >= 0 and percept <= 33):
            if self.large_count > 0:
                self.large_count -=1    # decrement large count from storage
                return "large"
            else:
                return None

        # return a medium bottle
        elif (percept >= 34 and percept <=66):
            if self.medium_count > 0:
                self.medium_count -=1   # decrement medium count from storage
                return "medium"
            else:
                return None
        # return a small bottle
        elif (percept >= 67 and percept <= 99):
                if self.small_count > 0:
                    self.small_count -=1 # decrement small count from storage
                    return "small"
                else:
                    return None

        # return nothing
        elif percept >= 100:
            return None

        else:
            return "Invalid input"
    
    # return True if all sizes = 0
    def storage_empty(self):
        if (self.large_count == 0 and self.medium_count == 0 and self.small_count == 0):
            return True
        else:
            return False

# Environment class
class ServerEnvironment(object):
    def __init__(self, server_agent):
        self.server_agent = server_agent
        self.num_agent_actions = 0

    # calls the action with a random input
    def tick(self):
        num = random.randint(a=0, b=130)    # hydration level
        self.server_agent.select_action(num)
        self.num_agent_actions +=1          # increment counter
        
        # display information (comment if testing using test.py)
        print("hydration level:", num)
        print("size:", self.server_agent.select_action(num))
        print("number of actions:",self.num_agent_actions)
        print("Empty yet?", self.server_agent.storage_empty())
        print("\n")
    
    def display_storage(self):
        print("small count:", self.server_agent.small_count, "medium count:", self.server_agent.medium_count, "large count:", self.server_agent.large_count)

    def simulate(self):
        while(self.server_agent.storage_empty() == False):
            self.tick()
            self.display_storage() # (comment this line if testing using test.py)


############################ Test ############################
# comment this section if testing using test.py

server_agent = ServerAgent(small_count=40, medium_count=30, large_count=20)
server_env = ServerEnvironment(server_agent)

server_env.simulate()