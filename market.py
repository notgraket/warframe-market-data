# notgraket
# Wrapper for Warframe Market API
# Created: 3-8-2022
# Last Edit: 3-11-22

import requests
from dataclasses import dataclass
from exceptions import ConnectionError

@dataclass
class User:
    def __repr__(self):
        return f"""<class 'User("{self.ingame_name}")'>"""
    ingame_name: str
    id: str
    status: str
    

@dataclass
class Order:
    def __repr__(self):
        return f"""<class 'Order("{self.item_name}")'>"""
    item_name : str
    id: str
    platinum: int
    quantity: int
    order_type: str
    platform: str
    region: str
    visible: str
    user: User


class Market:
    def __init__(self):
        self.listings = {}
    
    def clear(self, item_name : str):
        if item_name in self.listings:
            self.listings[item_name] = []


    def get_orders(self, item_name : str):
        """Requests order information from warframe market api"""
        Request = requests.get(f"https://api.warframe.market/v1/items/{item_name}/orders")

        if Request.status_code != 200:
            raise ConnectionError("No internet connection")

        else:
            order_list = Request.json()["payload"]["orders"]
            for order in order_list:
                self.save(
                    item_name, 
                    Order(
                        item_name = item_name,
                        id = order['id'],
                        platinum = order['platinum'],
                        quantity = order['quantity'],
                        order_type = order['order_type'],
                        platform = order['platform'],
                        region = order['region'],
                        visible = order['visible'],
                        user = User(
                            ingame_name = order['user']['ingame_name'],
                            id = order['user']['id'],
                            status = order['user']['status']
                        ) # end User
                    ) # end Order
                ) # end save
                
        







