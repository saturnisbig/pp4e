#!/usr/bin/env python
# -*- coding: utf-8 -*-

from person import Person


class Manager(Person):

    def give_raise(self, percent, bonus=0.1):
        self.pay *= (1.0 + percent + bonus)


if __name__ == "__main__":
    tom = Manager(name='Tom Doe', age=50, pay=50000)
    print tom.last_name(), tom.pay
    tom.give_raise(0.20)
    print tom.pay
