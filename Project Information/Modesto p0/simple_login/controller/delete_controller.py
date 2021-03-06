from flask import render_template

from service.deletion_service import validate_deletion, fetch_delete_login, delete_user_information

def get_deletion_page():
    return render_template("deletion.html")

def delete_user(deletion_input):
    user_id = fetch_delete_login(deletion_input)
    delete_user_information(user_id)
    return render_template("thankyou.html")