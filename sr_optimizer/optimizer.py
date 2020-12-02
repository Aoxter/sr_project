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

    def next_day(self, next_day_data):
        self.products_df, self.products = self.__get_products_seen_today(next_day_data)
        if next_day_data.empty:
            excluded_products = []
        else:
            #print("Next day:", next_day_data['click_timestamp'][0])
            #self.date = next_day_data['click_timestamp'][0]
            excluded_products = self.__get_excluded_products_pseudorandomly()
        for p in excluded_products:
            self.products.remove(p)
        return excluded_products

    def __get_excluded_products_pseudorandomly(self):
        dummy_list_of_potentially_excluded_products = self.products
        dummy_list_of_potentially_excluded_products.sort()
        dummy_how_many_products = round(len(dummy_list_of_potentially_excluded_products) / self.how_many_ratio)
        print("Produkty wykluczone na zapisane w optymizerze: ", dummy_how_many_products, "/", len(dummy_list_of_potentially_excluded_products), ":")
        random.seed(self.seed)
        excluded_products = random.sample(dummy_list_of_potentially_excluded_products, dummy_how_many_products)
        if excluded_products == None:
            excluded_products = []
        #return self.date, excluded_products
        #print("Excluded: ", excluded_products)
        return excluded_products

    def __get_products_seen_today(self, data_df):
        products = self.products
        products_df = self.products_df
        if not data_df.empty:
            print("Produkty przed: ", len(self.products))
            for p in data_df['product_id'].unique().tolist():
                if p not in products:
                    products.append(p)
        products_df.append(data_df, ignore_index=True)
        #products = list(dict.fromkeys(products))
        return products_df, products

