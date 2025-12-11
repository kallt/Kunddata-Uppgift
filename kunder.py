from datetime import datetime

class Customer:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.interactions = []
        self.last_interaction = None

    def add_interaction(self, text):
        self.interactions.append(text)
        self.last_interaction = datetime.now()
    
    def calculate_days_since_last_interaction(self):
        if self.last_interaction == None:
            return "Inga interaktioner"
        
        today = datetime.now()
        day_difference = today - self.last_interaction
        return day_difference.days