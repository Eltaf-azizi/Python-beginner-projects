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



