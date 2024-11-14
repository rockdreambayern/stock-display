import math
from datetime import datetime, timedelta

import akshare as ak
import currencyrate.currency_exchange_rate as currency_exchange_rate


def query_multiple_stock_price(currency_code):
    stock_hk_spot_df = ak.stock_hk_main_board_spot_em()
    target_stocks = stock_hk_spot_df[(stock_hk_spot_df["代码"] == "03690") | (stock_hk_spot_df["代码"] == "00700")]

    current_exchange_rate = currency_exchange_rate.RealTimeCurrencyExchangeRate("HKD", currency_code)

    data_list = []

    for index, target_stock in target_stocks.iterrows():
        latest_price = target_stock["最新价"]
        code = target_stock["代码"]
        name = target_stock["名称"]

        result = math.floor(latest_price * current_exchange_rate * 100) / 100

        data = {
            "name": name,
            "code": code,
            "price": latest_price,
            "price_cny": result
        }

        data_list.append(data)

    return data_list


def query_stock_price(currency_code):
    stock_hk_spot_df = ak.stock_hk_main_board_spot_em()
    target_stock = stock_hk_spot_df[stock_hk_spot_df["代码"] == "03690"]
    latest_price = target_stock["最新价"].values[0]
    code = target_stock["代码"].values[0]
    name = target_stock["名称"].values[0]

    print(target_stock)

    current_exchange_rate = currency_exchange_rate.RealTimeCurrencyExchangeRate("HKD", currency_code)
    result = math.floor(latest_price * current_exchange_rate * 100) / 100

    print(f"实时价格: {latest_price} 港币 {result} 元")

    data = {
        "name": name,
        "code": code,
        "price": latest_price,
        "price_cny": result
    }

    return data


def query_stock_history_prices(code):
    # 获取当前日期
    end_date = datetime.now()

    # 计算30天前的日期
    start_date = end_date - timedelta(days=30)

    # 将日期格式化为 'yyyymmdd'
    end_date_str = end_date.strftime('%Y%m%d')
    start_date_str = start_date.strftime('%Y%m%d')

    stock_hk_spot_em_df = ak.stock_hk_hist(symbol=code, period="daily", start_date=start_date_str,
                                           end_date=end_date_str,
                                           adjust="")

    data_list = []

    # 检查是否找到了匹配的记录
    if stock_hk_spot_em_df.empty:
        return data_list

    for index, stock in stock_hk_spot_em_df.iterrows():
        price = stock["收盘"]
        date = stock['日期'].strftime("%Y-%m-%d")

        data = {
            "name": code,
            "code": code,
            "price": price,
            "date": date
        }

        data_list.append(data)

    return data_list
