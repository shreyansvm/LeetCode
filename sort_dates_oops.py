import math
import os
import random
import re
import sys

class MyDates(object):
    """
    Maintains day, month and year for each valid date
    """
    def __init__(self):
        self.is_valid_date = False
        self.year = None
        self.month = None
        self.day = None

    def get_day(self):
        return self.day

    def get_month(self):
        return self.month

    def get_year(self):
        return self.year

    def verify_if_its_date(self, date):
        """
        :param date: takes each date string and checks if its valid.
                     if yes, then stores the day, month, year values
        :return: None
        """
        date_split = date.split(' ')
        try:
            if date_split[0]:
                if int(date_split[0]) >= 0 and int(date_split[0]) <= 31:
                    self.day = date_split[0]
        except IndexError:
            print('Error - dd doesnt exists in : ', date)
        try:
            if date_split[1]:
                self.month = date_split[1]
        except IndexError:
            print('Error - mm doesnt exists in : ', date)
        try:
            if date_split[2]:
                self.year = int(int(date_split[2]))
        except IndexError:
            print('Error - yyyy doesnt exists in : ', date)

        if self.day is not None \
            and self.month is not None \
            and self.year is not None:
            print('Valid date')
            self.is_valid_date = True
        else:
            self.is_valid_date = False


def construct_return_list(date_objs):
    """
    :param date_objs: takes a list of MyDates objects
    :return: contruct the return list using each object's day, month, year values
    """
    return_list = []
    for each_date_obj in date_objs:
        # print('construct_return_list: date : {}'.format(each_date_obj))
        # print('construct_return_list: date : {} {} {}'.format(each_date_obj.get_day(), each_date_obj.get_month(), each_date_obj.get_year()))
        temp_date = str(each_date_obj.get_day()) + ' ' + each_date_obj.get_month() + ' ' + str(each_date_obj.get_year())
        return_list.append(temp_date)
    return return_list


def sortDates(dates):
    """
    returns an array of date strings sorted chronologically
    """
    result = []
    date_obj_list = []
    dates_sorted_per_year = []
    for date in dates:
        if date is not None:
            dobj = MyDates()
            dobj.verify_if_its_date(date)
            print(' ````````````` ')
            if dobj.is_valid_date is True:
                print('date : {} {} {}'.format(dobj.day, dobj.month, dobj.year))
                date_obj_list.append(dobj)

    print(' ````````````` ')
    print(date_obj_list)
    print(' ````````````` ')

    # Sorting date_obj_list as per year
    #   reverse=True would sort it in descending order of the year
    dates_sorted_per_year = sorted(date_obj_list, key=lambda dobj: dobj.year, reverse=False)
    print(dates_sorted_per_year)
    print(' ````````````` ')

    result = construct_return_list(dates_sorted_per_year)
    print(result)
    return result


# sortDates(['01 March 2017', '03 Feb 2017', '15 Jan 1998'])
sortDates(['10', '20 Oct 2052', '06 Jun 1933', '26 May 1960'])
# sortDates(['01 Mar 2017', '03 Feb 2017', '15 Jan 1998', '01 Feb 2017'])