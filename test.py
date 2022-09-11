from main import ticket_price

assert ticket_price(0) == "Бесплатно", "Ошибка АОлавдфва для 0 лет"
assert ticket_price(7) == "100 рублей" "Ошибка для 7 лет"
assert ticket_price(60) == "Бесплатно", "Ошибка для 60 лет"
assert ticket_price(160) == "Бесплатно", "Ошибка для 160 лет"