
welcomeing = """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
"""
print(welcomeing)
our_menu = ['Wings','Cookies','Spring Rolls','Salmon','Steak','Meat Tornado','A Literal Garden','Ice Cream','Cake','Pie','Coffee','Tea','Unicorn Tears']
order=True
counter = 1

while order == True :
    order_input = str(input('> ').title())

    if order_input == 'Quit' :
        print ('Thank you for visiting us ')
        order = False 

    else:
         if order_input in our_menu:
              print(f"** {counter} orders of {order_input} have been added to your meal **")
              counter += 1
         else:
            print(f"** o0opps , we don't have {order_input}  , try another thing  **")

        


