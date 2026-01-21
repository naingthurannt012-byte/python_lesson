class Account():
    def __init__(self,id,name,nrc,amount):
        self.id = id
        self.name = name
        self.nrc = nrc
        self.amount= amount

    def set_id(self,id):
        self.id = id
    def get_id(self):
        return self.id

    def set_name(self,name):
        self.name = name
    def get_name(self):
        return self.name  
      
    def set_nrc(self,nrc):
        self.nrc = nrc
    def get_nrc(self):
        return self.nrc
    
    def set_amount(self,amount):
        self.amount = amount    
    def get_amount(self):
        return self.amount
    
    def display(self):
        print("-------------")
        print("id=",self.id)
        print("name=",self.name)    
        print("nrc=",self.nrc)
        print("amount=",self.amount)    
        print("-------------")

accounts = []   


def get_withdraw_amt():
       return int(input('Enter withdraw amount: '))
def get_deposit():
       return int(input('Enter deposit amount: '))
def close_account():
        print('Close Account..')
        
        found = 0
        found_index= -1
        i+=0
        deposit_id = Account.get_id()  
        for account in accounts:     
          if deposit_id == account[0]:
            found =1
            found_index=i
            break
            i += 1  
        if found == 1:
            del accounts[found_index]
            print('Account closed successfully.')
        else:
           print("Sorry, account not found.try again")

def withdraw_fund():
   print('withdraw Fund.. ')
   found = 0
   found_index = -1
   i = 0

   deposit_id = get_id()
   for account in accounts:
        if deposit_id == account[0]:
            found =1
            found_index = i
            break
        i += 1

        if found == 1:
          print('Account found.')

# since the object is tuple we cannot change the value
#that is why we need to convrt it into list as the following
        curr_account =list(accounts[found_index])
        print('Current Amount is = ',curr_account[3])
        curr_amount=curr_account[3]
        withdraw_amt = get_withdraw_amt()
        if withdraw_amt> curr_amount:
            print('Sorry..Insufficient fund...try again..')
            print("Your current amount is ony..",curr_amount)
        else:
            update_amount = curr_amount - deposit_amt
        update_amount=(curr_amount[0],curr_amount[1],curr_amount[2],update_amount)
        del account[found_index]
        accounts,insert(found_index,update_account)
        print('Deposit Success..')
    #   else:
    #      print('Sorry..Account id not found..try again..')
    
def deposit():
    print('Deposit Fund..')

    found=0
    found_index=-1
    i = 0

    deposit_id = get_id()
    for account in accounts:
        if deposit_id == account[0]:
            found = 1
            found_index = i
            break
            i += 1

        if found ==1:
            print('Account Found...')
            #since the object found is tuple we cannot change the value
            #that is why we need to convert it into list as the following
            curr_account=list(accounts[found_index])
            curr_amount = curr_account[3]
            deposit_amt=get_deposit()
            update_amount=curr_amount + deposit_amt
            update_account=(curr_account[0],curr_account[1],curr_account[2],update_amount)
            del accounts[found_index]
            accounts.insert(found_index,update_account)

            print('Deposit Success')
        else:
          print('Sorry..Account Id not found..try agian')

def display(acc):
   print('-----------')
   print('Account ID =',acc[0])
   print('Account Name =',acc[1])
   print('NRC =',acc[2])
   print('Amount =',acc[3])
   print('-----------')

def exit_program():
     print('Exit Program Now ..Bye Bye..')
def view_accounts():
    for account in accounts:
        display(account)
def get_id():
    return input('Enter ID:')
def get_name():
    return input('Enter Name:')
def get_nrc():
    return input('Enter NRC :')
def  get_amount():
    return input('Enter Amount :')
def create_account():
    id = get_id()
    name = get_name()
    nrc = get_nrc()
    amount=get_amount()

    account=(id,name,nrc,amount)
    accounts.append(account)
    print('Saving Success..')

def get_choice():
    return int(input('Enter Choice:'))
    
def main_menu():
    print(' Yoma Bank ')
    print('----------')
    print('  MENU ')
    print('---------')
    print('[1] Create Account ')
    print('[2] View Accounts')
    print('[3] Deposit Fund')
    print('[4] Withdraw Fund')
    print('[5] Close Account')
    print('---------')
    print('[6] Exit Program')
    print('----------')

def main():
    loop=1
    while loop:
        main_menu()
        choice = get_choice()
        if choice==1:
           create_account()
        elif choice==2:
           view_accounts()
        elif choice ==3:
            deposit()
        elif choice==4:
            withdraw_fund()
        elif choice==5:
            close_account()
        elif choice==6:
           exit_program()
        else:
           print('invlid choice..')

if __name__ == "__main__":
    main()

        

              

