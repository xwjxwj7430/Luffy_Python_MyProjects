开发环境： Python 3.7.2

数据：staff_table，数据结构如下：

staff_id,name,age,phone,dept,enroll_date

1,Alex Li,22,13651054608,IT,2013-04-01

2,Jack Wang,28,13451024608,HR,2015-01-07

3,Rain Wang,21,13451054608,IT,2017-04-01

4,Mack Qiao,44,15653354208,Sales,2016-02-01

5,Rachel Chen,23,13351024606,IT,2013-03-16

6,Eric Liu,19,18531054602,Marketing,2012-12-01

7,Chao Zhang,21,13235324334,Administration,2011-08-08

8,Kevin Chen,22,13151054603,Sales,2013-04-01

9,Shit Wen,20,13351024602,IT,2017-07-03

10,Shanshan Du,26,13698424612,Operation,2017-07-02

程序的实现的功能:

对员工信息表的增删改查：


登陆后输入规定语法的命令即可进行操作,语法输入时注意空格和标点符号。

![登陆](https://github.com/xwjxwj7430/Luffy_Python_MyProjects/blob/master/Day%2021%2020190205/Module%202%20Chapter%201%20Homework/1.%E6%89%93%E5%BC%80.png)



1.查：

语法为 find 关键词 from 数据文件 where 查找条件，例子如下：


find name,age from staff_table where age > 22

find * from staff_table where dept = "IT"

find * from staff_table where enroll_data like "2013"

![查](https://github.com/xwjxwj7430/Luffy_Python_MyProjects/blob/master/Day%2021%2020190205/Module%202%20Chapter%201%20Homework/2.%E6%9F%A5.png)

关键词有staff_id,name,age,phone,dept,enroll_date共6个

数据文件为staff_table

查找条件可以为><=和like，其中：

  大于小于号仅限于staff_id和age的比较
  
  like仅用于enroll_date查找年份
  
  等于号可用于除enroll_date以外的条件
  
  
  
 
2 添加员工信息：

语法为 add 数据文件 姓名，年龄，手机号，部门，入职日期 ，若干信息必须具备，缺一不可，其中手机号为唯一标识，不能重复，例子如下：

add staff_table Mosson Li,18,13678789527,IT,2018-12-11

![增](https://github.com/xwjxwj7430/Luffy_Python_MyProjects/blob/master/Day%2021%2020190205/Module%202%20Chapter%201%20Homework/3.%E5%8A%A0.png)




3 删除员工信息，根据员工id即staff_id:

语法为 del from 数据文件 where id = 数字

>>>:del from staff_table where id = 10

![删](https://github.com/xwjxwj7430/Luffy_Python_MyProjects/blob/master/Day%2021%2020190205/Module%202%20Chapter%201%20Homework/4.%E5%88%A0.png)

删除后，剩下的id会自动更新




4 修改员工信息，可根据特殊条件修改员工信息：

语法为 update 数据文件 set 要修改的关键字 = "修改后的内容" where 筛查的关键字 = "筛查内容"

demo 1

>>>:update staff_table set dept="Market" where dept = "IT"

将staff_table中dept为IT的修改成dept为Market

demo 2

>>>:update staff_table set age=25 where name = "Alex Li"

将staff_table中姓名为Alex Li的用户的年龄改成25


![改](https://github.com/xwjxwj7430/Luffy_Python_MyProjects/tree/master/Day%2021%2020190205/Module%202%20Chapter%201%20Homework)




5. 退出请输"q"
![退](https://github.com/xwjxwj7430/Luffy_Python_MyProjects/blob/master/Day%2021%2020190205/Module%202%20Chapter%201%20Homework/6.%E9%80%80%E5%87%BA.png)
