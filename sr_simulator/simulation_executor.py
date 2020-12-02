import configparser
from sr_simulator.simulator_core import simulator_core
from sr_simulator.simulation_results_postprocessor import simulation_results_postprocessor
import sys
import matplotlib.pyplot as plt

def execute_simulation(partners_to_involve_in_simulation_str, partners_to_read_data_from_str, days, NPM, seed, how_many_ratio, UCB_beta, path_to_data):
    # TODO load partners profiles?
    partners_to_involve_in_simulation = partners_to_involve_in_simulation_str.split(",")
    partners_to_read_data_from = partners_to_read_data_from_str.split(",")
    sim_core = simulator_core(partners_to_involve_in_simulation, partners_to_read_data_from, NPM, seed, how_many_ratio, UCB_beta, path_to_data)
    all_partners_results_dict = {}
    reoriented_for_each_partner = {}
    for partner_id in partners_to_involve_in_simulation:
        all_partners_results_dict[partner_id] = []
        reoriented_for_each_partner[partner_id] = {}
    for day in range(1, days):
        results_dict = sim_core.next_day()
        for partner in results_dict:
            all_partners_results_dict[partner].append(results_dict[partner])
        # TODO simulation_results_postproces
    postprocessor = simulation_results_postprocessor(all_partners_results_dict)
    final_results = {}
    reoriented_for_each_partner = postprocessor.reorient_results_for_each_partner()
    aggregated_for_each_partner = postprocessor.aggregate_results_for_each_partner(reoriented_for_each_partner)
    aggregated_for_all_partners = postprocessor.aggregate_results_for_all_partners(aggregated_for_each_partner)
    summed_for_all_partners = postprocessor.sum_results_for_all_partners(aggregated_for_all_partners)
    final_results['for_individual_partners'] = all_partners_results_dict
    final_results['reoriented_for_each_partner'] = reoriented_for_each_partner
    final_results['aggregated_for_each_partner'] = aggregated_for_each_partner
    final_results['aggregated_for_all_partners'] = aggregated_for_all_partners
    final_results['summed_for_all_partners'] = summed_for_all_partners
    save_results(final_results)
    # REORIENTED
    # x axis values
    x = []
    for day in range(1, days):
        x.append(day)
    # corresponding y axis values
    y = reoriented_for_each_partner['C0F515F0A2D0A5D9F854008BA76EB537']['profit_gain']
    # plotting the points
    plt.plot(x, y)
    # naming the x axis
    plt.xlabel('Days of simulation')
    # naming the y axis
    plt.ylabel('Reoriented profit gain')
    # giving a title to my graph
    plt.title('Profit gain by days for partner_id C0F515F0A2D0A5D9F854008BA76EB537')

    # function to show the plot
    plt.show()
    # ACCUMULATED
    # corresponding y axis values
    y = []
    acc = 0.0
    for v in reoriented_for_each_partner['C0F515F0A2D0A5D9F854008BA76EB537']['profit_gain']:
        acc += v
        y.append(acc)
    # plotting the points
    plt.plot(x, y)
    # naming the x axis
    plt.xlabel('Days of simulation')
    # naming the y axis
    plt.ylabel('Accumulated profit gain')
    # giving a title to my graph
    plt.title('Profit gain by days for partner_id C0F515F0A2D0A5D9F854008BA76EB537')

    # function to show the plot
    plt.show()


def save_results(result_dict, path = "results.json"):
    import json
    with open(path, 'w') as file:
        json.dump(result_dict, file)

def align_config():
    missing_arg_flag = False
    PTIIS = None
    PTRDF = None
    steps = None
    NPM = None
    seed = None
    how_many_ratio = None
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
    if config.has_option('OPTIONS', 'how_many_ratio'):
        how_many_ratio = config.get('OPTIONS', 'how_many_ratio')
    else:
        print("ERROR! Missing how_many_ratio value in config.ini")
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
        execute_simulation(PTIIS, PTRDF, int(steps), float(NPM), int(seed), float(how_many_ratio), UCB_beta, path)


if __name__ == "__main__":
    align_config()