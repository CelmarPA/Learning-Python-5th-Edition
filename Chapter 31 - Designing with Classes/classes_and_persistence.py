from pizzashop import PizzaShop

shop = PizzaShop()

print(shop.server, shop.chef)

import pickle

pickle.dump(shop, open('shopfile.pkl', 'wb'))

import pickle

obj = pickle.load(open('shopfile.pkl', 'rb'))

print(obj.server, obj.chef)

obj.order('LSP')
