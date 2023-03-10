import json
dict={
    'name':'sabah',
    'age':22,
    'place':'kannur',
    'address':'noormahal'

}
with open('product.json',"w") as fw:
    json.dump(dict,fw)
