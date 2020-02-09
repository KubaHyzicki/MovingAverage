#!/usr/bin/python3

from random import randint
from tkinter import *

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        self.ma=movingAverage()
        master.title("Moving average APP")

        self.message = StringVar()
        self.messageBox = Message(root, textvariable=self.message, width=100) #, height=10)
        self.messageBox.pack()
        self.message.set("Greetings Traveler, go ahead and do whatever u want!")


    #entries
        entriesMainFrame = Frame(master)

        tabSizeFrame = Frame(entriesMainFrame)
        tabSizeLabel = Label(tabSizeFrame, text="tabSize")
        self.tabSizeEntry = Entry(tabSizeFrame, textvariable=StringVar(), width=5)
        self.tabSizeEntry.insert(0,self.ma.getTabSize())
        tabSizeLabel.pack()
        self.tabSizeEntry.pack( side = BOTTOM)
        tabSizeFrame.pack( side = LEFT )

        minFrame = Frame(entriesMainFrame)
        minLabel = Label(minFrame, text="min")
        self.minEntry = Entry(minFrame, textvariable=StringVar(), width=5)
        self.minEntry.insert(0,self.ma.getMin())
        minLabel.pack()
        self.minEntry.pack( side = BOTTOM)
        minFrame.pack( side = LEFT )

        maxFrame = Frame(entriesMainFrame)
        maxLabel = Label(maxFrame, text="max")
        self.maxEntry = Entry(maxFrame, textvariable=StringVar(), width=5)
        self.maxEntry.insert(0,self.ma.getMax())
        maxLabel.pack()
        self.maxEntry.pack( side = BOTTOM )
        maxFrame.pack( side = LEFT )

        periodFrame = Frame(entriesMainFrame)
        periodLabel = Label(periodFrame, text="period")
        self.periodEntry = Entry(periodFrame, textvariable=StringVar(), width=5)
        self.periodEntry.insert(0,self.ma.getPeriod())
        periodLabel.pack()
        self.periodEntry.pack( side = BOTTOM )
        periodFrame.pack( side = LEFT )

        roundToFrame = Frame(entriesMainFrame)
        roundToLabel = Label(roundToFrame, text="roundTo")
        self.roundToEntry = Entry(roundToFrame, textvariable=StringVar(), width=5)
        self.roundToEntry.insert(0,self.ma.getRoundTo())
        roundToLabel.pack()
        self.roundToEntry.pack( side = BOTTOM )
        roundToFrame.pack( side = LEFT )

        entriesMainFrame.pack()

    #middleButtons
        middleButtonsMainFrame = Frame(master)
        self.smaButton = Button(middleButtonsMainFrame, text="SimpleMovingAverge", command=lambda: self.panelDisplay(self.ma.simpleMovingAverge()))
        self.smaButton.pack( side = TOP )

        self.wmaButton = Button(middleButtonsMainFrame, text="WeightedMovingAverge", command=lambda: self.panelDisplay(self.ma.weightedMovingAverge()))
        self.wmaButton.pack( side = TOP )

        self.ewmaButton = Button(middleButtonsMainFrame, text="ExponentialMovingAverge", command=lambda: self.panelDisplay(self.ma.exponentialMovingAverge()))
        self.ewmaButton.pack( side = TOP )

        middleButtonsMainFrame.pack()


    #bottomButtons
        bottomButtonsMainFrame = Frame(master)
        self.reloadButton = Button(bottomButtonsMainFrame, text="Reload", command=self.update)
        self.reloadButton.pack( side = RIGHT )

        self.displayButton = Button(bottomButtonsMainFrame, text="Print", command=lambda: self.panelDisplay(self.ma.getTable()))
        self.displayButton.pack( side = RIGHT )

        bottomButtonsMainFrame.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack( side = RIGHT )

    def cmdDisplay(self, string):
        print(string)

    def panelDisplay(self, string):
        self.message.set(str(string))

    def update(self):
        self.ma.changeTabSize(int(self.tabSizeEntry.get()))
        self.ma.changeMin(int(self.minEntry.get()))
        self.ma.changeMax(int(self.maxEntry.get()))
        self.ma.changePeriod(int(self.periodEntry.get()))
        self.ma.changeRoundTo(int(self.roundToEntry.get()))
        self.ma.reload()


class movingAverage:
    tab=[]
    tabSize=10
    min=0
    max=10                        #import sys;sys.maxsize=9223372036854775807
    period=3
    roundTo=2
    def __init__(self):
        self.reload()

    def reload(self):
        self.tab=[]
        for _ in range(0,self.tabSize):
            self.tab.append(randint(self.min,self.max))

    def getTable(self):
        return self.tab

    def changeMin(self, min):
        self.min=min

    def getMin(self):
        return self.min

    def changeMax(self, max):
        self.max=max

    def getMax(self):
        return self.max

    def changeTabSize(self, tabSize):
        self.tabSize=tabSize

    def getTabSize(self):
        return self.tabSize

    def changePeriod(self, period):
        self.period=period

    def getPeriod(self):
        return self.period

    def changeRoundTo(self, roundTo):
        self.roundTo=roundTo

    def getRoundTo(self):
        return self.roundTo

    def simpleMovingAverge(self):
        string=''
        list=[]
        string+="Period is {}".format(self.period)
        for newElement in self.tab:
            if len(list) == self.period:
                list.pop(0)
            list.append(newElement)
            sum=0

            for element in list:
                sum+=element
            result=sum/len(list)
            result=round(result,self.roundTo)
            string+="\nadded {}, SMA={}".format(newElement,result)
        return string

    def weightedMovingAverge(self):
        string=''
        list=[]
        div=0
        string+="Period is {}".format(self.period)
        for newElement in self.tab:
            if len(list) == self.period:
                list.pop(0)
            list.append(newElement)
            sum=0

            div=0
            i=1
            for element in list:
                sum+=element*(i)
                div+=i
                i+=1
            result=sum/div
            result=round(result,self.roundTo)
            string+="\nadded {}, WMA={}".format(newElement,result)
        return string

    def exponentialMovingAverge(self):
        string=''
        alfa=2/(self.period+1)
        list=[]
        div=0
        string+="Period is {}".format(self.period)
        for newElement in self.tab:
            if len(list) == self.period:
                list.pop(0)
            list.append(newElement)
            sum=0

            div=0
            i=0
            for element in reversed(list):
                sum+=element*self.__pow((1-alfa),i)
                div+=self.__pow((1-alfa),i)
                i+=1
            result = sum / div
            result = round(result, self.roundTo)
            string+="\nadded {}, EWMA={}".format(newElement, result)
        return string

    def __pow(self, var,index):
        if index == 0:
            return 1
        result = var
        i=1
        while index > i:
            result*=var
            i+=1
        return result



if __name__ == '__main__':
    root = Tk()
    my_gui = MyFirstGUI(root)
    root.mainloop()