from logic_application.bot_talk import Branch


def test_load_branch():
    branch_name = "dec5"
    branch = Branch(branch_name, "0")
    print(branch.data)


def test_gen_step():
    branch_name = "licvidation"
    branch = Branch(branch_name, "0")
    branch.gen_step()
    print(branch.step)


def test_update_status():
    branch_name = "regip"
    branch = Branch(branch_name, "5")
    branch.gen_step()
    branch.update_status('К системе налогооблажения')
    branch.gen_step()
    print(branch.data)


def test_something_goes_wrong():
    branch_name = None
    branch = Branch(branch_name, "0")
    branch.gen_step()
    branch.update_status('К системе налогооблажения')
    branch.gen_step()
    print(branch.prepare_step())


if __name__ == '__main__':
    test_something_goes_wrong()
