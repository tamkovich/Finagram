from logic_application.bot_talk import VARS, Branch
import command_system


def start(branch_name, status, msg):
    branch_name = VARS[msg]
    branch = Branch(branch_name, "0")
    branch.gen_step()
    return branch.prepare_step(), branch_name, branch.status


switch_command = command_system.Command()

switch_command.keys = list(VARS.keys())
switch_command.description = "Начинаете ветвь"
switch_command.process = start


