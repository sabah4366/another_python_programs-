from json import load

with open("products.json", "r") as f:
    data = load(f)
print(data)

# mobile = [item["name"] for item in data if item["category"] == "mobile"]
# print(mobile)

# electronics=[item['name'] for item in data if item['category']=="electronics"]
# print(electronics)

# costly_product=max(data ,key=lambda item:item['price'])
# print(costly_product)

#costly mobile
print("costly mobile")
mobile_details=[i for i in data if i["category"]=='mobile']
print(mobile_details)
costly_mobile=max(mobile_details,key=lambda item:item["price"])
print(costly_mobile)

# #low cost toy
# print("low cost toy")
# toys=[i for i in data if i['category']=='toy']
# print(toys)
# low_cost=min(data,key=lambda item:item["price"])
# print(low_cost)

# #sort products based on qty
# print("sort products based on qty")
# print(sorted(data,key=lambda item:item["qty"]))

# #maxm qty
# print("maxm qty")
# maxm_qty=max(data,key=lambda item:item['qty'])
# print(maxm_qty)

