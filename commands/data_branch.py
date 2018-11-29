from logic_application.bot_talk import Branch
import command_system


def data(branch_name, status, msg, *args, **kwargs):
    branch = Branch(branch_name, status)
    branch.gen_step()
    branch.update_status(msg)
    branch.gen_step()
    return branch.prepare_step(), branch_name, branch.status


data_command = command_system.Command()

data_command.keys = [
    "Далее",                             # dec5_text
    "По собственной инициативе",         # licvidation_text
    "В связи с бездействием",            # licvidation_text
    "Да", "Нет",                         # licvidation_text
    # "К системе налогооблажения",         # regip_text
    "Разработка ПО",                     # taxsystem
    "Дизайн",                            # taxsystem
    "SEO, продвижение",                  # taxsystem
    "Только разработка сайтов"           # taxsystem
]
data_command.description = "Консультация от Бота"
data_command.process = data
