#!/usr/bin/python

#input =raw_input("|" + "input: ".center(78) + "|")

class MyMenu:
    count=0

    def __init__(self, name="TUI Menu", c="+", h="-", v="|", hs="=", width=78):
        self.list_option = []
        self.name = name
        self.c = c
        self.h = h
        self.v = v
        self.hs = hs
        self.width = width


        MyMenu.count += 1

    def add(self, option):
        self.list_option.append(option)
#        print ("Option: "+option+" - added to menu")

    def display(self):
        option_count = 1
        print self.c + self.name.ljust(self.width, self.h) + self.c
        print self.c + self.hs * self.width + self.c
        print self.v + "Options".center(self.width) + self.v
        print self.c + self.hs * self.width + self.c
        for l in self.list_option:
            l = str(option_count) + " - " + l
            print self.v + l.center(self.width) + self.v
            option_count +=1
        for i in range(1, 7):
            print self.v + " " * self.width + self.v
        print self.c + "-" * self.width + self.c


# Test sample object
menu=MyMenu(name="My sample menu 1")
menu.add("Option 1")
menu.add("Option 2")

menu1=MyMenu(name="My sample menu 2", hs="#")
menu1.add("additional Option 1")
menu1.add("additional Option 2")
menu1.add("additional Option 3")

menu.display()
menu1.display()

menu3=MyMenu(width=100)
menu3.display()

