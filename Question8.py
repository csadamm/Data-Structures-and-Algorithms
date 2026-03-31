'''
Our goal is to find an approximation for the square root of n
i.e x = root(n)
i.e x^2 = n
Therefore: f(x) = x^2 - n is our function on which we will apply the Newton-Raphson metho

The Newton-Raphson method is that x_k+1 = x_k - (f(x_k)/f'(x_k))
In our case;
    f(x_k) = (x_k)^2 - n
    f'(x_k) = 2(x_k)
    
When f(x) = 0 -> x^2 - n = 0
              -> x^2 = n
              -> x = root(n)
              
So we will repeat the Newton Raphson method until f(x) = 0, as when we reach this point we will get:
x_k+1 = x_k - (0/2(x_k))
x_k+1 = x_k
Therefore each value after will be the same, hence we have reached the square root of n
'''
n = float(input("Input the number you would like to find the root of: "))
if n < 0:
    print("Error: Cannot find square root of a negative number")
else:
    #Our initial value will be n/2 unless n <= 1
    if n > 1:
        x = n/2
    else:
        x = 1

    #x**2 - n is f(x)
    #We set a max_iterations in case something goes wrong, to prevent an infinite loop
    max_iterations = 1000
    for _ in range(max_iterations):
        # We round the number as due to floating point precision, some numbers may not ever reach 0
        if (round((x**2)-n, 8) == 0):
            break
        x = x - ((x**2 - n)/(2*x))

    print(f"The squareroot of {n} is {x}")
