from logic_application.bot_talk import VARS, COMMENT_VARS
import command_system


def menu(*args, **kwargs):
    message = '*FinGram* - это Ваш персональный консультат, который обьяснит как открыть, ' \
              'сопровождать и в случае неудачи закрыть ИП. \nРобот поможет Вам определится с ' \
              'выбором системы налогооблажения, подобрать оптимальную форму регистрации и много ' \
              'другое. \n _Сделайте свой выбор!_'
    return (message, list(VARS.keys())+list(COMMENT_VARS.keys()), [], []), None, None


data_command = command_system.Command()

data_command.keys = ["Главное меню", '/start']
data_command.description = "Начальное меню"
data_command.process = menu


