import os
import glob
import argparse
import pandas as pd

def calculate_click_cost(partners):
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", default="F:/GitHub/sr_project/data/")
    arg = parser.parse_args()
    folder_path = arg.f
    back_path = os.getcwd()
    os.chdir(folder_path)
    extension = 'csv'
    dtypes = {'Sale': 'int64', 'SalesAmountInEuro': 'float64', 'time_delay_for_conversion': 'int64',
                           'click_timestamp': 'str', 'nb_clicks_1week': 'int64', 'product_price': 'float64',
                           'product_age_group': 'str', 'device_type': 'str', 'audience_id': 'str', 'product_gender': 'str',
                           'product_brand': 'str', 'product_category_1': 'str', 'product_category_2': 'str',
                           'product_category_3': 'str', 'product_category_4': 'str', 'product_category_5': 'str',
                           'product_category_6': 'str', 'product_category_7': 'str', 'product_country': 'str',
                           'product_id': 'str', 'product_title': 'str', 'partner_id': 'str', 'user_id': 'str'}
    all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
    file_counter = 0
    file_counter_end = len(all_filenames)
    click_cost_per_partner = []
    partners_temp = []
    for p in partners:
        partners_temp.append(str(p).lower())
    print("Calculating click costs per partner...")
    for f in all_filenames:
        f_temp = f[5:]
        f_temp = f_temp[:-1]
        f_temp = f_temp[:-1]
        f_temp = f_temp[:-1]
        f_temp = f_temp[:-1]
        print(f, "/", f_temp)
        if f_temp in partners_temp:
            clicks = 0
            sales = 0.0
            file_counter += 1
            print("partner: ", file_counter, "/", file_counter_end)
            df = pd.read_csv(f, sep=",", dtype=dtypes)
            partner_id = df['partner_id'].values[0]
            clicks += df.shape[0]
            for index, row in df.iterrows():
                if row['Sale'] == 1:
                    sales += row['SalesAmountInEuro']
            print("clicks: ", clicks)
            print("sales: ", sales)
            click_cost = (sales * 0.12) / clicks
            print("click cost: ", click_cost)
            click_cost_per_partner.append((partner_id, click_cost))
    os.chdir(back_path)
    return click_cost_per_partner
