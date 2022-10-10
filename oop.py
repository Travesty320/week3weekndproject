# four square method
# duplex-200,000
# rent for 1000 each side, 2000 total
#  BOX 1 income-rental income(2000),laundry income, storage shed,misc 
#  BOX 2 expenses- tax,:150
#       insurance,:100
#       utilities(electric, water, sewer, gas):0
#       hoa fees,:0
#       lawn/snow care,:0
#       vacancy,100
#       repairs,:100
#       capex:100
#       property management:200
#       mortgage:860
#       total-1610
# BOX 3:
#       cash flow- income 2000 -- expenses 1610
# BOX 4: cash on cash return on investment:
#       down payment: 40000
#       closing costs: 3000
#       rehab money: 7000
#       misc other: 0
#       total investment: 50000
#       annual cashflow: 4680
#       annual cash flow // total investment 9.36%
#       cash on cash roi= 9.68%
# input orders:
# ask what downpayment was made for the house add to total investment:
# ask what closing cost, rehab money and misc was spent and add it total investment:
# then ask for rental income, set that aside - times by 12 months and print yearly and monthly income
# ask for tax, insurance, vacancy, repairs, capex, property management, mortage: all seprately and total up.
# times total spending by 12 months. when you print total spending, print yearly spending and monthly
# subract total spending(12m) from total income(12m) to obtain yearly cashflow:
# yearly cashflow divided by total investment = yearly return on investment. print yearly return on investment

class ROI:
    def __init__(self):
        self.income = []
        self.expenses = []
        self.cashflow = None
        self.invested = []
        self.roi = None


    def Invested(self):
        run_invested = input("What is your total amount for property investment? ")
        if run_invested == int:
            self.invested.append()
        else:
            print("That is an invalid input.")
    
    def Total_Expenses(self):
        while True:
            run_expenses = input("Which monthly expense would you like to add? mortgage,closingcost,tax,insurance,misc")           
            if run_expenses.lower == "mortgage":
                self.expenses == input("How much?")
                self.expenses.append()
            elif run_expenses.lower == "closingcost":
                self.expenses == input("How much?")
                self.expenses.append()
            elif run_expenses.lower == "tax":
                self.expenses == input("How much?")
                self.expenses.append()
            elif run_expenses.lower == "insurance":
                self.expenses == input("How much?")
                self.expenses.append()
            elif run_expenses.lower == "misc":
                self.expenses == input("How much?")
                self.expenses.append()
            else:
                print("That is not a valid option.")
                     
    def Total_Income(self):
        
        run_income = input("What is your total monthly income of the property?")
        
        if type(run_income) == int:
            self.income.append()
        else:
            print("That is an invalid input.")
    
    def Annual_Cashflow(self):
        cashflow = []
        cashflow == (sum[expenses] - sum[income])
        print("Your monthly cashflow is" + cashflow +".")
    
    def Annual_ReturnOI(self):
        roi = sum(cashflow)*12 // sum(invested) 
        print("Your total return on investment is" + roi + "%." ) 

     

def r_o_i():
    while True:
        run = input("What would you like to add to? invested, expenses, income, showcashflow, roi, or quit ")
        if run.lower() == "income":
            make_your_future.Total_Income()
        elif run.lower() == "expenses":
            make_your_future.Total_Expenses()
        elif run.lower() == "showcashflow":
            make_your_future.Annual_Cashflow()
        elif run.lower() == "invested":
            make_your_future.Invested()
        elif run.lower() == "roi":
            make_your_future.Annual_ReturnOI()
        elif run.lower() == "quit":
            break
        else:
            print("That is not a valid option.")
    

