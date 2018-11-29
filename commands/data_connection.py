from logic_application.bot_talk import COMMENT_VARS, Comment
import command_system


def data(_branch_name, status, msg, chat_id, *args, **kwargs):
    branch_name = COMMENT_VARS.get(msg)
    if branch_name is None:
        branch_name = _branch_name
    else:
        status = "-1"
    branch = Comment(branch_name, status, msg, chat_id)
    branch.save()
    return branch.prepare_step(), branch_name, branch.status


data_command = command_system.Command()

data_command.keys = list(COMMENT_VARS.keys()) + ['/save_comment']
data_command.description = "Отсавить свое сообщение"
data_command.process = data
