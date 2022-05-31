from flask import render_template
from service.request_service import *
from service.deletion_service import prep_user_id

def get_request_page(username):
    return render_template("request.html", username=username)

def get_view_request_page(username):
    user_id = prep_user_id(username)
    reequestinfo = get_view_request(user_id)
    print(reequestinfo)
    return render_template("view_request.html", username=username, info=reequestinfo)

def request_user_input(username,register_input):
    user_id = prep_user_id(username)
    if validate_request_service(register_input):
        request_id = create_request(user_id, register_input)
        if request_id is not None:
            return render_template("account_page.html", username=username)
    else:
        return render_template("failed_request.html")
