# -*- coding: utf-8 -*-


from budget import Budget
import sys
import datetime
from secretary import Renderer
import copy
import random


now = datetime.datetime.now()

template_file = sys.argv[1]
engine = Renderer()

project_number = 511
project_title = "Test Başlık"
project_executer = "Xsetra"
project_budget = "145.000,00"
sign_date = "{0:02d}/{1:02d}/{2:4d}".format(now.day, now.month, now.year)

budgets = []
b1 = Budget(2017, "tur 1", "gerekce 1", random.randint(1,10), random.randint(100, 1000))
b2 = Budget(2017, "tur 2", "gerekce 2", random.randint(1,10), random.randint(100, 1000))
b3 = Budget(2017, "tur 3", "gerekce 3", random.randint(1,10), random.randint(100, 1000))

budgets.append(b1)
budgets.append(b2)
budgets.append(b3)

print ("Test ok")

result = engine.render(template_file,
		       project_number=project_number,
		       project_title=project_title,
		       project_executer=project_executer,
		       project_budget=project_budget,
		       sign_date=sign_date,
		       budgets=budgets)


output_file = open("rendered_document.odt", "wb")
output_file.write(result)
