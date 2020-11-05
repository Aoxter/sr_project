import pandas as pd
from partner_data_reader import partner_data_reader

class simulator_core:
    def __init__(self, partners_to_involve_in_simulation, partners_to_not_involve_in_simulation, path_to_data="../data/"):
        # list with all partners_id
        self.partners_to_read_data_from = partners_to_involve_in_simulation + partners_to_not_involve_in_simulation
        # list with all partners df in same order as in partners_id_list
        self.partners_one_day_data_list = []
        self.data_directory = path_to_data
        # list of optimizers for each partner
        self.product_list_optimizer = []
        # TODO call per_partner_simulator init
        self.pdr = partner_data_reader(self.partners_to_read_data_from, self.data_directory)

    def next_day(self):
        self.partners_one_day_data_list = self.pdr.next_day()
        # split_many_partners_data - podzieli self.partners_one_day_data_list
        # split_partner_data - podzieli dane pojedynczych partnerów
        # split_df - podzili df w ramach funkcji wyżej
        # wywołanie next optimizer dla każdego partnera oddzielnie
