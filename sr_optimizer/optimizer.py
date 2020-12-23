import random

class optimizer:
    def __init__(self, NPM, seed, how_many_ratio, UCB_beta):
        self.NPM = NPM
        self.seed = seed
        self.how_many_ratio = how_many_ratio
        self.UCB_beta = UCB_beta
        self.products = []
        self.products_df = None
        self.date = None
        self.firstDayFlag = True

    def next_day(self, next_day_data):
        if self.products_df is None:
            self.products_df = next_day_data
        else:
            self.products_df = self.products_df.append(next_day_data, ignore_index=True)
        self.products = self.__get_products_seen_today()
        if next_day_data.empty:
            excluded_products = []
        else:
            excluded_products = self.__get_excluded_products_pseudorandomly()
            # print("Next day:", next_day_data['click_timestamp'][0])
            # self.date = next_day_data['click_timestamp'][0]
        for p in excluded_products:
            self.products.remove(p)
        return excluded_products

    def __get_excluded_products_pseudorandomly(self):
        dummy_list_of_potentially_excluded_products = self.products
        dummy_list_of_potentially_excluded_products.sort()
        dummy_how_many_products = round(len(dummy_list_of_potentially_excluded_products) / self.how_many_ratio)
        random.seed(self.seed)
        excluded_products = random.sample(dummy_list_of_potentially_excluded_products, dummy_how_many_products)
        if excluded_products == None:
            excluded_products = []
        #return self.date, excluded_products
        #print("Excluded: ", excluded_products)
        return excluded_products

    def __get_products_seen_today(self):
        products = self.products_df['product_id'].unique().tolist()
        return products
        # if not data_df.empty:
        #     print("Produkty przed: ", len(self.products))
        #     for p in data_df['product_id'].unique().tolist():
        #         if p not in products:
        #             products.append(p)
        # if self.firstDayFlag:
        #     products_df = data_df
        #     self.firstDayFlag = False
        # else:
        #     products_df.append(data_df, ignore_index=True)
        #products = list(dict.fromkeys(products))
        #products.sort()


