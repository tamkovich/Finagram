# from database.models import UserTg, Message
from database import session, UserTg, Message


def test_create_user():
    bob = UserTg.create(user_id='20490124')
    session.commit()


def test_create_message():
    bob = UserTg.where(user_id='20490124').first()
    msg = Message.create(body='Hello World!', usertg=bob)
    session.commit()


def test_migrate():
    # session
    session.commit()


def test_clear_tables():
    """
    use it ONLY for test reason.
    Be carefully! Here is better way to destroy this func, than to use it.
    :return: None
    """
    Message.query.delete()
    UserTg.query.delete()
    session.commit()


if __name__ == '__main__':
    test_clear_tables()
