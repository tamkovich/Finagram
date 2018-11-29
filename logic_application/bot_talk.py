import json

from logic_application.database import create_review, create_consultation

VARS = {
    'Регистрация ИП': "regip",
    'Система налогообложения': "taxsystem",
    'Ликвидация ИП': "licvidation",
    'Налоговая декларация': "dec5",
}
HELP_VARS = {
    'Регистрация ИП': "regip",
    'Система налогообложения': "taxsystem",
    'Ликвидация ИП': "licvidation",
    'Налоговая декларация': "dec5",
    'К системе налогооблажения': "taxsystem"
}
COMMENT_VARS = {
    'Отзыв': 'review',
    'Консультация': 'consultation',
}
FILES_FOLDER = 'data_structures/'


class Branch:

    files = {
        "dec5": f"{FILES_FOLDER}dec5_text.json",
        "licvidation": f"{FILES_FOLDER}licvidation_text.json",
        "regip": f"{FILES_FOLDER}regip_text.json",
        "taxsystem": f"{FILES_FOLDER}tax_systems.json",
        "errors": f"{FILES_FOLDER}errors.json"
    }

    def __init__(self, branch_name, status):
        branch_name, status = (branch_name, status) if branch_name else ("errors", "0")
        self.status = status
        self.data = self.load_branch(branch_name)
        self.step = None

    def load_branch(self, branch_name):
        """
        :param branch_name: <str> name of the branch in bot speech
        :return: dict()-data with content of file for specific branch
        """
        filename = self.files.get(branch_name)
        if filename is None:
            filename = self.files['errors']
            self.status = "0"
        with open(filename, 'r') as f:
            data = json.load(f)
        return data

    def update_status(self, answer):
        """
        generate a new status by answer
        have to run after self.gen_step()
        :return: None
        """
        key = self.step['buttons'].get(answer)
        if key == '-':
            self.status = str(int(self.status) + 1)
        elif key == '-1':
            self.status = 0
        elif key == '+':
            self.__init__(self.step['switch'], "0")
        elif key is None:
            self.__init__(None, None)
        else:
            self.status = key

    def gen_step(self):
        """
        generate a current step by your status
        :return: None
        """
        self.step = self.data[self.status]

    def prepare_step(self):
        """
        prepare step to use in telegram api
        :return: <tuple> all data from step
        """
        return self.step['text'], list(self.step['buttons'].keys()), self.step['images'], self.step['files']


class Comment:
    files = {
        "review": f"{FILES_FOLDER}comment.json",
        "consultation": f"{FILES_FOLDER}comment.json",
        "comment": f"{FILES_FOLDER}comment.json",
    }
    _minibranch = {"review": "0", "consultation": "1"}

    def __init__(self, branch_name, status, msg, chat_id):
        self.step, self.status, self.create_func = self.load_step(branch_name, status)
        try:
            self.comment = msg.decode('utf-8')
        except AttributeError:
            self.comment = msg
        self.chat_id = chat_id

    def load_step(self, branch_name, status):
        """
        :param branch_name: <str> name of the branch in bot speech
        :param status: <str> state on the branch
        :return: dict()-data with content of file for specific step of the branch
        """
        filename = self.files["comment"]
        with open(filename, 'r') as f:
            data = json.load(f)
        if status == "2":
            if self._minibranch.get(branch_name) == "0":
                return data["2"], "-1", create_review
            else:
                return data["2"], "-1", create_consultation
        else:
            if self._minibranch.get(branch_name) == "0":
                return data["0"], "2", None
            else:
                return data["1"], "2", None

    def save(self):
        """
        Saved comment to the database with the `create_func`
        :return: None
        """
        if self.create_func:
            self.create_func(
                user_id=str(self.chat_id),
                body=self.comment,
            )

    def prepare_step(self):
        """
        prepare step to use in telegram api
        :return: <tuple> all data from step
        """
        return self.step['text'], list(self.step['buttons'].keys()), self.step['images'], self.step['files']
