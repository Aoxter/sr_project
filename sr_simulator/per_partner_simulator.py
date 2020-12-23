import pandas as pd
from sr_optimizer.optimizer import optimizer

class per_partner_simulator:
    def __init__(self, partner_id, NPM, seed, how_many_ratio, UCB_beta, click_cost):
        self.partner_id = partner_id
        self.partner_data_df = None
        self.partner_data_df_without_excluded = None
        self.partner_data_df_only_excluded = None
        self.yesterday_excluded = []
        self.next_day_excluded_products = []
        self.first_day_flag = True
        self.npm = NPM
        self.cost = 22 - NPM
        self.optimizer = optimizer(NPM, seed, how_many_ratio, UCB_beta)
        self.click_cost = click_cost
        self.date = None

    def next_day(self, partner_data_df, log_for_certification):
        self.partner_data_df = partner_data_df
        self.partner_data_df_without_excluded = partner_data_df
        self.partner_data_df_only_excluded = partner_data_df
        print("Prodcuts today: ", partner_data_df['product_id'].nunique())
        print("ProductsToExcluded (", len(self.yesterday_excluded), ")")
        if self.yesterday_excluded != []:
            # TODO credits for Patryk Baryła
            self.partner_data_df_without_excluded = self.partner_data_df_without_excluded[self.partner_data_df_without_excluded['product_id'].apply(lambda x: x not in self.yesterday_excluded)]
            self.partner_data_df_only_excluded = self.partner_data_df_only_excluded[self.partner_data_df_only_excluded['product_id'].apply(lambda x: x in self.yesterday_excluded)]
            # TODO credits end
        else:
            self.partner_data_df_only_excluded = pd.DataFrame(columns = ['Sale', 'SalesAmountInEuro', 'time_delay_for_conversion', 'click_timestamp', 'nb_clicks_1week',
                        'product_price', 'product_age_group', 'device_type', 'audience_id', 'product_gender',
                        'product_brand', 'product_category_1', 'product_category_2', 'product_category_3',
                        'product_category_4', 'product_category_5', 'product_category_6', 'product_category_7',
                        'product_country', 'product_id', 'product_title', 'partner_id', 'user_id'])
        try:
            print("ProductsActuallyExcluded (", len(self.partner_data_df_only_excluded['product_id'].unique().tolist()), ")")
        except:
            print("ProductsActuallyExcluded (0)")
        try:
            self.date = self.partner_data_df['click_timestamp'].values[0]
        except:
            self.date = None
        day_dict = {}
        day_dict['day'] = str(self.date)
        day_dict['productsToExclude'] = self.yesterday_excluded
        try:
            actuallyExcludedlist = self.partner_data_df_only_excluded['product_id'].unique().tolist()
            actuallyExcludedlist.sort()
        except:
            actuallyExcludedlist = []
        day_dict['productsActuallyExcluded'] = actuallyExcludedlist
        log_for_certification['days'].append(day_dict)
        # if there is missing day with no data then optimizer will not be called and self.yesterday_excluded will no be changed
        if not partner_data_df.empty:
            # get next day excluded
            self.next_day_excluded_products = self.optimizer.next_day(self.partner_data_df_without_excluded)
            # update yesterday excluded list
            self.yesterday_excluded = self.next_day_excluded_products
            self.yesterday_excluded.sort()
        return self.calculate_per_day_profit_gain_factors()

    def filter_out_other_partners_data(self):
        None

    def calculate_per_day_profit_gain_factors(self):
        click_savings_for_each_product = []
        sale_losses_for_each_product = []
        profit_losses_for_each_product = []
        #if self.yesterday_excluded != []:
        try:
            all_products = self.partner_data_df_only_excluded['product_id'].unique()
        except:
            all_products = []
        for product in all_products:
            mask = self.partner_data_df['product_id'] == product
            product_df = self.partner_data_df[mask]
            # clicks_saved = self.partner_data_df['product_id'].value_counts()[product]
            clicks_saved = product_df.shape[0]
            click_savings_for_each_product.append(clicks_saved * self.click_cost)
            sales_lost = 0.0
            for _, row in product_df.iterrows():
                if row['Sale'] == 1:
                    sale_price = row['SalesAmountInEuro']
                    sales_lost += sale_price
            sale_losses_for_each_product.append(sales_lost)
            profit_losses_for_each_product.append(sales_lost * 0.1)

        click_savings = 0.0
        sale_losses = 0.0
        profit_losses = 0.0
        for c in click_savings_for_each_product:
            click_savings += c
        for s in sale_losses_for_each_product:
            sale_losses += s
        for p in profit_losses_for_each_product:
            profit_losses += p
        profit_gain = (click_savings) - (sale_losses*(self.npm+self.cost))/100
        result = {}
        result['click_savings'] = click_savings
        result['sale_losses'] = sale_losses
        result['profit_losses'] = profit_losses
        result['profit_gain'] = profit_gain
        print(self.partner_id, ", ", self.date, ": ", result)
        print("-------------------------------------------------")
        return result