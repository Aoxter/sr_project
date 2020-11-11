import pandas as pd

class per_partner_simulator:
    def __init__(self, partner_id):
        self.partner_id = partner_id
        self.partner_data_df = None
        # TODO create optimizer instance for partner

    def next_day(self, partner_data_df):
        self.partner_data_df = partner_data_df
        # TODO call optimizer next day and return (excluded, date)
        optimized_tuple = (None, None)
        return self.calculate_per_day_profit_gain_factors(optimized_tuple[0])

    def filter_out_other_partners_data(self):
        None

    def calculate_per_day_profit_gain_factors(self, excluded_products):
        None