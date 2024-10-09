import logging

# Создаем хэндлер
handler = logging.FileHandler("logs.log", mode="w", encoding="utf-8")
formatter = logging.Formatter("%(asctime)s:%(module)s:%(levelname)s:%(name)s:%(message)s")
handler.setFormatter(formatter)

# Настраиваем логирование
logging.basicConfig(level=logging.INFO, handlers=[handler])

logger = logging.getLogger()

def get_mask_card_number(card_number: int) -> str:
    logger.info("Получен номер карты для маскирования: %s", card_number)
    # Преобразуем число в строку и проверяем, состоит ли оно только из цифр
    card_str = str(card_number)

    # Проверяем, что номер карты длиной 16 цифр и не является недопустимым вводом
    if len(card_str) != 16 or not card_str.isdigit() or card_number == 0 or card_number > 9999999999999999:
        logger.error("Недействительный номер карты: %s", card_number)
        raise ValueError("Недействительный номер карты")

    # Маскируем номер карты
    masked_card = f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"
    logger.info("Замаскированный номер карты: %s", masked_card)
    return masked_card


print(get_mask_card_number(7000792289606361))  # Ожидается: "7000 79** **** 6361"


def get_mask_account(account_number: int) -> str:
    logger.info("Получен номер счета для маскирования: %s", account_number)

    """Преобразуем номер счета в строку"""
    account_number_str = str(account_number)

    # Проверяем, состоит ли номер счета только из цифр и имеет ли нужную длину
    if not account_number_str.isdigit() or len(account_number_str) != 20:
        logger.error("Введен некорректный номер счета: %s", account_number)
        raise ValueError("Введен некорректный номер счета")

    # Создаем маску: оставляем первые 4 символа, 2 маскированные и 4 последние
    masked_account_number = f"{account_number_str[:4]} {account_number_str[4:6]}** **** {account_number_str[-4:]}"
    logger.info("Замаскированный номер счета: %s", masked_account_number)
    return masked_account_number


print(get_mask_account(12345678901234567890))  # Ожидается: "1234 56** **** 7890"
