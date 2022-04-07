class Product:
    def __init__(self, name, price, shippingCost, quantity):
        self.name = name
        self.price = price
        self.shippingCost = shippingCost
        self.quantity = quantity
    
    def getName(self):
        return self.name
    def getPrice(self):
        return self.price
    def getShippingCost(self):
        return self.shippingCost
    def getQuantity(self):
        return self.quantity
        
    def getTotalCost(self):
        quantityDiscount = 0.0
		
		# If your expressions become complicated it may make more sense to save
		# them in temporary variables (Explaining Variables)
		
        over50Products = (self.quantity > 50) or ((self.quantity * self.price) > 500)
        over25Products = (self.quantity > 25) or ((self.quantity * self.price) > 100)
        over10Products = (self.quantity >= 10) or ((self.quantity * self.price) > 50)
		
        # GOOD CODE 1
        # Refactored the code by using explaining variables to make it easier to read code

        if(over50Products):
            quantityDiscount = .10
        elif(over25Products):
            quantityDiscount = .07
        elif(over10Products):
            quantityDiscount = .05
		
        discount = ((self.quantity - 1) * quantityDiscount) * self.price
		
        return (self.quantity * self.price) + (self.quantity * self.shippingCost) - discount

class Store:
    def __init__(self):
        self.theProducts = []
	
    def addAProduct(self, newProduct):
        self.theProducts.append(newProduct)
	
    def getCostOfProducts(self):
        for product in self.theProducts:
			
            # GOOD CODE 2
            # Refactored code by using explaining variables to make the print statements much shorter and cleaner to read

            numOfProducts = product.getQuantity()
            prodName = product.getName()
            cost = product.getTotalCost()
			
            costWithDiscount = product.getTotalCost() / product.getQuantity()
            costWithoutDiscount = product.getPrice() + product.getShippingCost()
			
            print("Total cost for {0} {1}s is ${2}".format(numOfProducts, prodName, cost))
            print("Cost per product:", costWithDiscount)
            print("Savings per product:", (costWithoutDiscount - costWithDiscount))
            print()
			
	
		
cornerStore = Store()
cornerStore.addAProduct(Product("Pizza", 10.00, 1.00, 52))
cornerStore.addAProduct(Product("Pizza", 10.00, 1.00, 26))
cornerStore.addAProduct(Product("Pizza", 10.00, 1.00, 10))
cornerStore.getCostOfProducts()

# GOOD CODE 3
# Use meaningful names for variables instead so we understand what's going on when we revisit in the future
"""    
indivProductCost = totalCost / numberOfProducts
prodCostAndShipping = indivProductCost + shipping	
discountedProdCost = prodCostAndShipping - discount  
"""	

# GOOD CODE 4
# Use temporary variables within the function instead
"""
def getTotPrice(quantity, price, shippingCost, discount) {
	indivProdPriceAndShipping = price + shippingCost
	totalProdPriceAndShipping = price * quantity
    discountedTotalPrice = price - discount
	return discountedTotalPrice
"""