import json

VARS = {
        'Регистрация ИП': "regip",
        'Система налогообложения': "taxsystem",
        'Ликвидация ИП': "licvidation",
        'Налоговая декларация': "dec5",
    }


class Branch:
    FILES_FOLDER = 'data_structures/'
    files = {
        "dec5": f"{FILES_FOLDER}dec5_text.json",
        "licvidation": f"{FILES_FOLDER}licvidation_text.json",
        "regip": f"{FILES_FOLDER}regip_text.json",
        "taxsystem": f"{FILES_FOLDER}tax_systems2.json",
    }

    def __init__(self, branch_name, status):
        self.data = self.load_branch(branch_name)
        self.status = status
        self.step = None

    def load_branch(self, branch_name):
        """
        :param branch_name: <str> name of the branch in bot speech
        :return: dict()-data with content of file for specific branch
        """
        filename = self.files[branch_name]
        with open(filename, 'r') as f:
            data = json.load(f)
        return data

    def update_status(self, answer):
        """
        generate a new status by answer
        have to run after self.gen_step()
        :return: None
        """
        assert self.step, 'You have to generate step firstly. Use Branch.gen_step()'
        key = self.step['buttons'][answer]
        if key == '-':
            self.status = str(int(self.status) + 1)
        elif key == '-1':
            self.status = 0
        elif key == '+':
            self.__init__(self.step['switch'], "0")
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
        assert self.step, 'You have to generate step firstly. Use Branch.gen_step()'
        return self.step['text'], list(self.step['buttons'].keys()), self.step['images'], self.step['files']
