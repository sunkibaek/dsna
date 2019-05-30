class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    if user in group.users:
        return True

    for sub_group in group.groups:
        if is_user_in_group(user, sub_group):
            return True

    return False


def test1():
    print("Testing for sub child user")
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    print(is_user_in_group(sub_child_user, parent) == True)
    # True


def test2():
    print("Testing for sub sub child user")
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")
    sub_sub_child = Group("subsubchild")

    sub_sub_child_user = "sub_child_user"
    sub_sub_child.add_user(sub_sub_child_user)

    sub_child.add_group(sub_sub_child)
    child.add_group(sub_child)
    parent.add_group(child)

    print(is_user_in_group(sub_sub_child_user, parent) == True)
    # True


def test3():
    print("Testing for child user")
    parent = Group("parent")
    child = Group("child")

    child_user = "child_user"
    child.add_user(child_user)

    parent.add_group(child)

    print(is_user_in_group(child_user, parent) == True)
    # True


test1()
test2()
test3()
