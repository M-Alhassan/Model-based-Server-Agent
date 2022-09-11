if __name__ == "__main__":
    ############################### test server_simulation
    from server_simulation import *
    import random
    
    random.seed(20220829) # set the seed to be able to reproduce results
    
    server_agent = ServerAgent(small_count=5, medium_count=5, large_count=10)
    server_env = ServerEnvironment(server_agent)
    
    print("Server simulation #1 starting conditions:")
    print("small, medium, large counts: {}, {}, {}".format(server_agent.small_count, server_agent.medium_count, server_agent.large_count))
    print("env num_agent_actions: {}".format(server_env.num_agent_actions))
    
    print("-----simulating until storage is done-----")
    server_env.simulate() 
    print("env num_agent_actions: {}".format(server_env.num_agent_actions))
    print('______________________')
    
    random.seed(20220829) # set the seed to be able to reproduce results
    
    server_agent = ServerAgent(small_count=100, medium_count=50, large_count=50)
    server_env = ServerEnvironment(server_agent)
    
    print("Server simulation #2 starting conditions:")
    print("small, medium, large counts: {}, {}, {}".format(server_agent.small_count, server_agent.medium_count, server_agent.large_count))
    print("env num_agent_actions: {}".format(server_env.num_agent_actions))
    
    print("-----simulating until storage is done-----")
    server_env.simulate() 
    print("env num_agent_actions: {}".format(server_env.num_agent_actions))
    print('______________________')