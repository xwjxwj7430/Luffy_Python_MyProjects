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

登陆后输入规定语法的命令即可进行操作。
![登陆](Luffy_Python_MyProjects/Day 21 20190205/Module 2 Chapter 1 Homework/1.打开.png)
1.查：
语法为 find 关键词 from 数据文件 where 查找条件，例子如下：

find name,age from staff_table where age > 22
find * from staff_table where dept = "IT"
find * from staff_table where enroll_data like "2013"

关键词有staff_id,name,age,phone,dept,enroll_date共6个
数据文件为staff_table
查找条件可以为><=和like，其中：
  大于小于号仅限于staff_id和age的比较
  like仅用于enroll_date查找年份
  等于号可用于除enroll_date以外的条件
 



程序的启动方式、登录用户信息、程序的运行效果
