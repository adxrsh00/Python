def print_table(num):
   """ This function prints multiplication table of a given number"""
   for i in range(2,21):
       print(num,' x ', i, ' = ',num*i)
# end of function table
# input a number
n = int(input("Please Enter a number to print its multiplication table:"))
print_table(n)
