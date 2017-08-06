#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exercise 36: Birthday Plots

This exercise is Part 4 of 4 of the birthday data exercise series. The
other exercises are: Part 1, Part 2, and Part 3.

In the previous exercise we counted how many birthdays there are in each
month in our dictionary of birthdays.

In this exercise, use the bokeh Python library to plot a histogram of
which months the scientists have birthdays in! Because it would take a
long time for you to input the months of various scientists, you can use
my scientist birthday JSON file. Just parse out the months (if you don’t
know how, I suggest looking at the previous exercise or its solution)
and draw your histogram.

If you are using a purely web-based interface for coding, this exercise
won’t work for you, since it requires installing the bokeh Python
package. Now might be a good time to install Python on your own computer.
"""


from bokeh.plotting import figure, show, output_file
from datetime import date
import json
import requests


def get_text_web(url):
    return json.loads(requests.get(url).text)


def read_from_file(filename):
    with open(filename, "r") as a_file:
        text = json.load(a_file)
    return text


def get_month_name(text_date):
    year, month, day = text_date.split("-")
    obj_date = date(int(year), int(month), int(day))
    month_name = obj_date.strftime("%B"), int(month)
    return month_name


def count_months(persons, months: dict) -> dict:
    for name, birthday in persons.items():
        month_name = get_month_name(birthday)
        months[month_name[0]] = \
            months.get(month_name[0], (0, 0))[0] + 1, month_name[1] - 1
    return months


def get_axis_ordered(data: dict) -> tuple:

    x_list, y_list = list(range(12)), list(range(12))

    for x, y in data.items():
        x_list[y[1]] = x
        y_list[y[1]] = y[0]
    return x_list, y_list


def make_plot(x, y, file_plot):

    output_file(file_plot)

    p = figure(plot_width=1200, plot_height=800, title="Birthday Plots",
               x_range=x,)

    # Set Title, Background and Border
    p.title.text_color = "firebrick"
    p.title.text_font = "arial"
    p.title.text_font_style = "bold"
    p.background_fill_color = "green"
    p.background_fill_alpha = 0.50
    p.border_fill_color = "whitesmoke"
    p.min_border_left = 50

    # Set X Axes
    p.xaxis.axis_label = "Months"
    p.xaxis.axis_label_text_color = "firebrick"
    p.xaxis.axis_label_standoff = 15
    p.xaxis.axis_line_width = 3
    p.xaxis.axis_label_text_font_style = "bold"

    # Set Y Axes
    p.yaxis.axis_label = "Occurences"
    p.yaxis.axis_label_text_color = "firebrick"
    p.yaxis.axis_label_standoff = 15
    p.yaxis.axis_line_width = 3
    p.yaxis.axis_label_text_font_style = "bold"

    # Set Lines
    p.xgrid.grid_line_color = None
    p.ygrid.grid_line_color = "black"
    p.ygrid.grid_line_alpha = 0.5
    p.ygrid.grid_line_dash = [6, 4]

    # Set Legend
    p.legend.location = "top_right"
    p.legend.label_text_font = "arial"

    p.vbar(x=x, top=y, width=0.75, color="firebrick")

    return p


if __name__ == "__main__":

    filename = "random_persons.json"
    file_plot = "bokeh_plots/plot.html"
    url = "https://goo.gl/EQZpaE"

    x, y = get_axis_ordered(count_months(get_text_web(url), dict()))
    show(make_plot(x, y, file_plot))
