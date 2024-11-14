import os
import requests
from functools import lru_cache


@lru_cache(maxsize=128)
# Function to get real time currency exchange
def RealTimeCurrencyExchangeRate(from_code, to_code):
    # main_url variable store complete url
    app_key = os.getenv("current_rate_app_key")
    main_url = 'https://v6.exchangerate-api.com/v6/' + app_key + "/pair/" + from_code + "/" + to_code

    # get method of requests module

    # return response object
    req_ob = requests.get(main_url)

    # json method return json format
    # data into python dictionary data type.

    # result contains list of nested dictionaries
    result = req_ob.json()

    return result["conversion_rate"]


# Driver code
if __name__ == "__main__":
    # currency code
    from_currency = "HKD"
    to_currency = "CNY"

    # enter your api key here
    api_key = "YOUR API KEY"

    # function calling
    RealTimeCurrencyExchangeRate(from_currency, to_currency, api_key)
