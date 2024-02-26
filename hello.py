# def m(a, b):       
#     h = (a * b)/ (a + b)
#     print(h)


# m(a, b)
# a = 8
# b = 4
# print(m)

# import turtle
# turtle.bgcolor("black")
# squary = turtle.Turtle()
# def design():
#     squary.speed(20)
#     squary.pencolor("red")
#     for i in range(400):
#         squary.forward(i)
#         squary.left(91)
        
        


# import turtle
# import colorsys
# t = turtle.Turtle()
# def circle():
#     s=turtle.Screen().bgcolor('white')
#     t.speed(0)
#     n = 70
#     h = 0
#     for i in range(360):
#         c = colorsys.hsv_to_rgb(h, 1,   0.8)
#     h += 1/n
#     t.color(c)
#     t.left(1)
#     t.fd(1)
#     for i in range(2):
#         t.left(2)
#         t.circle(100)
  
  
# a = 6
# b = 9
# if (a>b):
#     design()
# else:
#     circle()
    


# def add_mumber(a, b):
#     return a * b

# result = add_mumber(374, 732)

# print(result)



# def greet(name):
#     print('hello, ' + name + '!')
    

# greet("Altaf")


# def add(num):
#     return num * num
    

# new = add(4)
# print(new)




# import os
# os.rename("new_file.py")os.
# if(not os.path.exists("data")):
#     os.mkdir("data")
# print(os.getcwd())
# for i in range(0, 100):
#     os.mkdir(f"Data/Day{i + 1}", "Data/Python {i + 1}")





# word_count = {
#     'video': 1,
#     'like': 9,
#     'view': 29,
#     'subscriber': 5
# }

# print(word_count.items())
# print(list(word_count.values()))
# print(list(word_count.keys()))

# print(word_count)
# print(word_count.popitem())
# print(word_count)



# print(sorted(list(word_count.values())))





# import datetime

# # Get the current date and time
# now = datetime.datetime.now()
# print("Current date and time:", now)

# # Create a specific date
# date = datetime.date(2023, 6, 5)
# print("Date:", date)

# # Create a specific time
# time = datetime.time(12, 30, 45)
# print("Time:", time)

# # Combine date and time into a datetime object
# datetime_obj = datetime.datetime.combine(date, time)
# print("Datetime object:", datetime_obj)

# # Parse a date string
# date_string = "2023-06-05"
# parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d")
# print("Parsed date:", parsed_date)

# # Format a datetime object as a string
# formatted_date = datetime_obj.strftime("%Y-%m-%d %H:%M:%S")
# print("Formatted date:", formatted_date)

# # Calculate a duration of time using timedelta
# duration = datetime.timedelta(days=5, hours=3)
# print("Duration:", duration)






# list1 = [1, 2, 3, 4, 5]
# list2 = ['one', 'two', 'three', 'four', 'five']

# zipped = list(zip(list1, list2))
# print(zipped)

# unzipped = list(zip(*zipped))
# print(unzipped)


# for (l1, l2) in zip(list1, list2):
#     print(l1)
#     print(l2)
    
    
    
    
    
# items = ['apple', 'orange', 'mango', 'banana']
# counts = [6, 5, 3, 12]
# prices = [1.23, 0.75, 0.34, 2.12]

# sentences = []
# for (item, count, price) in zip(items, counts, prices):
#     item, count, price = str(item), str(count), str(price)
#     sentence = 'I bought ' + count + ' ' + item + 's at ' + price + ' Dollars each.'
#     sentences.append(sentence)
    
# print(sentences)





import random 

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'guess the number between 1 and {x}: '))
        if guess > random_number:
            print('guess the number lower')
        elif guess < random_number:
            print('guess the number higher')
    print('Yah, the number you guessed is correct!')
    
guess(100)

