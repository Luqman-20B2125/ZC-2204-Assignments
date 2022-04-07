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
		
		#BAD CODE 1
        if((self.quantity > 50) or ((self.quantity * self.price) > 500)):
            quantityDiscount = .10
        elif((self.quantity > 25) or ((self.quantity * self.price) > 100)):
            quantityDiscount = .07
        elif((self.quantity >= 10) or ((self.quantity * self.price) > 50)):
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
			
			# You can also use an explaining variable for complicated calculations
			# It may however be better to extract this code into a method though
			# to separate it from the method
			
			# final is used to make sure the temp only has 1 value per iteration
			# It is bad practice to assign different values to a temp
			
            numOfProducts = product.getQuantity()
            prodName = product.getName()
            cost = product.getTotalCost()
			
            costWithDiscount = product.getTotalCost() / product.getQuantity()
            costWithoutDiscount = product.getPrice() + product.getShippingCost()
			
			# BAD CODE 2
            print("Total cost for ", product.getQuantity(), " ", product.getName(), "s is $", product.getTotalCost())
            print("Cost per product ", (product.getTotalCost() / product.getQuantity()))
            print("Savings per product ", ((product.getPrice() + product.getShippingCost()) - (product.getTotalCost() / product.getQuantity())))
	
		
cornerStore = Store()
cornerStore.addAProduct(Product("Pizza", 10.00, 1.00, 52))
cornerStore.addAProduct(Product("Pizza", 10.00, 1.00, 26))
cornerStore.addAProduct(Product("Pizza", 10.00, 1.00, 10))
cornerStore.getCostOfProducts()



# BAD CODE 3
# Why Is it Bad to Assign Many Values to a Temp?
"""    
temp = totalCost / numberOfProducts
temp = temp + shipping	
temp = temp - discount       # temp may now be the product price + shipping - discount but will this make sense a year from now?
"""	

# BAD CODE 4
# Don't assign values to parameters either
"""
def getTotPrice(quantity, price, shippingCost, discount) {
	price = price + shippingCost
	price = price * quantity
	return price - discount
"""