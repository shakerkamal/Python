def get_net_price(price, discount):
    return price * (1-discount)



net_price = get_net_price(discount=0.1, price=100)
net_price = get_net_price(price=100, discount=0.1)

def get_net_price(price, tax=0.07, discount=0.05):
    return price * (1 + tax - discount)

# net_price = get_net_price(100, tax=0.08, 0.06) 
# results in an error  SyntaxError: positional argument follows keyword argument
# Once you use a keyword argument, you need to use keyword arguments for the remaining parameters.


#correct way of calling
net_price = get_net_price(100, tax=0.08, discount=0.06) 