class shopping:
    def __init__(self):
        self.items={'ProductA':20 , 'ProductB':40 , 'ProductC':50}
        # Product details with price
        self.quantity_20=20
    def product(self):
        print('Welcome plz select the product')
        x=[]
        y=[]
        print('Select from these categories :  ProductA , ProductB , ProductC')
        
        while True:
          self.x=(input('enter the product as shown above '))  
          if self.x in self.items:
              self.Quantity = int(input('enter number of quantity '))
              if self.Quantity>10:
                sub={(self.Quantity*(self.items[self.x]))-((5/100)*(self.Quantity*(self.items[self.x]))):self.Quantity}
              elif self.Quantity<10:
                sub={(self.Quantity*(self.items[self.x])):self.Quantity}
          elif self.x == 'quit':
                  break
             
          x.append(sub)
          y.append(self.x)
        


        
        # discount 
        sum_cart_product = [sum(dictionary.keys()) for dictionary in x]
        r=(sum(sum_cart_product))
        
        
        
        sum_quantity = [sum(dictionary.values()) for dictionary in x]
        q=(sum(sum_quantity))
        self.ship=(q//10)*5
        print('Product Nmae                 sub-total & Quantity\n',y,x)
        
        if r<=200 :
            self.b=r-10
            print('Discount Applied :- flat $10 discount amount :- ',self.b)
            self.g=1*self.b
            T=self.b+self.g+self.ship
            print('Here is your product sheeping and gift wrap amount:-',self.g,      self.ship)
            print('Your total amount is ',T)
            
        elif q<=20  :
            self.c=(r)-((10/100)*r)
            print('Discount Applied :- flat 10%_discount amount :- ',self.c)
            self.g=1*self.c
            T=self.c+self.g+self.ship
            print('Here is your product sheeping and gift wrap amount:-\n',self.g,self.ship)
            print('Your total amount is ',T)
            
        elif q>30 and self.Quantity>=15 :
            self.d=(r)-((50/100)*r)
            print('Discount Applied :- flat 50%_discount amount :- ',self.d)
            self.g=1*self.d
            T=self.d+self.g+self.ship
            print('Here is your product sheeping and gift wrap amount:-\n',self.g,self.ship)
            print('Your total amount is ',T)

        
       
          
          
          
               
z=shopping()
z.product()
               
                

        