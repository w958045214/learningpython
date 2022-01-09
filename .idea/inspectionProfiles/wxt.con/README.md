python 学习练习



# 20210223

### 你当前使用的大数据平台是什么？以及你了解到的大数据平台有哪些？

华为FI，腾讯DBS，cdh，微医 DP，阿里 maxcompute，HDP TDH CDP（cdh+HDP）



### 大数据平台简介：

开源hadoop--几乎没有产品化，完全靠自己搭建

CDH/HDP/FI/TW-解决组件之间的版本兼容、集群自动化安装、管理等功能，产品化中等

公有云-阿里云   产品化程度较高，一站式开发平台

公有云-网易云   产品化程度较高，一站式开发平台

云端产品的私有化部署-阿里MaxComputer私有化部署等

仅提供大致方向，想知道详情，请移步各大搜索引擎



# 20210224

### 你当前选择的大数据方向？以及你了解到可以发展的热门方向有哪些？

ETL，BI,数仓，数据分析（量化分析)，数据推广，数据挖掘，视觉，机器学习，AI，数据科学





# 20210301(python)

群规定:

上班时间（9:00-18:00）只能聊技术相关，下班时间可以闲聊，拒绝黄赌毒，拒绝发无关链接

主题规划:

主题规划->python->clickhouse->sql(hivesql)为主->数仓->spark->flink->HADOOP->用户画像->推荐系统->数据结构与算法->机器学习->有异议请接龙

今日主题 

python基础教程1

执行Python程序





## introduduction

### 特点

1.Python 是一种解释型语言：没有编译环节

2.交互式 >>>

3.面向对象

### 环境搭建

[传送门](https://www.python.org/downloads/release/python-377/)





### 中文编码





解决方法为只要在文件开头加入 # -- coding: UTF-8 -- 或者 # coding=utf-8 就行了，= 号两边不要空格。

file > Settings>encoding>Editor > File encodings,将 IDE Encoding 和 Project Encoding 设置为utf-8。

### 交互式编程

linux上你只需要在命令行中输入 Python 命令即可，就会出现>>>

### 标识符

1.可以包括英文、数字以及下划线(_)，但不能以数字开头。

2.区分大小写

3.下划线开头的标识符是有特殊意义的，









4.可以同一行显示多条语句，方法是用分号 ; 分开

### 保留字符

所有 Python 的关键字只包含小写字母。

![img](https://docimg4.docs.qq.com/image/RQ3lxDCf0jhBRUUpVKMTNQ?w=754&h=430)

### 缩进

缩进的空白数量是可变的，但是所有代码块语句必须包含相同的缩进空白数量，这个必须严格执行。





在 Python 的代码块中必须使用相同数目的行首缩进空格数。

### 多行语句

一般以新行作为语句的结束符。

但可以使用斜杠（ \）将一行的语句分为多行显示。





语句中包含 [], {} 或 () 括号就不需要使用多行连接符。





### 引号

引号( ’ )、双引号( " )、三引号( ‘’’ 或 “”" ) 来表示字符串，引号的开始与结束必须是相同类型的。

三引号可以由多行组成，编写多行文本的快捷语法，常用于文档字符串，在文件的特定地点，被当做注释。





### 注释

#### 1.单行注释

位置在句首





位置可以在句末





注释位置开始到后面都是注释

#### 2.多行注释

使用三个单引号(’’’)或三个双引号(""")。





### 空行

空行是程序代码的一部分。

空行与代码缩进不同，空行并不是Python语法的一部分。但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。

### print 输出

print 默认输出是换行的，如果要实现不换行需要在变量末尾加上逗号 ,





执行结果为：





### 代码块和子句

缩进相同的一组语句构成一个代码块，我们称之代码组。

像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。

我们将首行及后面的代码组称为一个子句(clause)。





### 参数帮助信息

可以使用 -h 参数查看各参数帮助信息：





### 变量类型

## 变量赋值

等号 = 运算符左边是一个变量名，等号 = 运算符右边是存储在变量中的值

### 单变量赋值





### 多变量赋值

多个变量赋一个相同的值





多个变量赋不同的值





## 标准数据类型

- Numbers(数字）
- String（字符串）
- List （列表）
- Tuple(元组）
- Dictionary（字典）

## 数字

![img](https://docimg3.docs.qq.com/image/aYQvqxiYPAtPg7TinlZgNg?w=695&h=499)

当你指定一个值时，Number 对象就会被创建：





Python支持四种不同的数字类型：

- int（有符号整型）
- long（长整型[也可以代表八进制和十六进制]）
- float（浮点型）
- complex（复数）

![img](https://docimg6.docs.qq.com/image/1xNKVXLyCJ9PaITIS-gYUw?w=736&h=190)

*Python使用 L 来显示长整型。（小写也行，但不建议！）

*支持复数，复数由实数部分和虚数部分构成，可以用 a + bj,或者 complex(a,b) 表示， 复数的实部 a 和虚部 b 都是浮点型。

## 字符串

![img](https://docimg7.docs.qq.com/image/fnnyHtOAzbrqshpUNHgs5Q?w=635&h=472)由数字、字母、下划线组成的一串字符。

### 取值顺序

python的字串列表有2种取值顺序:

从左到右索引默认0开始的，最大范围是字符串长度少1

从右到左索引默认-1开始的，最大范围是字符串开头

![img](https://docimg1.docs.qq.com/image/VbNFdwznP01mY3Fqe9D8Fg?w=318&h=183)

### 截取字符串

要实现从字符串中获取一段子字符串的话，可以使用 [头下标:尾下标]

（包含头下标的字符，但不包含尾下标的字符。）来截取相应的字符串，其中下标是从 0 开始算起，可以是正数或负数，下标可以为空表示取到头或尾。

### + 与 *

加号（+）是字符串连接运算符，星号（*）是重复操作





## 列表[ ]

![img](https://docimg7.docs.qq.com/image/4L9m-mQYRemZ3P92T8nfIg?w=651&h=484)支持字符，数字，字符串甚至可以包含列表（即嵌套）。

### 取值顺序

从左到右索引默认 0 开始

从右到左索引默认 -1 开始，下标可以为空表示取到头或尾。

### 切割

列表中值的切割也可以用到变量 [头下标:尾下标]

### + 与 *

加号 + 是列表连接运算符，星号 * 是重复操作

## 元组（）

![img](https://docimg1.docs.qq.com/image/Up0Qf2b-Aj-8DT_TWVr8Ww?w=698&h=518)元组用 () 标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。

### 取值顺序

从左到右索引默认 0 开始

从右到左索引默认 -1 开始，下标可以为空表示取到头或尾。

### 切割

列表中值的切割也可以用到变量 [头下标:尾下标]

### + 与 *

加号 + 是列表连接运算符，星号 * 是重复操作

## 字典{}

![img](https://docimg9.docs.qq.com/image/Xjso212HsoxxC5zeqok4LQ?w=718&h=513)字典当中的元素是通过键来存取的，而不是通过偏移存取。

字典由索引(key)和它对应的值value组成。









## 数据类型转换

![img](https://docimg8.docs.qq.com/image/KL2USVNsBTClr6Dp0wa72A?w=755&h=744)删除

通过使用del语句删除单个或多个对象的引用





## 运算符

Python语言支持以下类型的运算符:

### 算术运算符

![img](https://docimg6.docs.qq.com/image/UhmNEC1a2IvjEs65X5NhnA?w=736&h=413)

### 比较（关系）运算符

![img](https://docimg6.docs.qq.com/image/t1lY5iyH2_F5LGp_7bf5Yw?w=740&h=373)

### 赋值运算符

![img](https://docimg7.docs.qq.com/image/wDtQ32D0wuGRGZK6FO0DAQ?w=584&h=387)

### 位运算符

![img](https://docimg9.docs.qq.com/image/6qpv9W_aHnSg0Y1bdkXe6Q?w=742&h=423)

### 逻辑运算符

![img](https://docimg10.docs.qq.com/image/22s_4AATVfjCo7WVGSHFjg?w=737&h=155)

### 成员运算符

![img](https://docimg9.docs.qq.com/image/C6NHuw4oZhSEW-royDTi8w?w=742&h=111)

### 身份运算符

![img](https://docimg1.docs.qq.com/image/1dSedNtKA5EbXlLaIJATSg?w=746&h=189)

### 运算符优先级

![img](https://docimg1.docs.qq.com/image/56cTVzFFSoPnRoV6YXmybw?w=735&h=591)

## 条件语句

if 语句用于控制程序的执行，基本形式为：



当判断条件为多个值时，可以使用以下形式：



不支持 switch 语句，所以多个条件判断，只能用 elif 来实现，如果判断需要多个条件需同时判断时，可以使用 or （或），表示两个条件有一个成立时判断条件成功；使用 and （与）时，表示只有两个条件同时成立的情况下，判断条件才成功。

同一行的位置上使用if条件判断语句，如下实例：



# 20210302(python)

## 循环

### for 循环





### while 循环





### 嵌套循环

#### for 循环嵌套语法：





#### while 循环嵌套语法：





### 循环控制语句

![img](https://docimg6.docs.qq.com/image/GF_ai431G7IPrh85_l2m-A?w=664&h=153)





结果：

![img](https://docimg1.docs.qq.com/image/60CqvHo_lxD5uUWmT21yRg?w=248&h=190)

pass 不做任何事情，一般用做占位语句。该处的 pass 便是占据一个位置，因为如果定义一个空函数程序会报错，当你没有想好函数的内容是可以用 pass 填充，使程序可以正常运行。

## Number

### math 模块、cmath 模块

区别是 cmath 模块运算的是复数，math 模块运算的是数学运算。

导入：



![img](https://docimg7.docs.qq.com/image/wSa20fFCag0A9MWPPMJzfQ?w=744&h=209)

### 数学函数

![img](https://docimg5.docs.qq.com/image/71LYh_paMoQ2TgVJmGrE4g?w=748&h=613)

### 随机数函数

![img](https://docimg3.docs.qq.com/image/9AmDqa4kIBBOKKaWl2AtNw?w=745&h=371)

### 三角函数

![img](https://docimg10.docs.qq.com/image/Efhvsv-YyNzal04dc_KeJQ?w=523&h=444)

### 数学常量

![img](https://docimg1.docs.qq.com/image/UewdMKQThT9zHNT-9x53XA?w=384&h=120)

## 字符串

单引号和双引号均可



### 转义字符

![img](https://docimg4.docs.qq.com/image/kuxNd-ro-KSFJrYFlcAkwA?w=544&h=681)

### 字符串运算符

![img](https://docimg5.docs.qq.com/image/8Hmcft2YHeglvWhW2Iwj3A?w=743&h=599)

### 字符串格式化

将一个值插入到一个有字符串格式符 %s 的字符串中。



结果：My name is Zara and weight is 21 kg!

### 字符串格式化符号

![img](https://docimg6.docs.qq.com/image/V72cAWwRzjMrU-eL2NWKaw?w=410&h=565)

### 格式化操作符辅助指令:

![img](https://docimg3.docs.qq.com/image/mpJYjqrS8NA3kY8IuWtFmA?w=553&h=427)

### 三引号

1.将复杂的字符串进行赋值。？？？

2.允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符。

3.典型的用例是，引用HTML或者SQL

### Unicode 字符串

引号前小写的"u"表示这里创建的是一个 Unicode 字符串。



### 字符串内建函数

#### string.capitalize()

把字符串的第一个字符大写

#### string.center(width)

返回一个原字符串居中,并使用空格填充至长度 width 的新字符串

#### string.count(str, beg=0, end=len(string))

返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数

#### string.decode(encoding=‘UTF-8’, errors=‘strict’)

以 encoding 指定的编码格式解码 string，如果出错默认报一个 ValueError 的 异 常 ， 除非 errors 指 定 的 是 ‘ignore’ 或 者’replace’

#### string.encode(encoding=‘UTF-8’, errors=‘strict’)

以 encoding 指定的编码格式解码 string，如果出错默认报一个 ValueError 的 异 常 ， 除非 errors 指 定 的 是 ‘ignore’ 或 者’replace’

#### string.endswith(obj, beg=0, end=len(string))

检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.

#### string.expandtabs(tabsize=8)

把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8。

#### string.find(str, beg=0, end=len(string))

检测 str 是否包含在 string 中，如果 beg 和 end 指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回-1

#### string.index(str, beg=0, end=len(string))

跟find()方法一样，只不过如果str不在 string中会报一个异常.

#### string.format()

格式化字符串

#### string.isalnum()

如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False

#### string.isalpha()

如果 string 至少有一个字符并且所有字符都是字母则返回 True,否则返回 False

#### string.isdecimal()

如果 string 只包含十进制数字则返回 True 否则返回 False.

#### string.isdigit()

如果 string 只包含数字则返回 True 否则返回 False.

#### string.islower()

如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False

#### string.isnumeric()

如果 string 中只包含数字字符，则返回 True，否则返回 False

#### string.isalpha()

如果 string 至少有一个字符并且所有字符都是字母则返回 True,否则返回 False

#### string.isdecimal()

如果 string 只包含十进制数字则返回 True 否则返回 False.

#### string.isdigit()

如果 string 只包含数字则返回 True 否则返回 False.

#### string.islower()

如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False

#### string.isnumeric()

如果 string 中只包含数字字符，则返回 True，否则返回 False

#### string.isspace()

如果 string 中只包含空格，则返回 True，否则返回 False.

#### string.istitle()

如果 string 是标题化的(见 title())则返回 True，否则返回 False

#### string.isupper()

如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False

#### string.join(seq)

以 string 作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串

#### string.ljust(width)

返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串

#### string.lower()

转换 string 中所有大写字符为小写.

#### string.lstrip()

截掉 string 左边的空格

#### string.maketrans(intab, outtab])

maketrans() 方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。

#### max(str)

返回字符串 str 中最大的字母。

#### min(str)

返回字符串 str 中最小的字母。

#### string.partition(str)

有点像 find()和 split()的结合体,从 str 出现的第一个位置起,把 字 符 串 string 分 成 一 个 3 元 素 的 元 组 (string_pre_str,str,string_post_str),如果 string 中不包含str 则 string_pre_str == string.

#### string.replace(str1, str2, num=string.count(str1))

把 string 中的 str1 替换成 str2,如果 num 指定，则替换不超过 num 次.

#### string.rfind(str, beg=0,end=len(string) )

类似于 find() 函数，返回字符串最后一次出现的位置，如果没有匹配项则返回 -1。

#### string.rindex( str, beg=0,end=len(string))

类似于 index()，不过是从右边开始.

#### string.rjust(width)

返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串

#### string.rpartition(str)

类似于 partition()函数,不过是从右边开始查找

#### string.rstrip()

删除 string 字符串末尾的空格.

#### string.split(str="", num=string.count(str))

以 str 为分隔符切片 string，如果 num 有指定值，则仅分隔 num+ 个子字符串

#### string.splitlines([keepends])

按照行(’\r’, ‘\r\n’, \n’)分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。

#### string.startswith(obj, beg=0,end=len(string))

检查字符串是否是以 obj 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查.

#### string.strip([obj])

在 string 上执行 lstrip()和 rstrip()

#### string.swapcase()

翻转 string 中的大小写

#### string.title()

返回"标题化"的 string,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())

#### string.translate(str, del="")

根据 str 给出的表(包含 256 个字符)转换 string 的字符,要过滤掉的字符放到 del 参数中

#### string.upper()

转换 string 中的小写字母为大写

#### string.zfill(width)

返回长度为 width 的字符串，原字符串 string 右对齐，前面填充0

# 20210303(python)

## 列表

列表索引从0开始。

### 访问列表中的值

使用下标索引来访问列表中的值，同样你也可以使用方括号的形式截取字符





### 更新

使用append()方法来添加列表项



### 删除列表元素





## 列表脚本操作符

![img](https://docimg1.docs.qq.com/image/pHuF6MibarjcC1d_jkhEJA?w=667&h=237)列表截取

![img](https://docimg4.docs.qq.com/image/O3dNqLqsAs5GawmXHvgbrA?w=728&h=150)

## 列表函数

### cmp(list1, list2)

比较两个列表的元素

### len(list)

列表元素个数

### max(list)

返回列表元素最大值

### min(list)

返回列表元素最小值

### list(seq)

将元组转换为列表

## 列表方法

### 1 list.append(obj)

在列表末尾添加新的对象

### 2 list.count(obj)

统计某个元素在列表中出现的次数

### 3 list.extend(seq)

在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）

### 4 list.index(obj)

从列表中找出某个值第一个匹配项的索引位置

### 5 list.insert(index, obj)

将对象插入列表

### 6 list.pop([index=-1])

移除列表中的一个元素（默认最后一个元素），并且返回该元素的值

### 7 list.remove(obj)

移除列表中某个值的第一个匹配项

### 8 list.reverse()

反向列表中元素

### 9 list.sort(cmp=None, key=None, reverse=False)

对原列表进行排序

## 元组（）

元组的元素不能修改。

元组中只包含一个元素时，需要在元素后面添加逗号



### 访问元组





### 修改元组

元素值是不允许修改的，但我们可以对元组进行连接组合





### 删除元组 del

值是不允许删除的，但我们可以使用del语句来删除整个元组

### 元组运算符

![img](https://docimg7.docs.qq.com/image/twZ_aOAWyUZ2BFFmr9wLdg?w=646&h=234)

### 元组索引，截取

![img](https://docimg9.docs.qq.com/image/li4Rb6TmOjUE37iYZs7rAw?w=698&h=158)

### 无关闭分隔符

任意无符号的对象，以逗号隔开，默认为元组



### 元组内置函数

#### cmp(tuple1, tuple2)

比较两个元组元素。

#### len(tuple)

计算元组元素个数。

#### max(tuple)

返回元组中元素最大值。

#### min(tuple)

返回元组中元素最小值。

#### tuple(seq)

将列表转换为元组。

## 字典(Dictionary) { }

可变容器模型，且可存储任意类型对象。





键一般是唯一的，如果重复最后的一个键值对会替换前面的，值不需要唯一。





值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。???

### 访问字典里的值

把相应的键放入熟悉的方括弧





### 修改字典

![img](https://docimg9.docs.qq.com/image/skomKzxQ4-yPVCNnjm6hcg?w=454&h=315)

### 删除字典元素





## 字典内置函数

Python字典包含了以下内置函数：

### cmp(dict1, dict2)

比较两个字典元素。

### len(dict)

计算字典元素个数，即键的总数。

### str(dict)

输出字典可打印的字符串表示。





![img](https://docimg6.docs.qq.com/image/lQP0ICkYGlOsLGCroBR1_Q?w=375&h=96)

### type(variable)

返回输入的变量类型，如果变量是字典就返回字典类型。

## 字典内置函数&方法

### dict.clear()

删除字典内所有元素

### dict.copy()

返回一个字典的浅复制





![img](https://docimg9.docs.qq.com/image/AAHt4eGSzAbAieCB-Alf-g?w=353&h=79)

### 引用和 copy 的区别

深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用





dict2 其实是 dict1 的引用（别名），所以输出结果都是一致的，dict3 父对象进行了深拷贝，不会随dict1 修改而修改，子对象是浅拷贝所以随 dict1 的修改而修改。

![img](https://docimg9.docs.qq.com/image/OjproJ2ucIOMWFwAraWdsA?w=292&h=97)

### dict.fromkeys(seq[, val])

创建一个新字典，以序列 seq 中元素做字典的键，val 为字典所有键对应的初始值

### dict.get(key, default=None)

返回指定键的值，如果值不在字典中返回default值

### dict.has_key(key)

如果键在字典dict里返回true，否则返回false

### dict.items()

以列表返回可遍历的(键, 值) 元组数组

### dict.keys()

以列表返回一个字典所有的键

### dict.setdefault(key, default=None)

和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default

### dict.update(dict2)

把字典dict2的键/值对更新到dict里

### dict.values()

以列表返回字典中的所有值

### pop(key[,default])

删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。

### popitem()

返回并删除字典中的最后一对键和值。

## 日期和时间

时间间隔是以秒为单位的浮点小数





## 时间函数

time.time()

用于获取当前时间戳。

time.localtime(time.time())

获取当前时间

time.asctime（）

取可读的时间模式

time.strftime(format[, t])

格式化日期

time.altzone（）

返回格林威治西部的夏令时地区的偏移秒数。如果该地区在格林威治东部会返回负值（如西欧，包括英国）。对夏令时启用地区才能使用。

time.asctime([tupletime])

接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14 2008"（2008年12月11日 周二18时07分14秒）的24个字符的字符串。

time.clock( )

用以浮点数计算的秒数返回当前的CPU时间。用来衡量不同程序的耗时，比time.time()更有用。

time.ctime([secs])

作用相当于asctime(localtime(secs))，未给参数相当于asctime()

time.gmtime([secs])

接收时间戳（1970纪元后经过的浮点秒数）并返回格林威治天文时间下的时间元组t。注：t.tm_isdst始终为0

time.localtime([secs])

接收时间戳（1970纪元后经过的浮点秒数）并返回当地时间下的时间元组t（t.tm_isdst可取0或1，取决于当地当时是不是夏令时）。

time.mktime(tupletime)

接受时间元组并返回时间戳（1970纪元后经过的浮点秒数）。

time.sleep(secs)

推迟调用线程的运行，secs指秒数。

9 time.strftime(fmt[,tupletime])

接收以时间元组，并返回以可读字符串表示的当地时间，格式由fmt决定。

10 time.strptime(str,fmt=’%a %b %d %H:%M:%S %Y’)

根据fmt的格式把一个时间字符串解析为时间元组。

11 time.time( )

返回当前时间的时间戳（1970纪元后经过的浮点秒数）。

12 time.tzset()

根据环境变量TZ重新初始化时间相关设置。

### 时间元组

![img](https://docimg5.docs.qq.com/image/I_4m4O81YxW1mBU-DPGHuw?w=613&h=393)

![img](https://docimg3.docs.qq.com/image/35AI0fABYw1G9UPqAbOrbA?w=629&h=435)

### 获取当前时间





![img](https://docimg9.docs.qq.com/image/oDgDVMuGX_MQuIzdQTp25A?w=726&h=107)

### 获取格式化的时间





![img](https://docimg3.docs.qq.com/image/0NAZaMvrehzj-D7_0UaGVA?w=289&h=88)

### 格式化日期





![img](https://docimg4.docs.qq.com/image/1yo94bhuvmeG9EGrwbGfgg?w=264&h=134)

### 时间日期格式化符号：





### 获取某月日历





![img](https://docimg8.docs.qq.com/image/LbO0m6G4PHA2KcX1ZIu0cw?w=192&h=182)

## 日历函数

### calendar.calendar(year,w=2,l=1,c=6)

返回一个多行字符串格式的year年年历，3个月一行，间隔距离为c。 每日宽度间隔为w字符。每行长度为21* W+18+2* C。l是每星期行数。

### calendar.firstweekday( )

返回当前每周起始日期的设置。默认情况下，首次载入 calendar 模块时返回 0，即星期一。

### calendar.isleap(year)

是闰年返回 True，否则为 False。

### calendar.leapdays(y1,y2)

返回在Y1，Y2两年之间的闰年总数。

### calendar.month(year,month,w=2,l=1)

返回一个多行字符串格式的year年month月日历，两行标题，一周一行。每日宽度间隔为w字符。每行的长度为7* w+6。l是每星期的行数。

### calendar.monthcalendar(year,month)

返回一个整数的单层嵌套列表。每个子列表装载代表一个星期的整数。Year年month月外的日期都设为0;范围内的日子都由该月第几日表示，从1开始。

### calendar.monthrange(year,month)

返回两个整数。第一个是该月的星期几的日期码，第二个是该月的日期码。日从0（星期一）到6（星期日）;月从1到12。

### calendar.prcal(year,w=2,l=1,c=6)

相当于 print calendar.calendar(year,w=2,l=1,c=6)。

### calendar.prmonth(year,month,w=2,l=1)

相当于 print calendar.month(year,month,w=2,l=1) 。

### calendar.setfirstweekday(weekday)

设置每周的起始日期码。0（星期一）到6（星期日）。

### calendar.timegm(tupletime)

和time.gmtime相反：接受一个时间元组形式，返回该时刻的时间戳（1970纪元后经过的浮点秒数）。

### calendar.weekday(year,month,day)

返回给定日期的日期码。0（星期一）到6（星期日）。月份为 1（一月） 到 12（12月）。

# 20210304(python)

## 函数

函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()。

任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。

函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。

函数内容以冒号起始，并且缩进。

return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。





### 函数调用





![img](https://docimg3.docs.qq.com/image/I0SthNF8oEqTqK_guFwWBQ?w=215&h=99)

## 参数传递

![img](https://docimg1.docs.qq.com/image/VK_TBRc4zxZj2ixfWRwKVA?w=593&h=280)

python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。

#### 不可变类型：

类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。

#### 可变类型：

类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响

### 传不可变对象实例??

### 传可变对象实例??

### 参数

以下是调用函数时可使用的正式参数类型：

- 必备参数
- 关键字参数
- 默认参数
- 不定长参数

#### 必备参数？？

必备参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。

调用printme()函数，必须传入一个参数，不然会出现语法错误：





报错





#### 关键字参数??

关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。

使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。

#### 默认参数??

调用函数时，默认参数的值如果没有传入，则被认为是默认值。

#### 不定长参数





加了星号（*）的变量名会存放所有未命名的变量参数。不定长参数实例如下：





### 匿名函数 lambda









### return 语句





### 变量作用域

函数内部的变量拥有一个局部作用域





命名空间是一个包含了变量名称们（键）和它们各自相应的对象们（值）的字典。

如果一个局部变量和一个全局变量重名，则局部变量会覆盖全局变量。

给函数内的全局变量赋值，必须使用 global 语句。





## 模块

模块(Module)，是一个 Python 文件，以 .py 结尾，包含了 Python 对象定义和Python语句。

### import 语句









### from…import 语句









### from…import* 语句

把一个模块的所有内容全都导入到当前的命名空间





### 搜索路径

当你导入一个模块，Python 解析器对模块位置的搜索顺序是：

1、当前目录

2、如果不在当前目录，Python 则搜索在 shell 变量 PYTHONPATH 下的每个目录。

3、如果都找不到，Python会察看默认路径。UNIX下，默认路径一般为/usr/local/lib/python/。

模块搜索路径存储在 system 模块的 sys.path 变量中。变量里包含当前目录，PYTHONPATH和由安装过程决定的默认目录。

### PYTHONPATH 变量

作为环境变量，PYTHONPATH 由装在一个列表里的许多目录组成。PYTHONPATH 的语法和 shell 变量 PATH 的一样。

在 Windows 系统，典型的 PYTHONPATH 如下：



在 UNIX 系统，典型的 PYTHONPATH 如下：



### dir()

dir() 函数一个排好序的字符串列表，内容是一个模块里定义过的名字。返回的列表容纳了在一个模块里定义的所有模块，变量和函数。







### globals() locals() 函数

globals() 和 locals() 函数可被用来返回全局和局部命名空间里的名字。

函数内部调用 locals()，返回的是所有能在该函数里访问的命名。

函数内部调用 globals()，返回的是所有在该函数里能访问的全局名字。

两个函数的返回类型都是字典。所以名字们能用 keys() 函数摘取。

### reload() 函数

当一个模块被导入到一个脚本，模块顶层部分的代码只会被执行一次。因此，如果你想重新执行模块里顶层部分的代码，可以用 reload() 函数。该函数会重新导入之前导入过的模块。语法如下：





在这里，module_name要直接放模块的名字，而不是一个字符串形式。

## 包 ？？？

包就是文件夹，但该文件夹下必须存在 init.py 文件, 该文件的内容可以为空。init.py 用于标识当前文件夹是一个包。

构建过程？？？

## 文件I/0

## 输入

### raw_input函数

raw_input是2.x版本的输入函数，在新版本环境下会报错，该函数未定义。在3.x版本中应该用input()代替raw_input()。

![img](https://docimg9.docs.qq.com/image/BPEsqg4w3QwSfx8zQzp_VQ?w=318&h=91)

### input函数

![img](https://docimg6.docs.qq.com/image/LXEg5NSEWcphsiq_blJPAw?w=561&h=78)

注意加括号！！





## 输出

### print





## File 方法

### 打开文件 -open 函数





**file_name：**file_name变量是一个包含了你要访问的文件名称的字符串值。

**access_mode：**access_mode决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读®。

**buffering:**如果buffering的值被设为0，就不会有寄存。如果buffering的值取1，访问文件时会寄存行。如果将buffering的值设为大于1的整数，表明了这就是的寄存区的缓冲大小。如果取负值，寄存区的缓冲大小则为系统默认。

![img](https://docimg10.docs.qq.com/image/ycH0-UNn-Tr9YqM_eTEGSA?w=800&h=475)

### 关闭文件 -close()函数





## 写write()方法





## 读read()方法





## 定位





### tell()

告诉你文件内的当前位置, 换句话说，下一次的读写会发生在文件开头这么多字节之后。

### seek（offset [,from]）

法改变当前文件的位置。Offset变量表示要移动的字节数。From变量指定开始移动字节的参考位置。

## 重命名-rename()





## 删除文件remove()





## 目录

### mkdir()方法

### chdir()方法

### rmdir()方法

### File 对象和 OS 对象

提供了很多文件与目录的操作方法？？？

## 文件属性

### file.closed

返回true如果文件已被关闭，否则返回false。

### file.mode

返回被打开文件的访问模式。

### file.name

返回文件的名称。

### file.softspace

如果用print输出后，必须跟一个空格符，则返回false。否则返回true。

## 异常处理

### 标准异常种类

BaseException 所有异常的基类

SystemExit 解释器请求退出

KeyboardInterrupt 用户中断执行(通常是输入^C)

Exception 常规错误的基类

StopIteration 迭代器没有更多的值

GeneratorExit 生成器(generator)发生异常来通知退出

StandardError 所有的内建标准异常的基类

ArithmeticError 所有数值计算错误的基类

FloatingPointError 浮点计算错误

OverflowError 数值运算超出最大限制

ZeroDivisionError 除(或取模)零 (所有数据类型)

AssertionError 断言语句失败

AttributeError 对象没有这个属性

EOFError 没有内建输入,到达EOF 标记

EnvironmentError 操作系统错误的基类

IOError 输入/输出操作失败

OSError 操作系统错误

WindowsError 系统调用失败

ImportError 导入模块/对象失败

LookupError 无效数据查询的基类

IndexError 序列中没有此索引(index)

KeyError 映射中没有这个键

MemoryError 内存溢出错误(对于Python 解释器不是致命的)

NameError 未声明/初始化对象 (没有属性)

UnboundLocalError 访问未初始化的本地变量

ReferenceError 弱引用(Weak reference)试图访问已经垃圾回收了的对象

RuntimeError 一般的运行时错误

NotImplementedError 尚未实现的方法

SyntaxError Python 语法错误

IndentationError 缩进错误

TabError Tab 和空格混用

SystemError 一般的解释器系统错误

TypeError 对类型无效的操作

ValueError 传入无效的参数

UnicodeError Unicode 相关的错误

UnicodeDecodeError Unicode 解码时的错误

UnicodeEncodeError Unicode 编码时错误

UnicodeTranslateError Unicode 转换时错误

Warning 警告的基类

DeprecationWarning 关于被弃用的特征的警告

FutureWarning 关于构造将来语义会有改变的警告

OverflowWarning 旧的关于自动提升为长整型(long)的警告

PendingDeprecationWarning 关于特性将会被废弃的警告

RuntimeWarning 可疑的运行时行为(runtime behavior)的警告

SyntaxWarning 可疑的语法的警告

UserWarning 用户代码生成的警告

### 异常处理

### try/except

### except（不带任何异常类型）

### except（带多种异常类型）

### try-finally

无论是否发生异常都将执行最后的代码。

### 触发异常raise





## OS文件/目录方法

参考地址：

传送门1[传送门2](http://python.usyiyi.cn/python_278/library/os.html)

os.access(path, mode)

检验权限模式

os.chdir(path)

改变当前工作目录

os.chflags(path, flags)

设置路径的标记为数字标记。

os.chmod(path, mode)

更改权限

os.chown(path, uid, gid)

更改文件所有者

os.chroot(path)

改变当前进程的根目录

os.close(fd)

关闭文件描述符 fd

os.closerange(fd_low, fd_high)

关闭所有文件描述符，从 fd_low (包含) 到 fd_high (不包含), 错误会忽略

os.dup(fd)

复制文件描述符 fd

os.dup2(fd, fd2)

将一个文件描述符 fd 复制到另一个 fd2

os.fchdir(fd)

通过文件描述符改变当前工作目录

os.fchmod(fd, mode)

改变一个文件的访问权限，该文件由参数fd指定，参数mode是Unix下的文件访问权限。

os.fchown(fd, uid, gid)

修改一个文件的所有权，这个函数修改一个文件的用户ID和用户组ID，该文件由文件描述符fd指定。

os.fdatasync(fd)

强制将文件写入磁盘，该文件由文件描述符fd指定，但是不强制更新文件的状态信息。

os.fdopen(fd[, mode[, bufsize]])

通过文件描述符 fd 创建一个文件对象，并返回这个文件对象

os.fpathconf(fd, name)

返回一个打开的文件的系统配置信息。name为检索的系统配置的值，它也许是一个定义系统值的字符串，这些名字在很多标准中指定（POSIX.1, Unix 95, Unix 98, 和其它）。

os.fstat(fd)

返回文件描述符fd的状态，像stat()。

os.fstatvfs(fd)

返回包含文件描述符fd的文件的文件系统的信息，像 statvfs()

os.fsync(fd)

强制将文件描述符为fd的文件写入硬盘。

os.ftruncate(fd, length)

裁剪文件描述符fd对应的文件, 所以它最大不能超过文件大小。

os.getcwd()

返回当前工作目录

os.getcwdu()

返回一个当前工作目录的Unicode对象

os.isatty(fd)

如果文件描述符fd是打开的，同时与tty(-like)设备相连，则返回true, 否则False。

os.lchflags(path, flags)

设置路径的标记为数字标记，类似 chflags()，但是没有软链接

os.lchmod(path, mode)

修改连接文件权限

os.lchown(path, uid, gid)

更改文件所有者，类似 chown，但是不追踪链接。

os.link(src, dst)

创建硬链接，名为参数 dst，指向参数 src

os.listdir(path)

返回path指定的文件夹包含的文件或文件夹的名字的列表。

os.lseek(fd, pos, how)

设置文件描述符 fd当前位置为pos, how方式修改: SEEK_SET 或者 0 设置从文件开始的计算的pos; SEEK_CUR或者 1 则从当前位置计算; os.SEEK_END或者2则从文件尾部开始. 在unix，Windows中有效

os.lstat(path)

像stat(),但是没有软链接

os.major(device)

从原始的设备号中提取设备major号码 (使用stat中的st_dev或者st_rdev field)。

os.makedev(major, minor)

以major和minor设备号组成一个原始设备号

os.makedirs(path[, mode])

递归文件夹创建函数。像mkdir(), 但创建的所有intermediate-level文件夹需要包含子文件夹。

os.minor(device)

从原始的设备号中提取设备minor号码 (使用stat中的st_dev或者st_rdev field )。

os.mkdir(path[, mode])

以数字mode的mode创建一个名为path的文件夹.默认的 mode 是 0777 (八进制)。

os.mkfifo(path[, mode])

创建命名管道，mode 为数字，默认为 0666 (八进制)

os.mknod(filename[, mode=0600, device])

创建一个名为filename文件系统节点（文件，设备特别文件或者命名pipe）。

os.open(file, flags[, mode])

打开一个文件，并且设置需要的打开选项，mode参数是可选的

os.openpty()

打开一个新的伪终端对。返回 pty 和 tty的文件描述符。

os.pathconf(path, name)

返回相关文件的系统配置信息。

os.pipe()

创建一个管道. 返回一对文件描述符(r, w) 分别为读和写

os.popen(command[, mode[, bufsize]])

从一个 command 打开一个管道

os.read(fd, n)

从文件描述符 fd 中读取最多 n 个字节，返回包含读取字节的字符串，文件描述符 fd对应文件已达到结尾, 返回一个空字符串。

os.readlink(path)

返回软链接所指向的文件

os.remove(path)

删除路径为path的文件。如果path 是一个文件夹，将抛出OSError; 查看下面的rmdir()删除一个 directory。

os.removedirs(path)

递归删除目录。

os.rename(src, dst)

重命名文件或目录，从 src 到 dst

os.renames(old, new)

递归地对目录进行更名，也可以对文件进行更名。

os.rmdir(path)

删除path指定的空目录，如果目录非空，则抛出一个OSError异常。

os.stat(path)

获取path指定的路径的信息，功能等同于C API中的stat()系统调用。

os.stat_float_times([newvalue])

决定stat_result是否以float对象显示时间戳

os.statvfs(path)

获取指定路径的文件系统统计信息

os.symlink(src, dst)

创建一个软链接

os.tcgetpgrp(fd)

返回与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组

os.tcsetpgrp(fd, pg)

设置与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组为pg。

os.tempnam([dir[, prefix]])

返回唯一的路径名用于创建临时文件。

os.tmpfile()

返回一个打开的模式为(w+b)的文件对象 .这文件对象没有文件夹入口，没有文件描述符，将会自动删除。

os.tmpnam()

为创建一个临时文件返回一个唯一的路径

os.ttyname(fd)

返回一个字符串，它表示与文件描述符fd 关联的终端设备。如果fd 没有与终端设备关联，则引发一个异常。

os.unlink(path)

删除文件路径

os.utime(path, times)

返回指定的path文件的访问和修改的时间。

os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])

输出在文件夹中的文件名通过在树中游走，向上或者向下。

os.write(fd, str)

写入字符串到文件描述符 fd中. 返回实际写入的字符串长度

os.path 模块

获取文件的属性信息。

