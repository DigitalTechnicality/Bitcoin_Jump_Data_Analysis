import pandas as pd

data = pd.read_csv('Coinbase_BTCUSD_ob_10_2019_04_01.csv')
price = data["price"]
only_bids = (data["type"] == "b")
only_bids_value = data[only_bids]
#print(only_bids_value)
#bids_mean = only_bids_value.mean
only_bids_mean = only_bids_value["amount"]
real_mean = only_bids_mean.mean()
print(real_mean)
print(only_bids_mean)
#print(data.head)
#print(only_bids)
#print(only_bids["value"])
