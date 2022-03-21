veg_price = {'cabbage':2.9,'carrot':1.8,'spinach':3.6,'asparagus':2.94,'artichoke':3.20,'lettuce':2.49}
order = {'cabbage':2,'artichoke':5}

total = 0
for veggie,guantity in order.items():
	total += veg_price[veggie] * quantity
print(total)