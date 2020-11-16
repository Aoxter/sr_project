import pandas as pd
from sr_optimizer.optimizer import optimizer

class per_partner_simulator:
    def __init__(self, partner_id, NPM, seed, UCB_beta):
        self.partner_id = partner_id
        self.partner_data_df = None
        self.click_saving = 0.0
        self.sale_losses = 0.0
        self.profil_losses = 0.0
        self.profil_gain = 0.0
        self.yesterday_excluded = []
        self.next_day_excluded = []
        self.first_day_flag = True
        self.optimizer = optimizer(NPM, seed, UCB_beta)

    def next_day(self, partner_data_df):
        self.partner_data_df = partner_data_df
        # update yesterday excluded list
        if self.first_day_flag:
            self.first_day_flag = False
        else:
            self.yesterday_excluded = self.next_day_excluded
        # get next day excluded
        optimized_tuple = self.optimizer.next_day(self.partner_data_df)
        self.next_day_excluded = optimized_tuple[1]
        return self.calculate_per_day_profit_gain_factors()

    def filter_out_other_partners_data(self):
        None

    def calculate_per_day_profit_gain_factors(self):
        None