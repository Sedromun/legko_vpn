import datetime

from config import CONNECT_INSTR_URL, MIN_ADD_AMOUNT
from database.controllers.user import get_user, register_user
from utils.common import datetime_format
from utils.country import COUNTRIES
from utils.payment import get_order_perm_key


def get_greeting_text():
    return (
        "👋 Добро пожаловать в бота <b>Легко VPN</b>!\n\n"
        "⚡️ В нашем сервисе вы можете получить ключ доступа к серверу любой страны и "
        "пользоваться интернет-ресурсами без ограничений!\n\n"
        "🏆 <b>Наши преимущества</b>:\n"
        "• <i>Легкий доступ к сайтам и приложениям</i>\n"
        "• <i>Простая смена стран</i>\n"
        "• <i>Надежность, приватность и анонимность</i>\n"
        "• <i></i>\n"
    )


def get_incorrect_command():
    return "Такой команды нет"


def get_information_text():
    return "Здесь вы можете найти доступные для подключения страны, наш канал и отзывы пользователей"


def get_profile_text(id: int):
    user = get_user(id)
    if user is None:
        register_user(id)
    return f"🏦Ваш баланс: {str(user.balance)} ₽\n\n" f"🙋🏻‍♂️ID: {str(id)}\n"


def get_buy_vpn_text():
    return "🛡️<b>Выберите тариф</b>:"


def get_payment_option_text(amount: int, balance: int):
    return f"💸К оплате {amount}₽\n\n🏦На балансе {balance}₽\n\n<b>Выберите тип оплаты:</b>"


def get_success_created_key_text(key: str):
    return (
        f"🎉 <b>Благодарим за покупку!</b>\n\n<a href='{CONNECT_INSTR_URL}'>⚙️ Инструкция по "
        f"подключению</a>\n\n"
    )


def get_payment_choose_country_text():
    return "Выберите страну для <b>VPN</b>\n<i>(Её можно будет изменить)</i>"


def get_not_enough_money_text(add: int):
    return (
            "На балансе недостаточно средств\n<i>Не достаточно: " + str(add)
            + "₽</i>\n\n<b>Выберите сумму для пополнения</b>"
            + ("\nминимальная сумма пополнения 90₽" if add < MIN_ADD_AMOUNT else "")
    )


def get_pay_text():
    return "Для оплаты нажмите на кнопку"


def get_key_data(order):
    return (
        f"Страна: {order.country} {COUNTRIES[order.country]}\n\n"
        f"Дата истечения: {
            (order.expiration_date.astimezone(datetime.timezone.utc) + datetime.timedelta(hours=3))
            .strftime(datetime_format)
        }\n"
        f"(осталось {get_left_time(order.expiration_date.astimezone(datetime.timezone.utc))})\n\n"
        f"Ключ:\n<code>{get_order_perm_key(order.id)}</code>"
    )


def get_left_time(expiration_date: datetime.datetime):
    current = datetime.datetime.now(datetime.timezone.utc)
    if (expiration_date - current).days > 0:
        return str((expiration_date - current).days) + " дней"
    elif (expiration_date - current).seconds // 3600 > 0:
        return str((expiration_date - current).seconds // 3600) + " часов"
    else:
        return str((expiration_date - current).seconds // 60) + " минут"

def get_referral_bought(amount: int):
    return (f"🎉 Поздравляем, по вашей реферальной ссылке была совершена покупка - вам начислена награда: {amount}₽"
            f" - уже зачислены на ваш баланс")


def order_expired_text(order_id: int):
    return (f"Время действия вашего VPN ключа {order_id} истекло.\n\nСпасибо что выбрали нас!\n\n"
            f"Не забудьте оформить новый ключ!")


def order_going_to_expired_text(order_id: int, time: str):
    return (f"Время действия вашего VPN ключа {order_id} истекает через {time}.\n\nНе забудьте продлить время его"
            f" действия")
