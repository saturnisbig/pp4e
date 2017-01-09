#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Person:

    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay *= (1.0 + percent)

    def __str__(self):
        return '<%s => %s, %s, %s>' % (self.__class__.__name__, self.name,
                                       self.pay, self.job)

class Manager(Person):

    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, 'manager')

    def give_raise(self, percent, bonus=.10):
        Person.give_raise(self, percent + bonus)


if __name__ == "__main__":
    bob = Person('Bob Smith', 41)
    sue = Person('Sue Jones', 42, 40000, 'hardware')
    tom = Manager('Tom Doe', 45, 50000)

    print sue, sue.pay, sue.last_name()

    for obj in (bob, sue, tom):
        obj.give_raise(.10)
        print obj
