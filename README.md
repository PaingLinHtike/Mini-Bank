🏦 MiniBank — Simple Python Banking System

MiniBank is a lightweight, console-based banking simulator built in Python. It allows users to register, log in, transfer money, withdraw funds, and update account details — all managed through an in-memory dictionary.

⭐ Features

🔐 User Registration
Create a new account with username, passcode, and initial balance.

🚪 User Login
Secure login using username and passcode.

💸 Money Transfer
Transfer funds to another registered user.

🏧 Withdraw Money
Take out money from your account if you have enough balance.

🛠️ Update Account Info
Change username, passcode, or reset your amount.

📒 In-Memory Storage
All data is managed inside a Python dictionary (no database required).

▶️ How to Run

Follow on-screen instructions:

Press 1 to log in

Press 2 to register

🧠 How the Program Works
1. Registration

User enters:

Username

Passcode (twice for confirmation)

Starting amount

System prevents duplicate usernames.

2. Login

Username + passcode must match an existing account.

On success, user is taken to the menu.

3. Menu Options
Option	Action
1	Transfer money to another user
2	Withdraw money
3	Update user information
4 Internal Storage

Users are stored like this:

main_userInfo = {
    1: {"r_username": "john", "r_userpasscode": 1234, "amount": 500},
    2: {"r_username": "alice", "r_userpasscode": 4321, "amount": 900}
}

🛠️ Code Overview

firstOption() – entry menu

register() – create a new user

login() – verify login credentials

menu() – transfer, withdraw, update profile

returnId() – find user ID by username

existUser() – check if user exists

checkUserCount() – auto-assign incremental user IDs
