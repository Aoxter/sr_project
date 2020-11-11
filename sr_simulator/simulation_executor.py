from simulator_core import simulator_core

def execute_simulation(partners_to_involve_in_simulation, partners_to_not_involve_in_simulation, path_to_data, days):
    # TODO load partners profiles
    sim_core = simulator_core(partners_to_involve_in_simulation, partners_to_not_involve_in_simulation, path_to_data)
    for day in range(1, days):
        results = sim_core.next_day()
        # TODO simulation_results_postproces

def align_config():
    None


if __name__ == "__main__":
    None