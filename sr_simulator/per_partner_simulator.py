import pandas as pd
from sr_optimizer.optimizer import optimizer

class per_partner_simulator:
    def __init__(self, partner_id, NPM, seed, how_many_ratio, UCB_beta, click_cost):
        self.partner_id = partner_id
        self.partner_data_df = None
        self.partner_data_df_without_excluded = None
        self.yesterday_excluded = []
        self.next_day_excluded_products = []
        self.first_day_flag = True
        self.optimizer = optimizer(NPM, seed, how_many_ratio, UCB_beta)
        self.click_cost = click_cost
        self.date = None

    def next_day(self, partner_data_df):
        self.partner_data_df = partner_data_df
        self.partner_data_df_without_excluded = partner_data_df
        print("Produktów dziś: ", partner_data_df['product_id'].nunique())
        print("Yesterday: ", self.yesterday_excluded)
        if self.yesterday_excluded != []:
            # TODO credits for Patryk Baryła
            self.partner_data_df_without_excluded = self.partner_data_df_without_excluded[self.partner_data_df_without_excluded['product_id'].apply(lambda x: x not in self.yesterday_excluded)]
            # TODO credits end
        try:
            self.date = self.partner_data_df['click_timestamp'].values[0]
        except:
            self.date = None
        print("Yesterday excluded: ", len(self.yesterday_excluded))
        # get next day excluded
        self.next_day_excluded_products = self.optimizer.next_day(self.partner_data_df_without_excluded)
        # update yesterday excluded list
        self.yesterday_excluded = self.next_day_excluded_products
        return self.calculate_per_day_profit_gain_factors()

    def filter_out_other_partners_data(self):
        None

    def calculate_per_day_profit_gain_factors(self):
        if self.first_day_flag:
            self.first_day_flag = False
            click_savings = 0.0
            sale_losses = 0.0
            profit_losses = 0.0
            profit_gain = 0.0
        else:
            all_products = self.partner_data_df['product_id'].unique()
            click_savings_for_each_product = []
            sale_losses_for_each_product = []
            profit_losses_for_each_product = []
            sales_cost = 0.0
            clicks = 0
            if self.yesterday_excluded != []:
                for product in all_products:
                    mask = self.partner_data_df['product_id'] == product
                    product_df = self.partner_data_df[mask]
                    if product in self.yesterday_excluded:
                        clicks_saved = self.partner_data_df['product_id'].value_counts()[product]
                        click_savings_for_each_product.append(clicks_saved * self.click_cost)
                        sales_lost = 0.0
                        for _, row in product_df.iterrows():
                            if row['Sale'] == 1:
                                sale_price = row['SalesAmountInEuro']
                                sales_lost += sale_price
                                sales_cost += sale_price
                        sale_losses_for_each_product.append(sales_lost)
                        profit_losses_for_each_product.append(sales_lost * 0.1)
                    else:
                        clicks += 1
            click_savings = 0.0
            sale_losses = 0.0
            profit_losses = 0.0
            for c in click_savings_for_each_product:
                click_savings += c
            for s in sale_losses_for_each_product:
                sale_losses += s
            for p in profit_losses_for_each_product:
                profit_losses += p
            profit_gain = (sales_cost * 0.22) - clicks * self.click_cost
        result = {}
        result['click_savings'] = click_savings
        result['sale_losses'] = sale_losses
        result['profit_losses'] = profit_losses
        result['profit_gain'] = profit_gain
        print(self.partner_id, ", ", self.date, ": ", result)
        print("-------------------------------------------------")
        return result