class BankAccount:
	def __init__(self,account_type, amount):
		self.account_type = account_type
		self.amount = amount
		
	def deposit(self,deposit_amount):
		self.amount += deposit_amount
		
	def withdraw(self, withdraw_amount):
		self.amount -= withdraw_amount
		
	def __str__(self):#remain ammount
		return "{}:{}".format(self.account_type, self.amount)
xue = BankAccount("Checkings",100)
print (xue.account_type)
print (xue.amount)

xue.deposit(100)
print (xue.amount)

xue.withdraw(10)
print (xue.amount)

print(xue)