import random

class optimizer:
    def __init__(self, NPM, seed, how_many_ratio, UCB_beta):
        self.NPM = NPM
        self.seed = seed
        self.how_many_ratio = how_many_ratio
        self.UCB_beta = UCB_beta
        self.products = []
        self.date = None

    def next_day(self, next_day_data):
        self.products = self.__get_products_seen_today(next_day_data)
        if next_day_data.empty:
            excluded_products = []
        else:
            #print("Next day:", next_day_data['click_timestamp'][0])
            #self.date = next_day_data['click_timestamp'][0]
            excluded_products = self.__get_excluded_products_pseudorandomly()
        return excluded_products

    def __get_excluded_products_pseudorandomly(self):
        dummy_list_of_potentially_excluded_products = self.products
        dummy_list_of_potentially_excluded_products.sort()
        dummy_how_many_products = round(len(dummy_list_of_potentially_excluded_products) / self.how_many_ratio)
        print("Produkty wykluczone na otrzymane: ", dummy_how_many_products, "/", len(dummy_list_of_potentially_excluded_products), ":")
        random.seed(self.seed)
        excluded_products = random.sample(dummy_list_of_potentially_excluded_products, dummy_how_many_products)
        if excluded_products == None:
            excluded_products = []
        #return self.date, excluded_products
        print("Excluded: ", excluded_products)
        return excluded_products

    def __get_products_seen_today(self, data_df):
        if data_df.empty:
            products = []
        else:
            products = data_df['product_id'].unique().tolist()
        return products

