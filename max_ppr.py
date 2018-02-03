# Maximize Price-Performance Ratio

price = 10
performance = 150
add_item_price = 3
add_item_performance = [30, 70, 15, 40, 65]
max_ppr = 0

for i in range(len(add_item_performance)):
    ppr = (performance + add_item_performance[i]) / (price + add_item_price)
    if ppr > max_ppr:
        max_ppr, ppr = ppr, max_ppr

print(max_ppr)