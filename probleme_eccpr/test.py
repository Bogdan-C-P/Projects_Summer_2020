import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import chart_studio.plotly as pl
import plotly.offline as po
import cufflinks as cf

po.init_notebook_mode(connected=True)
cf.go_offline()

def create_data(data):
    if data==1:
        x = np.random.rand(100,5)
        df1 = pd.DataFrame(x, columns=["A", "B", "C", "D", "E"])
    elif data==2:
        x = [0, 0, 0, 0, 0]
        r1 = [0, 0, 0, 0, 0]
        r2 = [0, 0, 0, 0, 0]
        r3 = [0, 0, 0, 0, 0]
        r4 = [0, 0, 0, 0, 0]
        print("Enter the values for columns")
        for i in range(len(x)):
            x[i]=(input())
        print("Enter the values for first row")
        for i in range(len(x)):
            r1[i] = int(input())
        print("Enter the values for second row")
        for i in range(len(x)):
            r2[i] = int(input())
        print("Enter the values for third row")
        for i in range(len(x)):
            r3[i] = int(input())
        print("Enter the values for forth row")
        for i in range(len(x)):
            r4[i] = int(input())
        df1=pd.DataFrame([r1, r2, r3, r4], columns= x)
    elif data==3:
        file = input("Enter files name(+extension): ")
        x = pd.read_csv(file)
        df1 = pd.DataFrame(x)
    else:
        print("DataFrame creation failed please try again: ")
    return df1
def plotter(plot):
    if plot == 1:
        final_plot=df1.iplot(kind="scatter")
    elif plot ==2:
        final_plot = df1.iplot(kind="scatter", mode="markers", symbol="x",colorscale="paired")
    elif plot == 3:
        final_plot=df1.iplot(kind="bar")
    elif plot == 4:
        final_plot = df1.iplot(kind="hist")
    elif plot == 5:
        final_plot = df1.iplot(kind="box")
    elif plot == 6:
        final_plot = df1.iplot(kind="surface")
    else:
        final_plot=print("Please try again")
    return final_plot.show()


def plotter2(plot):
    col = int(input("Enter ther number of columns you want to plot by selecting 1, 2 or 3: "))
    if col == 1:
        colm = input("enter the column you want to plot:")
        if plot == 1:
            final_plot = df1[colm].iplot(kind="scatter")
        elif plot == 2:
            final_plot = df1[colm].iplot(kind="scatter", mode="markers", symbol="x", colorscale="paired")
        elif plot == 3:
            final_plot = df1[colm].iplot(kind="bar")
        elif plot == 4:
            final_plot = df1[colm].iplot(kind="hist")
        elif plot == 5:
            final_plot = df1[colm].iplot(kind="box")
        elif plot == 6 or plot == 7:
            final_plot = print("imposible for a single column")
        else:
            final_plot = print("please try again")
    elif col == 2:
        colm = input("enter the first column you want to plot:")
        colm1=input("enter the second column :")
        if plot == 1:
            final_plot = df1[[colm,colm1]].iplot(kind="scatter")
        elif plot == 2:
            final_plot = df1[[colm,colm1]].iplot(kind="scatter", mode="markers", symbol="x", colorscale="paired")
        elif plot == 3:
            final_plot = df1[[colm,colm1]].iplot(kind="bar")
        elif plot == 4:
            final_plot = df1[[colm,colm1]].iplot(kind="hist")
        elif plot == 5:
            final_plot = df1[[colm,colm1]].iplot(kind="box")
        elif plot == 6 :
            final_plot = df1[[colm,colm1]].iplot(kind="surface")
        elif plot == 7:
            size=input("Please enter the size column for bubble plot")
            final_plot = df1.iplot(kind="bubble",x=colm,y=colm1,size=size)
        else:
            final_plot = print("please try again")
    elif col == 3:
        colm = input("enter the first column you want to plot:")
        colm1 = input("enter the second column: ")
        colm2 = input("enter the third column: ")
        if plot == 1:
            final_plot = df1[[colm, colm1,colm2]].iplot(kind="scatter")
        elif plot == 2:
            final_plot = df1[[colm, colm1,colm2]].iplot(kind="scatter", mode="markers", symbol="x", colorscale="paired")
        elif plot == 3:
            final_plot = df1[[colm, colm1,colm2]].iplot(kind="bar")
        elif plot == 4:
            final_plot = df1[[colm, colm1,colm2]].iplot(kind="hist")
        elif plot == 5:
            final_plot = df1[[colm, colm1,colm2]].iplot(kind="box")
        elif plot == 6:
            final_plot = df1[[colm, colm1,colm2]].iplot(kind="surface")
        elif plot == 7:
            size = input("Please enter the size column for bubble plot")
            final_plot = df1.iplot(kind="bubble", x=colm, y=colm1,z=colm2, size=size)
        else:
            final_plot = print("please try again")
    else:
        final_plot=print("please try again")
    return final_plot.show()
def main(cat):
    if cat==1:
        print("Select the type of plot you need (choose from 1 to 6): ")
        print("1.Line plot")
        print("2.Scatter plot")
        print("3.Bar plot")
        print("4.Histogram")
        print("5.Box plot")
        print("6.Surface plot")
        plot=int(input())
        output=plotter(plot)
    elif cat==2:
        print("Select the type of plot you need (choose from 1 to 7): ")
        print("1.Line plot")
        print("2.Scatter plot")
        print("3.Bar plot")
        print("4.Histogram")
        print("5.Box plot")
        print("6.Surface plot")
        print("7.Bubble plot")
        plot=int(input())
        output=plotter2(plot)
    else:
        print("Please enter 1 or 2")
    return output



print("Select the type of data you need to plot (1 2 or 3): ")
print("1. Random data (100 rows 5 columns) ")
print("2. Customize data frame with 5 columns and 4 rows ")
print("3 Upload csv/json/txt file ")

data = int(input())
df1 = create_data(data)



print("Your DataFrame head is given below check the columns to plot using cufflinks")
print(df1.head())
print("what kind of plot do you need, the complete data plot or column plot")
cat=int(input("Press 1 for plotting all columns or press 2 to specify columns to plot"))

main(cat)