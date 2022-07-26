import streamlit as st
import sys

tab1, tab2,tab3,tab4,tab5,tab6= st.tabs(["First ", "Second","Third","Fourth","Fifth","Sixth"])
with tab1:
    st.title("Welcome to streamlit practices lab !")
    st.write("Here we're going to use python to solve some problems .")
    st.write("There'll be a practice followed by the solution that would be explained through a comment .")

    st.write("Here i'll import the library that we'll be using through that line of code :")
    st.code("""
    import streamlit as st
    #I've used that to import streamlit library as st for a shortcut so
    #i won't write on every call streamlit , i'll write st unstaid


    import sys
    #I've used that to display the used version of python
    """,language="python")
    st.write('---')

    st.header("First practice : ")
    st.write("### Display -hello world !- on the page ")
    st.write("here's the solution : hello world !")
    code="""
    #This is the code solution :
    st.write("hello world !")
    #I've used the function st.write
    """
    st.code(code,language="python")



    st.write('---')




    st.header("Second practice : ")
    st.write("### Display -Hello , i'm born on the year 1997 welcome !- with the date number stored on another variable .")


    year=1997
    st.write("Here's the solution : i'm born on the year ",year,' welcome ! ')
    st.write("Here's another solution : i'm born on the year "+str(year)+" welcome !")
    st.write(f"and here's another solution :i'm born on the year {year} welcome!")

    st.code("""
    year=1997
    st.write("i'm born on the year ",year,' welcome ! ')
    #Here as you can see , i've used a coma to separate the year from the string
    #so it displayed it not as a string but as a number , as it is ,
    #and that's why it's wroten differently .

    st.write("i'm born on the year "+str(year)+" welcome !")
    #Here i've changed the type of the number to a string then i've
    #concatenate it with the rest of the string and that's why it's
    #all writen on the same way .


    st.write(f"i'm born on the year {year}")
    #This is the same thing as the second solution but it's faster .

    """,language="python")


    st.write('---')
    st.header("3rd practice : ")
    st.write('### Display the used version of streamlit and python .')
    st.write("here's the solution : ")
    st.write("The used version of streamlit : "+st.__version__ )
    st.write("The used version of python : "+sys.version)
    st.code("""
    #Here's the code solution :
    st.write("The used version of streamlit : "+st.__version__ )
    #st.__version__ would giveback the streamlit version used .
    st.write("The used version of python : "+sys.version)
    #sys.version would give back the version of python used with
    #more informations

    """,language="python")


    st.write('---')
    st.header('4th practice : ')
    st.write("### Display the current time and date ")
    st.write("Here's the solution : ")


    import datetime
    current_time_and_date = datetime.datetime.now()
    st.write("The current time and date is : "+str(current_time_and_date))
    st.code("""
    import datetime
    #I've imported that library to use it to extract the time and the date of
    #the current momment .


    current_time_and_date = datetime.datetime.now()
    #Then i've called the function now from datetime to extract the data
    #and put it into a variable

    st.write("The current time and date is : "+str(current_time_and_date))
    #Then i've wrote it through concatenation with the string also
    #changing the datatype to str
    """,language="python")





with tab2:
    st.title("This is the continuation of the previous practices .")
    st.header("5th Practice")
    st.write("### Write a program that would take two intiger as an entry , then the user would choose to substract , add ,devide or multiply them together .(Take in consideration the devision by 0)")
    st.write("Here's the solution : ")
    #Definition of the functions with lambda
    add=lambda x,y:x+y
    substract=lambda x,y:x-y
    devide=lambda x,y:x/y if y!=0 else 'error'
    multiply=lambda x,y:x*y
    t1,t2=st.columns([1,1])
    with t1:
        x = st.number_input('Enter the first number')
    with t2:
        y = st.number_input('Enter the second number')

    st.write("choose the operation :")
    result=0
    f1,f2,f3,f4=st.columns([1,1,1,1])
    with f1:
        addition=st.button('Addition')
    with f2:
        substraction=st.button('Substraction')
    with f3:
        multiplication=st.button('Multiplication')
    with f4:
        devision=st.button('Devision')
    if addition:
        result=add(x,y)
    elif substraction:
        result=substract(x,y)
    elif devision:
        result=devide(x,y)
    elif multiplication:
        result=multiply(x,y)
    st.write(f'The result is : {result}')

    st.write("Here's the code solution :")
    st.code("""

add=lambda x,y:x+y
substract=lambda x,y:x-y
devide=lambda x,y:x/y if y!=0 else 'error'
multiply=lambda x,y:x*y

#I've defined all the functions with lambda , it's faster and effecient .

t1,t2=st.columns([1,1])
#Then i've created colummns with equal size in order to be displayed on
#the same row and to let the user freely enter the variable and on
#a clean way .

with t1:
    x = st.number_input('Enter the first number')
with t2:
    y = st.number_input('Enter the second number')
#Then i've got the variables given by the input function and stored it
#on x and y


st.write("choose the operation :")
#That would print to choose the operation

result=0
#I've made a variable called result to store the calculation in it .


f1,f2,f3,f4=st.columns([1,1,1,1])
#Then i've created columns in order to let the user the freedom of choise

with f1:
    addition=st.button('Addition')
with f2:
    substraction=st.button('Substraction')
with f3:
    multiplication=st.button('Multiplication')
with f4:
    devision=st.button('Devision')
#I've stored the button calls in variables by their name

if addition:
    result=add(x,y)
elif substraction:
    result=substract(x,y)
elif devision:
    result=devide(x,y)
elif multiplication:
    result=multiply(x,y)
#Then i've checked each independent variable name with the if and
#else statements then stored the return value from each
#function call on the result.


st.write(f'The result is : {result}')
#And by the end i've wrote the result with st.write and used the format
#function to write it on a simple way .
#And voila !
    """,language="python")

    st.write('---')
    st.header("6th practice")
    st.write("### Write an algorithm that would calculate a second degree function :(x+c)^2  ")
    sdf=lambda x,c:x*x+2*x+c
    st.write("Here's the formula of a second degree function : (x+c)^2 , please enter the following numbers")
    lm1,lm2=st.columns([1,1])
    with lm1:
        x=st.number_input("Enter the value of X :")
    with lm2:
        c=st.number_input("Enter the value of C ;")
    st.write("Here's the result : ",sdf(x,c))

    st.write("Here's the code solution : ")
    st.code("""
sdf=lambda x,c:x*x+2*x+c
#Here i've created a function with lambda , it's quick and effecient
#to calculate the result of the second degree function


lm1,lm2=st.columns([1,1])
#Then i've created two columns so the user would see clearly
#what to enter and where


with lm1:
    x=st.number_input("Enter the value of X :")
with lm2:
    c=st.number_input("Enter the value of C ;")
#I've used same thing on the previous practice .
#i received the input using the streamlit api call .


st.write("Here's the result : ",sdf(x,c))
#By the end i've displayed the results and didn't switch to string .
    """,language ="python")

with tab3:
    st.title("This is the third part of the basics of python and streamlit .")
    st.header("7th practice")
    st.write("### Write a program that would find the smallest and the biggest number in an array of 1 Dimention , the length of the array could be any , the array contains floats . (take into consideration the empty array .)")
    st.write("Here's the solution :")

    array=[14,8,9,25,0,-1]
    #array=[]

    #I've defined two arrays one that contains numbers and the other is
    #empty

    #At the beginning i've defined the array that i'll be working with.
    st.write("The array is : ",array)

    def small_big(arr):
        if len(arr)!=0:
            small=arr[0]
            big=arr[0]
        else :
            return "The array is empty ."
        for i in array:
            if i<small :
                small=i
            if i>big:
                big=i
        return big,small



    result = small_big(array)
    if isinstance(result, str):
        st.write("The array is empty")
    else :
        big,small=small_big(array)
        st.write(f"The smallest number of the array is {small} and the biggest number of the array is {big} .")
    st.write("Here's the code solution :")


    st.code("""
array=[14,8,9,25,0,-1]
#array=[]

#I've defined two arrays one that contains numbers and the other is
#empty

#At the beginning i've defined the array that i'll be working with.
st.write("The array is : ",array)

def small_big(arr):
    if len(arr)!=0:
        small=arr[0]
        big=arr[0]
    else :
        return "The array is empty ."
    for i in array:
        if i<small :
            small=i
        if i>big:
            big=i
    return big,small
#Then i've defined the function that has two return vales .
#I've put the first array of the list into the variable
#small and big that refers to the smallest and the biggest
#variables on the array .
#Then i went through the list looking if there was any variable
#inside the list if its bigger than the big or smaller than the
#small variable and from there i've changed the values .
result = small_big(array)
if isinstance(result, str):
    st.write("The array is empty")
else :
    big,small=small_big(array)
    st.write(f"The smallest number of the array is {small} and the biggest number of the array is {big} .")
#I've displayed the results in case the array is empty and in case
#there's numbers on the array .
""" ,language="python")
    st.write("---")

    st.header("8th practice ")
    st.write("### Write a program that would append one number into the array and remove it from the array .(take in consideration the empty array )")
    st.write("Here's the solution :")

    arrr=[0,5,12,150,25]
    if "arrr" not in st.session_state:
        st.session_state['arrr']=arrr

    added_value=st.number_input("Enter the value of the last element: ",1)
    ladd=st.button("Add to the list ! !")
    if ladd:
        st.session_state['arrr'].append(added_value)
    popping=st.button("Pop the last element out !")
    if popping:
        if st.session_state['arrr']!=[]:
            st.session_state['arrr'].pop()

    st.write(st.session_state['arrr'])

    st.write("Here's the code solution : ")
    st.code("""
arrr=[0,5,12,150,25]
#first i initiated the list .


if "arrr" not in st.session_state:
    st.session_state['arrr']=arrr

#Then i've charged the variable into a session_state to store it
#and to make it accecible and modifiable because
#we're going to use it all along the program .


added_value=st.number_input("Enter the value of the last element: ",1)
#Then i've took an input of the user entered number.


ladd=st.button("Add to the list ! !")
#After that i've used a button to add to the list .

if ladd:
    st.session_state['arrr'].append(added_value)
#Then i've used the if statement set to be triggered
#if the user enter a new value .
#So the entered value would be automatically stored
#into our array .


popping=st.button("Pop the last element out !")
#Then i've added a button to pop out the last element .


if popping:
    if st.session_state['arrr']!=[]:
        st.session_state['arrr'].pop()
#if it's triggered and array is not empty , the last element
#would pop out .

st.write(st.session_state['arrr'])
#By the end i've wrote down all the array with st.write
""",language="python"
    )


with tab4:
    st.title("4th part of solving practices using python and streamlit .")
    st.write("On this part we're going to make plots using different libraries ")
    st.write("---")
    st.header("8th practice")
    st.write("### Plot a line chart of a random 1D table .")
    st.write("Here's the solution : ")
    from numpy import random
    x = random.randint(0,5,10)
    st.line_chart(x)
    st.write("Here's the code solution : ")

    st.code("""
from numpy import random
#We'll use that library to generate random numbers .

x = random.randint(0,5,10)
#In here i generated 10 random numbers from 0 to 4.

st.line_chart(x)
#This is how i plotted the line chart .
    """)

    st.write("---")
    st.header("9th practice")
    st.write("### Plot a bar chart of a random 1D table")
    st.write("Here's the solution : ")
    x = random.randint(0,5,10)
    st.bar_chart(x)
    st.write("Here's the code solution : ")

    st.code("""
x = random.randint(0,5,10)
#In here i generated 10 random numbers from 0 to 4 ,
#same thing is we did before .

st.bar_chart(x)
#This is how i plotted the bar chart .

    """)
    st.write('---')
    st.header("10th practice")
    st.write("### Plot an area chart of a 2D array .")
    st.write("Here's the solution : ")
    x = random.randint(0,5,(10,2))
    st.area_chart(x)
    st.write("Here's the code solution : ")
    st.code("""
x = random.randint(0,5,(10,2))
#In here i've done the same thing as before but now , i've
#choose 2D array with the length of 10 in each .


st.area_chart(x)
#With that line of code i've plotted the line chart of the array.
    """,language="python")
    st.write("---")
    st.header("11th practice")
    st.write("### Use matplotlib to plot a 1D chart .")
    st.write("Here's the solution : ")
    import matplotlib.pyplot as plt
    x=random.randint(0,5,10)


    fig, ax = plt.subplots()
    ax.hist(x)
    st.pyplot(fig)
    st.write("Here's the code solution : ")
    st.code("""
import matplotlib.pyplot as plt
#Here i've imported pyplot from matplotlib as plt
#as a shortcut .

x=random.randint(0,5,10)
#in here i've generated the empty array .

fig, ax = plt.subplots()
ax.hist(x)
#here i've called the function subplots to plot
#the selected data
#i've received two variables
#one that we'll use to plot
#and the other to assign the array that we want to plot

st.pyplot(fig)
#this function would plot the graph in streamlit web application
    """,language="python")

with tab5:
    st.title("5th part of solving practices using python and streamlit .")
    st.write ("Here we would display multiple charts on the window .")
    st.write("---")
    st.header("12th practice")
    st.write("### Plot 4 charts , two by two of a random 1D array.")
    st.write("Here's the solution : ")
    c1=random.randint(0,5,10)
    c2=random.randint(0,5,10)
    c3=random.randint(0,5,10)
    c4=random.randint(0,5,10)

    cc1,cc2=st.columns([1,1])
    with cc1:
        st.line_chart(c1)
        st.line_chart(c2)
    with cc2:
        st.line_chart(c3)
        st.line_chart(c4)

    st.write("Here's the code solution :")
    st.code("""
    c1=random.randint(0,5,10)
    c2=random.randint(0,5,10)
    c3=random.randint(0,5,10)
    c4=random.randint(0,5,10)
    #In here i generated 10 random numbers from 0 to 4
    #them on an array

    cc1,cc2=st.columns([1,1])
    #In here i created two columns using streamlit.

    with cc1:
        st.line_chart(c1)
        st.line_chart(c2)
    #I used the first column to plot the first two charts.
    with cc2:
        st.line_chart(c3)
        st.line_chart(c4)
    #I used the second column to plot the second two charts .
    """,language="python")

    st.write("---")
    st.header('Practice number 13')
    st.write("### Write a code that would display 4 plotly charts two by two.")
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots


    fig = make_subplots(
        rows=2, cols=2,
        specs=[[{"type": "xy"}, {"type": "polar"}],
               [{"type": "domain"}, {"type": "scene"}]],
    )
    y=random.randint(1,10,5)
    fig.add_trace(go.Bar(y=y),row=1, col=1)
    theta=random.randint(0,360,5)
    r=random.randint(1,100,4)
    fig.add_trace(go.Barpolar(theta=theta, r=r),row=1, col=2)
    value=random.randint(1,5,4)
    fig.add_trace(go.Pie(values=value),row=2, col=1)
    x=random.randint(0,6,10)
    y=random.randint(0,6,10)
    z=random.randint(0,6,10)
    fig.add_trace(go.Scatter3d(x=x, y=y,z=z, mode="lines"),row=2, col=2)

    st.plotly_chart(fig)

    st.write("Here's the code solution : ")
    st.code("""
import plotly.graph_objects as go
from plotly.subplots import make_subplots
#Here i imported the libraries that i need .


fig = make_subplots(
    rows=2, cols=2,
    specs=[[{"type": "xy"}, {"type": "polar"}],
           [{"type": "domain"}, {"type": "scene"}]],
)
#In here i initiated the subplots


y=random.randint(1,10,5)
fig.add_trace(go.Bar(y=y),row=1, col=1)
#in here i generated the random numbers and added a trace
#to the final plot that we're going to make .


theta=random.randint(0,360,5)
r=random.randint(1,100,4)
fig.add_trace(go.Barpolar(theta=theta, r=r),row=1, col=2)
#In here i did the same thing as previous , hence the plots are
#Different so they would need different parameters that i generated.


value=random.randint(1,5,4)
fig.add_trace(go.Pie(values=value),row=2, col=1)
#I've done the same thing over here , generating new parameters
#and plotting it on the chart .


x=random.randint(0,6,10)
y=random.randint(0,6,10)
z=random.randint(0,6,10)
fig.add_trace(go.Scatter3d(x=x, y=y,z=z, mode="lines"),row=2, col=2)
#this was about plotting a 3D chart
#it requires 3D array input , each one on a different array .

#I was able to not display the labels but i kept them .

st.plotly_chart(fig)
#By the end i've plotted the fig variable that we kept adding to
#it during all the process and it was the final result .
    """,language="python")
    st.write("---")
    st.header("Practice number 14 ")
    st.write("### Display 4 charts using matplotlib two by two ")
    st.write("Here's the solution :")
    import matplotlib.pyplot as plt
    fig, axs = plt.subplots(2, 2)
    x=random.randint(0,6,10)
    axs[0, 0].plot(x)
    axs[0, 0].set_title('Plot number 1')

    x=random.randint(0,6,10)
    axs[0, 1].plot(x, 'tab:orange')
    axs[0, 1].set_title('Plot number 2')

    x=random.randint(0,6,10)
    axs[1, 0].plot(x, 'tab:green')
    axs[1, 0].set_title('Plot number 3')

    x=random.randint(0,6,10)
    axs[1, 1].plot(x, 'tab:red')
    axs[1, 1].set_title('Plot number 4')

    for ax in axs.flat:
        ax.label_outer()
    st.pyplot(fig)

    st.write("Here's the code solution : ")
    st.code("""
import matplotlib.pyplot as plt
#In here i've imported the library that i'll use .


fig, axs = plt.subplots(2, 2)
#Over here i've made subplots to follow the instructions .

x=random.randint(0,6,10)
axs[0, 0].plot(x)
axs[0, 0].set_title('Plot number 1')
#Here i generated the random numbers .
#After that i've plotted them into their part from the subplots.
#so each plot would go to it place

x=random.randint(0,6,10)
axs[0, 1].plot(x, 'tab:orange')
axs[0, 1].set_title('Plot number 2')
#Same thing here .
#as you can see i've added the title .


x=random.randint(0,6,10)
axs[1, 0].plot(x, 'tab:green')
axs[1, 0].set_title('Plot number 3')
#same thing here and on the one below .

x=random.randint(0,6,10)
axs[1, 1].plot(x, 'tab:red')
axs[1, 1].set_title('Plot number 4')

for ax in axs.flat:
    ax.label_outer()
#in order for the display would be on it place i've used
#this method to hide the X axis numbers .

st.pyplot(fig)
#At the end i've plotted the final figure using this function.
    """)

with tab6:
    st.title("Welcome to solving the practices using python and streamlit !")
    st.write("Here we'll create object and see how it works using python and streamlit .")
    st.write("---")
    st.header("Practice number 15")
    st.write("### Create an object named living_being and put on it the following variables :name,age, height and the weight ; Also make two inputs and a button to push the objects into an array and pop the last element, display the array at the end.")
    st.write("Here's the solution : ")
    class living_being:
        def __init__(self,name,height,weight,age):
            self.height=str(height)+'cm'
            self.weight=str(weight)+'kg'
            self.name=name
            self.age=str(age)+"years"



    if "tb" not in st.session_state:
        tb=[]
        st.session_state['tb']=tb

    en1,en2=st.columns([1,1])
    with en1:
        name=st.text_input("Enter the name of the living being","cat")
        height=st.number_input("Enter the height",60)
        weight=st.number_input("Enter the weight",2)
        age=st.number_input("Enter the age",2)

    with en2:
        st.write("")
        st.text("")
        t1=st.button("Add object to the list")
        tZ=st.button("Push the last element of the list of objects out .")

    if t1:

        lb=living_being(name,height,weight,age)
        st.session_state['tb'].append(lb)
    elif tZ:
        if st.session_state['tb']!=[]:
            st.session_state['tb'].pop()
    st.write("Here's the element of your list : ")
    for i in st.session_state['tb']:
        st.write(vars(i))
    st.write("Here's the code solution : ")

    st.code("""
class living_being:
    def __init__(self,name,height,weight,age):
        self.height=str(height)+'cm'
        self.weight=str(weight)+'kg'
        self.name=name
        self.age=str(age)+"years"
#At the start i've defined a class to create the objects from it .
#i've put the method init to initiate the things that i will use


tb=[]
#After that i've created a new table .

if "tb" not in st.session_state:
    st.session_state['tb']=tb
#Then i've called the session state to store the variable in that array
#And we'll later on put the objects of that class in it.


en1,en2=st.columns([1,1])
#After that i've created two columns to make the data look presentable.

with en1:
    name=st.text_input("Enter the name of the living being","cat")
    height=st.number_input("Enter the height",60)
    weight=st.number_input("Enter the weight",2)
    age=st.number_input("Enter the age",2)
#On the first column i received the inputs .

with en2:
    st.write("")
    st.text("")
    t1=st.button("Add object to the list")
    tZ=st.button("Push the last element of the list of objects out .")
#On the second column i've put the buttons in order to push in or pop
#out of the list .


if t1:
    lb=living_being(name,height,weight,age)
    st.session_state['tb'].append(lb)
#In here if the user pressed the button to push hte data it would be triggered.

elif t2:
    if st.session_state['tb']!=[]:
        st.session_state['tb'].pop()
#same thing here but to pop the last element out .

st.write("Here's the element of your list : ")
for i in st.session_state['tb']:
    st.write(vars(i))
#here i've plotted the data

    """,language="python")

    st.write("---")
    st.header("Practice number 16")
    st.write("### Write a program that would create objects of animal that would heritate from the previous created class with the methods eat , sleep and live that would print that those those actions,call those functions if the user press a button , add the variable type in it.(Take the informations from the user just like the previous practice .) ")
    st.write("Here's what should be printed by calling the method eat :  the animal cat has the name of rose is living ")
    class animal(living_being):
        def __init__(self,name,height,weight,age,type):
            super().__init__(name,height,weight,age)
            self.type=type
        def eat(self):
            return "the animal "+self.type+" has the name of "+self.name +" is eating "
        def sleep(self):
            return "the animal "+self.type+" has the name of "+self.name +" is sleeping "
        def live(self):
            return "the animal "+self.type+" has the name of "+self.name +" is living "

    ta=[]

    if "ta" not in st.session_state:
        st.session_state['ta']=ta

    st1,st2=st.columns([1,1])

    with st1:
        name=st.text_input("Enter the name of the animal","rose")
        height=st.number_input("Enter the height of the animal",60)
        weight=st.number_input("Enter the weight of the animal",2)
        age=st.number_input("Enter the age of the animal",2)

    with st2:

        type=st.text_input("Enter the type of the animal","cat")
        p1=st.button("Add object to the list of animals")
        p2=st.button("Push the last element of the list of objects animals out .")

    if p1:
        lb=animal(name,height,weight,age,type)
        st.session_state['ta'].append(lb)

    elif p2:
        if st.session_state['ta']!=[]:
            st.session_state['ta'].pop()

    final_print=""
    x1,x2,x3=st.columns([1,1,1])
    with x1:
        eat=st.button("Eat")
    with x2:
        sleep=st.button("Sleep")
    with x3:
        live=st.button("live")


    if eat:
        if st.session_state["ta"]!=[]:
            final_print=st.session_state['ta'][-1].eat()
    if sleep:
        if st.session_state["ta"]!=[]:
            final_print=st.session_state['ta'][-1].sleep()
    if live:
        if st.session_state["ta"]!=[]:
            final_print=st.session_state['ta'][-1].live()

    st.write("Here's the result : "+final_print)
    st.write("Here's the element of your list : ")
    for i in st.session_state['ta']:
        st.write(vars(i))
    st.write("Here's the code solution : ")
    st.code("""
class animal(living_being):
    def __init__(self,name,height,weight,age,type):
        super().__init__(name,height,weight,age)
        self.type=type
    def eat(self):
        return "the animal "+self.type+" has the name of "+self.name +" is eating "
    def sleep(self):
        return "the animal "+self.type+" has the name of "+self.name +" is sleeping "
    def live(self):
        return "the animal "+self.type+" has the name of "+self.name +" is living "
#in here i've initiated the class animal that's heritating from
#the class living being .


ta=[]
#After that i've initiated an empty array
if "ta" not in st.session_state:
    st.session_state['ta']=ta
#I've called the session state to store the empty array if
#it does not exist


st1,st2=st.columns([1,1])
#After that i've created two columns


with st1:
    name=st.text_input("Enter the name of the animal","rose")
    height=st.number_input("Enter the height of the animal",60)
    weight=st.number_input("Enter the weight of the animal",2)
    age=st.number_input("Enter the age of the animal",2)
#I putted on the first column the inputs of the user and setted
#the default values .


with st2:

    type=st.text_input("Enter the type of the animal","cat")
    p1=st.button("Add object to the list of animals")
    p2=st.button("Push the last element of the list of objects animals out .")
#I've put a text input as well as buttons to receive
#what the user entered .


if p1:
    lb=animal(name,height,weight,age,type)
    st.session_state['ta'].append(lb)


elif p2:
    if st.session_state['ta']!=[]:
        st.session_state['ta'].pop()
#Same thing as the previous practice


final_print=""
x1,x2,x3=st.columns([1,1,1])
with x1:
    eat=st.button("Eat")
with x2:
    sleep=st.button("Sleep")
with x3:
    live=st.button("live")
#In here i've created three columns
#On each one there's a button .


if eat:
    if st.session_state["ta"]!=[]:
        final_print=st.session_state['ta'][-1].eat()
if sleep:
    if st.session_state["ta"]!=[]:
        final_print=st.session_state['ta'][-1].sleep()
if live:
    if st.session_state["ta"]!=[]:
        final_print=st.session_state['ta'][-1].live()
#If one of those three buttons is pressed the correspendant
#method would be called from the last element of the array of objects.


st.write("Here's the result of the last element of the array of objects: "+final_print)
st.write("Here's the element of your list : ")
for i in st.session_state['ta']:
    st.write(vars(i))
#At the end i've printed the final result
#As well as the array of objects and its values .
    """,language="python")

















    #
