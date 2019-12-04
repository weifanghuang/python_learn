def show_magicians(printed_names):
    for printed_name in printed_names:
        print(str(printed_name).title())

def make_great(changed_lists):
    for i in range(4):
        changed_lists[i] = 'the Great ' + changed_lists[i]
    return changed_lists

magicians = ['job', 'jane', 'stand', 'smile']
make_great(magicians)
show_magicians(magicians)
#————————————————
#版权声明：本文为CSDN博主「幸福慢慢来丶」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
#原文链接：https://blog.csdn.net/qq_38835602/article/details/78843
