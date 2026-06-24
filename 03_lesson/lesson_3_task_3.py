from address import Address
from mailing import Mailing

to_address = Address('123456', 'Moscow', 'Lenina', 10, 5)
from_address = Address('789456', 'Adler', 'Kirova',  104,  1)
mail1 = Mailing(from_address, to_address, 50, '123x')


print(f'{mail1.track} из {mail1.from_address.postal_code}, '
      f'{mail1.from_address.city}, {mail1.from_address.street} '
      f'{mail1.from_address.house} - {mail1.from_address.apartment} в '
      f'{mail1.to_address.postal_code}, {mail1.to_address.city},'
      f'{mail1.to_address.street}, {mail1.to_address.house}'
      f'- {mail1.to_address.apartment}. Стоимость {mail1.cost} рублей.')
