from kunder import Customer

class customerData:
    def __init__(self, name):
        self.name = name
        self.customers = []

    def add_customer(self, name, email, phone):
        for customer in self.customers:
            if customer.email == email:
                raise ValueError ("Mejlet finns redan med i listan!")
            
        new_customer = Customer(name, email, phone)
        self.customers.append(new_customer)
        print(f"{name} har lagts till som en ny kund.")



