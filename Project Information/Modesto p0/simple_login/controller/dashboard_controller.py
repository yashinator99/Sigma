from flask import render_template
from database.user_info_dao import deposit_money, withdraw_money, send_money
from database.login_dao import fetch_user, fetch_user_by_username

def get_dashboard():
    return render_template("dashboard.html")

def deposit_action(dashboard_input):
    # user_id = fetch_user(dashboard_input.get("username"))
    user_id = fetch_user(dashboard_input.get("username"), dashboard_input.get("password"))
    deposit_money(user_id, dashboard_input.get("deposit"))
    return render_template("deposited.html")

def withdraw_action(dashboard_input):
    # user_id = fetch_user(dashboard_input.get("username"))
    user_id = fetch_user(dashboard_input.get("username"), dashboard_input.get("password"))
    withdraw_money(user_id, dashboard_input.get("withdraw"))
    return render_template("withdrew.html")

def send_action(dashboard_input):
    # user_id = fetch_user(dashboard_input.get("username"))
    user_id = fetch_user(dashboard_input.get("username"), dashboard_input.get("password"))
    recipient_id = fetch_user_by_username(dashboard_input.get("recipient_username"))
    send_money(user_id, recipient_id, dashboard_input.get("send"))
    return render_template("sent.html")