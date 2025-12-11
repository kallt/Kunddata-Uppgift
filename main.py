from kunder import Customer

kund1 = Customer("Bilal", "bilal@live.se","0745810394")


kund1.add_interaction("Ringde och fråga om")

print(kund1.name)
print(kund1.email)
print(kund1.phone)
print(len(kund1.interactions))
print(kund1.interactions)
print(kund1.last_interaction)
print(kund1.calculate_days_since_last_interaction())