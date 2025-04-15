# program 3 : Find customers who bought a product but never returned.

all_customers = {"John", "Mary", "Steve", "Ana"}
returned_customers = {"Mary", "Ana"}
customer_who_never_retured=all_customers - returned_customers
print("Customers who bought a product but never returned are :",customer_who_never_retured)
