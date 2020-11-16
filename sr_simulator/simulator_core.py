from sr_simulator.partner_data_reader import partner_data_reader
from sr_simulator.per_partner_simulator import per_partner_simulator

class simulator_core:
    def __init__(self, partners_to_involve_in_simulation, partners_to_read_data_from, NPM, seed, UCB_beta, path_to_data="../data/"):
        self.partners_to_involve_in_simulation = partners_to_involve_in_simulation
        self.partners_to_read_data_from = partners_to_read_data_from
        # list with all partners df in same order as in partners_id_list
        self.partners_one_day_data_list = []
        self.data_directory = path_to_data
        # list of optimizers for each partner
        self.product_list_optimizer = []
        for partner_id in self.partners_to_involve_in_simulation:
            self.product_list_optimizer.append(per_partner_simulator(partner_id, NPM, seed, UCB_beta))
        self.pdr = partner_data_reader(self.partners_to_read_data_from, self.data_directory)

    def next_day(self):
        self.partners_one_day_data_list = self.pdr.next_day()
        for plo in self.product_list_optimizer:
            plo.next_day(self.filter_out_other_partners_data(plo.partner_id))
        # split_many_partners_data - podzieli self.partners_one_day_data_list
        # split_partner_data - podzieli dane pojedynczych partnerów
        # split_df - podzili df w ramach funkcji wyżej
        # TODO return gain

    def filter_out_other_partners_data(self, partner_id):
        for tuple in self.partners_one_day_data_list:
            if partner_id == tuple[0]:
                return tuple[1]
        # TODO return empty DF?
        return None
