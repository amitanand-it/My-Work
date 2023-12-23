
class Vendor:

    def __init__(self, name):
        self.name = name
        self.bids = {}

    def __str__(self):
        return f"Vendor: {self.name}"

    def place_bid(self, item, amount):
        self.bids[item] = amount

    def get_bid(self, item):
        return self.bids[item]

    def list_bids(self):
        for item, amount in self.bids.items():
            print(f"Vendor {self.name}, {item}, Amount: {amount}")


class Item:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Item: {self.name}"


class Bidding:

    def __init__(self):
        self.vendors = []
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def add_vendor(self, vendor):
        self.vendors.append(vendor)

    def list_vendors(self):
        for index, vendor in enumerate(self.vendors, start=1):
            print(f"{index} - {vendor}")

    def list_items(self):
        for index, item in enumerate(self.items, start=1):
            print(f"{index} - {item}")
    
    def bid_allotment(self):

        winning_bids_list = {} 

        for item in self.items:
            item_bids_list = [] 

            for vendor in self.vendors:
                bid_amount = vendor.get_bid(item)
                item_bids_list.append((vendor.name, bid_amount))

            winning_bid = (min(item_bids_list, key=lambda x: x[1]))

            winning_bids_list[item.name] = winning_bid

        return winning_bids_list
                    



    def bid_comparison(self, item=None):

        if item:
            print(f"Bids for Item: {item}")
            for vendor in self.vendors:
                print(f"{vendor.name}, {vendor.get_bid(item)}")
        else:
            for item in self.items: 
                print(f"Bids for Item: {item.name}")
                for vendor in self.vendors:
                    print(f"{vendor.name}, {vendor.get_bid(item)}")



if __name__ == '__main__':

    vendor1 = Vendor(name="Amit")
    vendor2 = Vendor(name="Jatin")

    item1 = Item(name="Item1")
    item2 = Item(name="Item2")

    bidsystem = Bidding()

    bidsystem.add_vendor(vendor1)
    bidsystem.add_vendor(vendor2)

    print("\n\nVENDORS LIST:-")
    bidsystem.list_vendors()

    bidsystem.add_item(item1)
    bidsystem.add_item(item2)

    print("\n\nITEMS LIST:-")
    bidsystem.list_items()

    vendor1.place_bid(item1, amount=100)
    vendor1.place_bid(item2, amount=500)
    vendor1.list_bids()

    vendor2.place_bid(item1, amount=70)
    vendor2.place_bid(item2, amount=400)
    vendor2.list_bids()

    bidsystem.bid_comparison()
    winning_list = bidsystem.bid_allotment()
    print(winning_list)
    
