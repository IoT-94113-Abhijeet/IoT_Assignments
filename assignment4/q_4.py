def histogram(number):
    for num in number:
        print(f"{num}: {'*' * num}")

a=int(input(f"enter the value :"))
b=int(input(f"enter the value :"))
c=int(input(f"enter the value :"))
histogram({a,b,c})
