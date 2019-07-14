from settings.API import API_KEY

import quandl
quandl.ApiConfig.api_key = API_KEY

mydata = quandl.get('XNYS/SG')


if __name__ == "__main__":
    print(API_KEY)
