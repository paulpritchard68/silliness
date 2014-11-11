#! /usr/bin/python
""" XKComplete: A date reversing completeness counter inspired by XKCD
http://xkcd.com/1017/

Copyright (C) 2012 Paul Pritchard

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>."""

from __future__ import division
import datetime
import math

def xkcdate(percentage_complete):
    """ Returns the percetange completed, either as a date or a year"""
    today = datetime.date.today()
    completion = percentage_complete / 100
    days = float(365.25 * (math.exp(3+20.3444*(completion)**3) - math.exp(3)))
    try:
        date = (today - datetime.timedelta(days)).strftime("%A, %d %B %Y")
    except:
        dateval = datetime.datetime.today().year - int(days / 365.25)
        if dateval < 0:
            dateval = 0 - dateval
            adbc = " BC"
        else:
            adbc = " AD"
        date = str(dateval) + adbc

    return date

if __name__ == "__main__":
    percentage_complete = 0
    while percentage_complete < 100:
        percentage_complete = input("Enter percentage complete: ")
        print xkcdate(percentage_complete)
