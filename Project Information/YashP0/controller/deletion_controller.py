from flask import render_template
from service.deletion_service import prep_user_id, delete_user_from_db

def delete_user_account(registration_input):

    user_id = prep_user_id(registration_input)

    delete_user_from_db(user_id)
    return render_template("deletion.html")
