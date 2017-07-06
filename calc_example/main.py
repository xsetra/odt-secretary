# -*- coding: utf-8 -*-


import sys
from secretary import Renderer


class Person:
	def __init__(self, name, surname, country):
		self.name = name
		self.surname = surname
		self.country = country

template_file_name = sys.argv[1]

datas = [ [10,20,30,40,50,60], [70,80,90] ]


engine = Renderer()
result = engine.render(template_file_name, subeler=datas)

output = open("rendered_calc.ods", "wb")
output.write(result)

