def moving_average(numbers, window_size):
        
    lst = []
        
    for i in range(len(numbers)):
        if len(lst) == window_size:
            lst.pop(0)
            lst.append(numbers[i])
        else:
            lst.append(numbers[i])
        
        print(lst)
        yield sum(lst) / len(lst)
        
nums = moving_average([10,20,30,40,50,60,70,80,90,100,110,120,130,140,150], 5)

try:
    while True:
        print(next(nums))
except StopIteration:
    print("Done!")


#Step	Window Contents	Computed Moving Average
#1	[10]	10.0
#2	[10, 20]	(10 + 20) / 2 = 15.0
#3	[10, 20, 30]	(10 + 20 + 30) / 3 = 20.0
#4	[20, 30, 40]	(20 + 30 + 40) / 3 = 30.0
#5	[30, 40, 50]	(30 + 40 + 50) / 3 = 40.0