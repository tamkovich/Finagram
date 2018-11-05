from logic_application.bot_talk import HELP_VARS, Branch
import command_system


def start(_branch_name, _status, msg):
    branch_name = HELP_VARS[msg]
    branch = Branch(branch_name, "0")
    branch.gen_step()
    return branch.prepare_step(), branch_name, branch.status


switch_command = command_system.Command()

switch_command.keys = list(HELP_VARS.keys())
switch_command.description = "Начинаете ветвь"
switch_command.process = start


