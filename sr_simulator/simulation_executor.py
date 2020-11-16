import configparser
from sr_simulator.simulator_core import simulator_core
import sys

def execute_simulation(partners_to_involve_in_simulation, partners_to_read_data_from, days, NPM, seed, UCB_beta, path_to_data):
    # TODO load partners profiles
    sim_core = simulator_core(partners_to_involve_in_simulation, partners_to_read_data_from, NPM, seed, UCB_beta, path_to_data)
    for day in range(1, days):
        results = sim_core.next_day()
        # TODO simulation_results_postproces

def align_config():
    missing_arg_flag = False
    PTIIS = None
    PTRDF = None
    steps = None
    NPM = None
    seed = None
    UCB_beta = None
    path = None
    config = configparser.ConfigParser()
    config.read('config.ini')
    if config.has_option('OPTIONS', 'partners_to_involve_in_simulation'):
        PTIIS = config.get('OPTIONS', 'partners_to_involve_in_simulation')
    else:
        print("ERROR! Missing partners_to_involve_in_simulation value in config.ini")
        missing_arg_flag = True
    if config.has_option('OPTIONS', 'partners_to_read_data_from'):
        PTRDF = config.get('OPTIONS', 'partners_to_read_data_from')
    else:
        print("ERROR! Missing partners_to_read_data_from value in config.ini")
        missing_arg_flag = True
    if config.has_option('OPTIONS', 'number_of_simulation_steps'):
        steps = config.get('OPTIONS', 'number_of_simulation_steps')
    else:
        print("ERROR! Missing number_of_simulation_steps value in config.ini")
        missing_arg_flag = True
    if config.has_option('OPTIONS', 'NPM'):
        NPM = config.get('OPTIONS', 'NPM')
    else:
        print("ERROR! Missing NPM value in config.ini")
        missing_arg_flag = True
    if config.has_option('OPTIONS', 'pseudorandom_seed'):
        seed = config.get('OPTIONS', 'pseudorandom_seed')
    else:
        print("ERROR! Missing pseudorandom_seed value in config.ini")
        missing_arg_flag = True
    if config.has_option('OPTIONS', 'UCB_beta'):
        UCB_beta = config.get('OPTIONS', 'UCB_beta')
    else:
        print("ERROR! Missing UCB_beta value in config.ini")
        missing_arg_flag = True
    if config.has_option('OPTIONS', 'path_to_data'):
        path = config.get('OPTIONS', 'path_to_data')
    else:
        print("ERROR! Missing path_to_data value in config.ini")
        missing_arg_flag = True
    if missing_arg_flag == True:
        input("Press any key to exit")
        sys.exit()
    else:
        execute_simulation(PTIIS, PTRDF, steps, NPM, seed, UCB_beta, path)


if __name__ == "__main__":
    align_config()