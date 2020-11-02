import pandas as pd
from datetime import datetime, date
import os


def split_df(path):
    df_raw = pd.read_csv(path, sep="\t", header=0,
                         names=['Sale', 'SalesAmountInEuro', 'time_delay_for_conversion', 'click_timestamp',
                                'nb_clicks_1week', 'product_price', 'product_age_group', 'device_type', 'audience_id',
                                'product_gender', 'product_brand', 'product_category_1', 'product_category_2',
                                'product_category_3', 'product_category_4', 'product_category_5', 'product_category_6',
                                'product_category_7', 'product_country', 'product_id', 'product_title', 'partner_id', 'user_id'])
    df_raw['click_timestamp'] = [datetime.fromtimestamp(x).date() for x in df_raw['click_timestamp']]
    print(df_raw.dtypes)
    df_raw.sort_values(['click_timestamp'], ascending=True, inplace=True)
    for i, x in df_raw.groupby('partner_id'):
        p = os.path.join(os.getcwd(), "data_{}.csv".format(i.lower()))
        x.to_csv(p, index=False)


if __name__ == "__main__":
    path = "CriteoSearchData"
    print("start")
    split_df(path)