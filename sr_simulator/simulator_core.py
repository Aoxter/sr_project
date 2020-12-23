from sr_simulator.partner_data_reader import partner_data_reader
from sr_simulator.per_partner_simulator import per_partner_simulator
from sr_simulator.click_cost_calculator import calculate_click_cost

class simulator_core:
    def __init__(self, partners_to_involve_in_simulation, partners_to_read_data_from, NPM, seed, how_many_ratio, UCB_beta, path_to_data="../data/"):
        self.partners_to_involve_in_simulation = partners_to_involve_in_simulation
        self.partners_to_read_data_from = partners_to_read_data_from
        # list with all partners df in same order as in partners_id_list
        self.partners_one_day_data_list = []
        self.data_directory = path_to_data
        # list of optimizers for each partner
        self.product_list_optimizer = []
        self.all_partners_results_dict = {}
        self.click_costs = calculate_click_cost(partners_to_involve_in_simulation, path_to_data)
        for partner_id in self.partners_to_involve_in_simulation:
            partner_click_cost = 1
            for c in self.click_costs:
                if c[0] == partner_id:
                    partner_click_cost = c[1]
            self.product_list_optimizer.append(per_partner_simulator(partner_id, NPM, seed, how_many_ratio, UCB_beta, partner_click_cost))
            self.all_partners_results_dict[partner_id] = {}
        self.pdr = partner_data_reader(self.partners_to_read_data_from, self.data_directory)



    def next_day(self, log_for_certification):
        self.partners_one_day_data_list = self.pdr.next_day()
        for plo in self.product_list_optimizer:
            single_partner_result_dict = plo.next_day(self.filter_out_other_partners_data(plo.partner_id), log_for_certification)
            self.all_partners_results_dict[plo.partner_id] = (single_partner_result_dict)
        # split_many_partners_data - podzieli self.partners_one_day_data_list
        # split_partner_data - podzieli dane pojedynczych partnerów
        # split_df - podzieli df w ramach funkcji wyżej
        return self.all_partners_results_dict

    def filter_out_other_partners_data(self, partner_id):
        for tuple in self.partners_one_day_data_list:
            if partner_id == tuple[0]:
                return tuple[1]
        # TODO return empty DF?
        return None
