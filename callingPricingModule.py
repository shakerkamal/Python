import pricing
# import pricing as sell_price


net_price = pricing.get_net_price(
    price= 100,
    tax_rate= 0.1
)

print(net_price)




# to import all the objects
from pricing import *

net_price = get_net_price(
    price= 100,
    tax_rate= 0.1
)