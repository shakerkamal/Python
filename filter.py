# filter(fn, list) ==> returns an iterator

scores = [70, 60, 80, 90, 50]
filtered = filter(lambda score: score >= 60, scores)

print(list(filtered))



countries = [
    ['China', 1394015977],
    ['United States', 329877505],
    ['India', 1326093247],
    ['Indonesia', 267026366],
    ['Bangladesh', 162650853],
    ['Pakistan', 233500636],
    ['Nigeria', 214028302],
    ['Brazil', 21171597],
    ['Russia', 141722205],
    ['Mexico', 128649565]
]

countriesGreaterThan300Millions = filter(lambda country: country[1] > 300000000, countries)

print(list(countriesGreaterThan300Millions))
