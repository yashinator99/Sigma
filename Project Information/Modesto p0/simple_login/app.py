# I will run flask here
from database.login_dao import insert_user
def main():
    print(insert_user("test_user_3", "pass_2"))

if __name__ == "__main__":
    main()