list.sort()
list.sort(reverse=True)

#The sort() method sorts a list in place. In other words, it changes the order of elements in the original list


guests = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer']

guests.sort()
print(guests)

guests.sort(reverse=True)
print(guests)





companies = [('Google', 2019, 134.81),
             ('Apple', 2019, 260.2),
             ('Facebook', 2019, 70.7)]

# sorting based on revenue
def sort_key(company):
    return company[2]

companies.sort(key=sort_key)
print(companies)

# or with lambda expression
companies.sort(key=lambda company:company[2])
print(companies)