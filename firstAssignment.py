class MiniBank:

    main_userInfo: dict = {}

    def firstOption(self):
        option : int = int(input("Press1 to Login.\nPress2 to register."))
        if option == 1:
            self.login()
        else:
            self.register()

    def returnId(self, transfer_username):
        userInfo_length : int = len(self.main_userInfo)
        for i in range(1, userInfo_length+1):
            if self.main_userInfo[i]["r_username"] == transfer_username:
                return i
        return None

    def menu(self,loginId):
        menu_input = int(input("Press1 to Transfer\nPress2 to Withdraw\nPress3 to update user data:"))
        if menu_input == 1:
            transfer_username : str = input("\nEnter username to transfer: ")
            transfer_id : int = self.returnId(transfer_username)
            if transfer_id == None:
                print("\nThere is no such user.\n")
            else:
                if transfer_id == loginId:
                    print("\nCan't transfer to own account.\n")
                    return
                print("\nTransfer Id: ", transfer_id)
                print("My Id: ", loginId)
                amount :int = int(input("\nEnter amount to transfer {0}:".format(self.main_userInfo[transfer_id]["r_username"])))
                if amount > self.main_userInfo[loginId]["amount"]:
                    print("You don't have enough money!")
                else:
                    self.main_userInfo[loginId]["amount"] -= amount
                    self.main_userInfo[transfer_id]["amount"] += amount
                print("\nYou have transferred a total of ${0} to {1}.\n".format(amount, transfer_username))
                print("Current amount: $", self.main_userInfo[loginId]["amount"])

        elif menu_input == 2:
            wcurrent_amount :int = self.main_userInfo[loginId]["amount"]
            print("\nCurrent amount: $", wcurrent_amount)
            amount: int = int(input("Enter amount to withdraw: "))
            if amount > wcurrent_amount:
                print("\nYou don't have enough money!\n")
            else:
                self.main_userInfo[loginId]["amount"] -= amount
            print("Latest amount: $", self.main_userInfo[loginId]["amount"],"\n")
        elif menu_input == 3:
            user_info = self.main_userInfo[loginId]
            uoption :int = int(input("\nPress1 to change name\nPress2 to change password\nPress3 to change amount:"))
            if uoption == 1:
                new_name :str = input("\nEnter new username: ")
                user_info["r_username"] = new_name
            elif uoption == 2:
                new_password :int = int(input("\nEnter new password: "))
                user_info["r_userpasscode"] = new_password
            elif uoption == 3:
                new_amount :int = int(input("\nEnter new amount: "))
                user_info["amount"] = new_amount
            print("\nNew User Details: ", user_info)

    def login(self):
        print("\n______________This is login______________\n")

        l_username : str = input("Pls enter username to Login: ")
        l_userpasscode : int = int(input("Pls enter passcode to Login: "))

        existUser = self.existUser(l_username, l_userpasscode)
        if(existUser):
            print("\n______________Login Successful______________\n")
            loginId=self.returnId(l_username)
            self.menu(loginId)
        else:
            print("\nU can't Login!\n")

    def existUser(self, l_username, l_userpasscode):
        user_count = len(self.main_userInfo)
        for i in range(1,user_count+1):
            if (self.main_userInfo[i]["r_username"] == l_username and
                self.main_userInfo[i]["r_userpasscode"] == l_userpasscode):
                return True
        return False

    def register(self):
        print("\n______________This is register______________\n")

        r_username : str = input("Pls enter username to Register: ")
        for user_id in range(1,len(self.main_userInfo )+1):
            if r_username == self.main_userInfo[user_id]["r_username"]:
                print("\nUser already exists!\n")
                return
        r_userpasscode1 : int = int(input("Pls enter passcode to Register: "))
        r_userpasscode2 : int = int(input("Pls enter again passcode to com: "))
        r_amonut : int = int(input("Pls enter amount to register: "))

        if r_userpasscode1 == r_userpasscode2:
            id: int = self.checkUserCount()
            userInfoForm: dict = {id:{"r_username":r_username, "r_userpasscode":r_userpasscode1, "amount":r_amonut}}
            self.main_userInfo.update(userInfoForm)
            print("______________Successfully Registered_____________\n\n")
            print(self.main_userInfo)

    def checkUserCount(self):
        count = len(self.main_userInfo)
        return count + 1

if __name__ == '__main__':
    miniBank : MiniBank = MiniBank()
    while True:
        miniBank.firstOption()
        miniBank.main_userInfo