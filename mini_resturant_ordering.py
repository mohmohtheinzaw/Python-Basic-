class Resturant:
    menus={
        'pizza' : 7000,
        'fried chicken wing': 5000,
        'humburger' : 4000,
        'apple juice' : 2000,
        'cola' : 1500,
        'fried potato':3000
    }

    def __init__(self):
        self.total =0
        self.orders =[]
    
    def addOrders(self,order):
        self.orders.append(order)
        self.total += self.menus[order]

        # self.qty = qty
        # print(self.menus[order])
        # self.subTotal = self.menus[order] * qty

    def printBill(self) :
        for order in self.orders :
            print(f'{order}: {self.menus[order]}')
        print(f'Total is {self.total}')
            


def startOrdering() :
        resturant = Resturant()

        while True : 
            order = input('Order :')
            # qty = input('Qty :')
            resturant.addOrders(order)

            another = input('Order again? y/n :')
            if(another == 'y') :
                continue
            else :
                resturant.printBill()
                break
startOrdering()


