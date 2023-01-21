"""
项目名称：学生管理系统
作者:觅食
创作日期: 2023年1月21日
使用文档参考：Python学生管理系统.docx
"""

print("*"*10+"学生管理系统"+"*"*10)

# 创建存储学生信息的列表
student_list = []


while True:

    # 输入数字,选择对应功能
    print("1.添加学生\n"
          "2.删除学生\n"
          "3.修改学生\n"
          "4.查询学生\n"
          "5.退出系统")


    # 利用function接受输入的数字
    function = input("请输入数字选择功能:")

    # 添加学生信息
    def add():
        students = input("请输入添加学生姓名:")
        # 利用append进行添加学生信息
        student_list.append(students)
        print("-"*30)


    # 删除学生信息
    def delete():
        students = input("请输入需要删除的学生姓名")
        # remove删除对应学生的姓名
        student_list.remove(students)
        print("-" * 30)

    # 修改学生信息
    def Modify():
        students = input("请输入需要修改的学生姓名")
        # students_modified修改后的学生姓名
        students_modified = input("请输入修改后学生姓名")
        # 返回学生姓名对应的索引位置
        a = student_list.index(students)
        # 利用索引位置进行修改
        student_list[a] = students_modified
        print("-" * 30)


    # 查询学生信息
    def query():
        students = input("请输入需要查询的学生姓名")
        # 将学生的列表遍历
        for i in student_list:
            # 如果列表中有跟查询的是相同的,则表示存在
            if students == i:
                print("学生信息存在")
            # 如果列表中没有相同的,则表示不存在
            elif students != i:
                print("学生信息不存在")
        print("-" * 30)

    # 退出系统
    def exits():
        exit()


    # 与输入的数字进行对比,调用相关的函数
    if function == '1':
        # 添加学生信息
        add()
    elif function == '2':
        # 删除学生信息
        delete()
    elif function == '3':
        # 修改学生信息
        Modify()
    elif function == '4':
        # 查询学习信息
        query()
    elif function == '5':
        # 退出系统
        exits()
    else:
        print("输入错误,请重新输入")

