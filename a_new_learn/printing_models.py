from printing_function import *
#创建一个要打印的列表
unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []

#模拟打印每个设计，直到没有未打印的设计为止
#参考p111在列表之间移动元素
while unprinted_designs:
	current_design = unprinted_designs.pop()

	#模拟根据设计制作3D打印的过程
	print("printing model: " + current_design)
	completed_models.append(current_design)
#显示打印好的模型
print("\nThe following models have been printed: ")
for completed_model in completed_models:
	print(completed_model)