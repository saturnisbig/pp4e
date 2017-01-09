#!/usr/bin/env python
# -*- coding: utf-8 -*-

from person import Person


class Manager(Person):

    def __init__(self, name, age, pay):
        #super(Person).__init__(name, age, pay, 'manager')
        Person.__init__(self, name, age, pay, 'manager')

    def give_raise(self, percent, bonus=0.1):
        Person.give_raise(self, percent+bonus)
        #self.pay *= (1.0 + percent + bonus)


if __name__ == "__main__":
    tom = Manager(name='Tom Doe', age=50, pay=50000)
    print tom.last_name(), tom.pay
    tom.give_raise(0.20)
    print tom.pay
    print tom.job
