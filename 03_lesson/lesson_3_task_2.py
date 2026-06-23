from smartphone import Smartphone

catalog = []


catalog = [
        Smartphone('Xiaomi', '15T 5G', '+79123456789'),
        Smartphone('Sumsung', 'Galaxy A16', '+79456789123'),
        Smartphone('Apple', 'iPhone 15 Pro', '+79987654321'),
        Smartphone('Poco', 'X8 Pro', '+79963258741'),
        Smartphone('Honor', 'X9 D', '+79147852369')
        ]

for phone in catalog:
    print(phone.brand, '-', phone.model, '.', phone.phon_number)
