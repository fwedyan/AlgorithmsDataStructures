############# My library ############################
###### a function that can be used to validate integer inputs
# the function takes two parameters, upper and lower limit
# and returns the validated input
############################################################
def validate(msg, lower, upper):
   if (lower > upper):
        #swap them!
        lower = upper
        upper = lower
   var = int(input(msg))
   while (var<lower or var >upper):
       print("incorrect input, should be in the range [",lower,",",upper,"]")
       var = int(input("read the requested value: "))
  
   
   return var


def validateIntegerInput(msg, lower):
  """ get an integer value higher than the given lower
    """

  while True:
     try:
         var = int(input(msg))
         while (var<lower):
             print("incorrect input, should be larger or equal to ",lower)
             var = int(input("read the requested value: "))
         break
     except ValueError:
         print("Invalid input, please try again....")
    
  
  return var

############################
# finds the averarge [1...N]
# precondition: N>=1
###########################
def average(N):
    sum=0
    for i in range(1,N+1):
        sum +=i
    avg = sum/N
    return avg

##############################
# function finds the factorial of a given number
# precondition: input >=0
#################################
def factorial(N):
    f =1
    if N==0:
        return 1
    if N==1:
        return 1
    for i in range(1,N+1):
        f*=i
    return f

##########################################
# Function to find whether a given number is prime
# precondition: integer number
###########################################
def isPrime(n):
    prime = True
    i = 2
    while (i<=n/2 and prime==True):
        if (n%i==0):
            prime=False
        i+=1
    return prime

#############################################
def min(a,b):
    m = a
    if b>m:
        m =b
    return m

##################################################
def gcd(a,b):
    m = min(a,b)
    i = m;
    gcd = 1
    found = False
    while i>1 and found == False:
        if a%i==0 and b%i==0:
            gcd = i
            found=True
        else:
            i-=1
    return gcd
##
        

