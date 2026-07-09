import operator

from controllers.search_employee_skills_controller import SearchEmployeeSkillsController
from menus.search_employee_skills_menu import SearchEmployeeSkillsMenu as sesm

ctrl = SearchEmployeeSkillsController()
ctrl.set_employees()
sesm.display_list(ctrl.employees)

filter = [{"id": 1, "op":operator.ge, "lvl":2}, {"id": 7, "op":operator.ge, "lvl":2}]
ctrl.filter = filter
sesm.display_filtered_list(ctrl.employees, ctrl.filter) 
