import kim

from printing_function import *

unprinted_designs = []
completed_models = []
#客户输入设计
order = True
while order:
	design = input("\nPlease enter you want print design " +
		"\n(if you don't want print anything please enter 'q') : ")
	if design == 'q':
		order = False
	else:
		unprinted_designs.append(design.title())
print(unprinted_designs)

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print("order is " + str(unprinted_designs))
print("have been ptinted is " + str(completed_models))