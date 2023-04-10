import time

# 1
variable = input('Input your variable!\n')
for i in variable:
    if i.isalnum():
        if i.isdigit():
            print(f"It's {['odd', 'even'][int(i) % 2 == 0]} number!")
        else:
            print(f"It's {['lower', 'upper'][i.isupper()]} letter!")
    else:
        print("It's a symbol!")

# 2
while x := 1 > 0:
    print("I love Python")
    time.sleep(4.2)
