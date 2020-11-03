import pandas as pd
from datetime import datetime, date, timedelta


class partner_data_reader:
    def __init__(self, partners_id, path_to_data="../data/"):
        # list with all partners_id
        self.partners_id_list = partners_id
        # list with all partners df in same order as in partners_id_list
        self.partners_data_list = []
        self.data_directory = path_to_data
        # first dates for partners
        self.current_date = None
        self.headers = ['Sale', 'SalesAmountInEuro', 'time_delay_for_conversion', 'click_timestamp', 'nb_clicks_1week',
                        'product_price', 'product_age_group', 'device_type', 'audience_id', 'product_gender',
                        'product_brand', 'product_category_1', 'product_category_2', 'product_category_3',
                        'product_category_4', 'product_category_5', 'product_category_6', 'product_category_7',
                        'product_country', 'product_id', 'product_title', 'partner_id', 'user_id']
        self.dtypes = {'Sale': 'int64', 'SalesAmountInEuro': 'float64', 'time_delay_for_conversion': 'int64',
                       'click_timestamp': 'str', 'nb_clicks_1week': 'int64', 'product_price': 'float64',
                       'product_age_group': 'str', 'device_type': 'str', 'audience_id': 'str', 'product_gender': 'str',
                       'product_brand': 'str', 'product_category_1': 'str', 'product_category_2': 'str',
                       'product_category_3': 'str', 'product_category_4': 'str', 'product_category_5': 'str',
                       'product_category_6': 'str', 'product_category_7': 'str', 'product_country': 'str',
                       'product_id': 'str', 'product_title': 'str', 'partner_id': 'str', 'user_id': 'str'}
        self.get_the_earliest_date()

    def get_the_earliest_date(self):
        for partner_id in self.partners_id_list:
            partner_path = self.data_directory + "data_" + partner_id + ".csv"
            partner_df = pd.read_csv(partner_path, sep=",", dtype=self.dtypes)
            partner_df['click_timestamp'] = pd.to_datetime(partner_df['click_timestamp'])
            # convert datetime to date
            partner_df['click_timestamp'] = [datetime.date(x) for x in partner_df['click_timestamp']]
            # first day (csv is sorted)
            first_day = partner_df['click_timestamp'][0]
            if self.current_date is None:
                self.current_date = first_day
            else:
                if self.current_date > first_day:
                    self.current_date = first_day

    def next_day(self):
        # clear previous day data
        self.partners_data_list.clear()
        for partner_id in self.partners_id_list:
            self.partners_data_list.append(self.get_next_day_partner_data(partner_id, self.current_date))
        # date update
        self.current_date += datetime.timedelta(days=1)
        return self.partners_data_list

    def get_next_day_partner_data(self, partner_id, day):
        partner_path = self.data_directory + "data_" + partner_id + ".csv"
        partner_df = pd.read_csv(partner_path, sep=",", dtype=self.dtypes)
        partner_df['click_timestamp'] = pd.to_datetime(partner_df['click_timestamp'])
        partner_df['click_timestamp'] = [datetime.date(x) for x in partner_df['click_timestamp']]
        next_day_df = partner_df[partner_df['click_timestamp'] == str(day)]
        return next_day_df


if __name__ == "__main__":
    pdr = partner_data_reader(partners_id=["0A2CEC84A65760AD90AA751C1C3DD861"])