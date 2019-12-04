import new_printing_models
unprinted_designs = []
#客户输入设计
order = True
while order:
	design = input("\nPlease enter you want print design " +
		"\n(if you don't want print please enter 'q') : ")
	if design == 'q':
		order = False
	else:
		unprinted_designs.append(design)
print(unprinted_designs)

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
