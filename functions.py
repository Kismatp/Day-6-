# def function_name(list_of_parameters):
#     # Body of function 
#     pass
#     # Return value

# Function to add two numbers:

def add_two_numbers(num1,num2=20):
    """
    This function add two numbers,

    Arguments:
        num1: First Number 
        num2: Second number 

    Return:
        sum of num1 and num2 

    
    """


    sum=num1+num2
    return sum 


sum=add_two_numbers(10,20 ) # Positional arguments
print(sum)

# Keyboard arguments 
sum= add_two_numbers(num1=10, num2=20 )
print(f"Sum is: {sum}")

# Using Deafult argument
sum= add_two_numbers(10)
print(f"Sum with default argument is: {sum}")


# Unpacking of list, tuple
list1 = [10,20,30,40,50,60]
# We can use * operator to unpack sequence 

x,*y,z= list1
print(x,y,z)

def sum(*var):
    sum=0
    for value in var:
        sum+=value
    return sum 

result=sum(10,20,30,40,50,60,70)
print(f"Sum is: {result}")




