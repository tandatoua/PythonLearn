# <center> Django ORM
# 0、Say something
# 1、ORM 简介
   &emsp; &emsp;对象关系映射（Object Relational Mapping，简称ORM），通过使用描述对象和数据库之间映射的元数据，将程序中的对象自动持续化到关系数据库中。  
   &emsp; &emsp;ORM的方法论基于三个核心原则：   
   * 简单： 以最基本的形式建模数据  
   * 传达性：数据库结构呗任何人都能理解的语言文档化  
   * 精确性：基于数据库模型创建正确标准话的结构   
   &emsp; &emsp;ORM解决的主要问题是对象关系的映射。域模型和关系模型分别是建立在概念模型的基础上的。域模型是面向对象的，而关系模型是面向关系的。一般情况下，一个持久化类和一个表对应，类的每个实例对应表中的一条记录，类的每个属性对应表的每个字段。  

## 1.1 ORM技术特点：   
   &emsp; &emsp;1.提高了开发效率。由于ORM可以自动对Entity对象与数据库中的Table进行字段与属性的映射，所以我们实际可能已经不需要一个专用的、庞大的数据访问层。   
   &emsp; &emsp;2.ORM提供了对数据库的映射，不用sql直接编码，能够像操作对象一样从数据库获取数据。 
## 1.2 ORM优点
   &emsp; &emsp;1.ORM隐藏了数据访问细节，在开发过程中，不用考虑SQL语句问题，使得通用数据库交互变得简单，从而实现快速开发。      
   &emsp; &emsp;2.ORM让构造固话数据结构化变得简单，基本上所有的ORM框架都提供了通过对象模型构造关键型关系数据库结构的功能，不用将对象模型通过一条一条的SQL语句实现。  
&emsp; &emsp;3、ORM便于开发管理、提高开发效率、可维护性、可扩展性，降低运行性能。
## 1.3 ORM缺点
&emsp; &emsp;1.性能，自动化意味着映射和关联自动管理，这势必会牺牲一定的性能。
&emsp; &emsp;2.对于复杂的数据库操作，ORM仍然力不从心。
# 2、Django ORM
&emsp; &emsp;Django框架自带ORM模型。
## 2.1模型设计
&emsp; &emsp;Django遵循Code Frist 原则，即：根据代码中定义的类自动生成数据库。   
&emsp; &emsp;Django的数据模型的建立比较简单，就是继承django.db.models中的model类，然后给其增加相应的属性。每个属性对应关系数据库里面的一个字段。     
&emsp; &emsp;然后通过manage.py的makemigrations and migrate commond，执行数据库迁移。
### 2.1.1 django字段类型
&emsp; &emsp;1、models.AutoField　　自增列 = int(11)
　　如果没有的话，默认会生成一个名称为 id 的列，如果要显示的自定义一个自增列，必须将给列设置为主键 primary_key=True。  
&emsp; &emsp;2、models.CharField　　字符串字段
　　必须 max_length 参数  
&emsp; &emsp;3、models.BooleanField　　布尔类型=tinyint(1)
　　不能为空，Blank=True  
&emsp; &emsp;4、models.ComaSeparatedIntegerField　　用逗号分割的数字=varchar
　　继承CharField，所以必须 max_lenght 参数  
&emsp; &emsp;5、models.DateField　　日期类型 date
　　对于参数，auto_now = True 则每次更新都会更新这个时间；auto_now_add 则只是第一次创建添加，之后的更新不再改变。  
&emsp; &emsp;6、models.DateTimeField　　日期类型 datetime
　　同DateField的参数  
&emsp; &emsp;7、models.Decimal　　十进制小数类型 = decimal
　　必须指定整数位max_digits和小数位decimal_places  
&emsp; &emsp;8、models.EmailField　　字符串类型（正则表达式邮箱） =varchar
　　对字符串进行正则表达式  
&emsp; &emsp;9、models.FloatField　　浮点类型 = double  
&emsp; &emsp;10、models.IntegerField　　整形  
&emsp; &emsp;11、models.BigIntegerField　　长整形  
　　integerfieldranges = {  
　　　　'SmallIntegerField': (-32768, 32767),    
　　　　'IntegerField': (-2147483648, 2147483647),  
　　　　'BigIntegerField': (-9223372036854775808, 9223372036854775807),  
　　　　'PositiveSmallIntegerField': (0, 32767),  
　　　　'PositiveIntegerField': (0, 2147483647),  
　　}  
&emsp; &emsp;12、models.IPAddressField　　字符串类型（ip4正则表达式）   
&emsp; &emsp;13、models.GenericIPAddressField　　字符串类型（ip4和ip6是可选的）
　　参数protocol可以是：both、ipv4、ipv6
　　验证时，会根据设置报错   
&emsp; &emsp;14、models.NullBooleanField　　允许为空的布尔类型  
&emsp; &emsp;15、models.PositiveIntegerFiel　　正Integer  
&emsp; &emsp;16、models.PositiveSmallIntegerField　　正smallInteger  
&emsp; &emsp;17、models.SlugField　　减号、下划线、字母、数字  
&emsp; &emsp;18、models.SmallIntegerField　　数字
　　数据库中的字段有：tinyint、smallint、int、bigint  
&emsp; &emsp;19、models.TextField　　字符串=longtext  
&emsp; &emsp;20、models.TimeField　　时间 HH:MM[:ss[.uuuuuu]]  
&emsp; &emsp;21、models.URLField　　字符串，地址正则表达式  
&emsp; &emsp;22、models.BinaryField　　二进制  
&emsp; &emsp;23、models.ImageField   图片  
&emsp; &emsp;24、models.FilePathField 文件  
### 2.1.2相关参数
&emsp; &emsp;1、null=True
　　数据库中字段是否可以为空  
&emsp; &emsp;2、blank=True
　　django的 Admin 中添加数据时是否可允许空值  
&emsp; &emsp;3、primary_key = False 
　　主键，对AutoField设置主键后，就会代替原来的自增 id 列  
&emsp; &emsp;4、auto_now 和 auto_now_add
　　auto_now   自动创建---无论添加或修改，都是当前操作的时间
　　auto_now_add  自动创建---永远是创建时的时间  
&emsp; &emsp;5、choices
GENDER_CHOICE = (
        (u'M', u'Male'),
        (u'F', u'Female'),
    )
gender = models.CharField(max_length=2,choices = GENDER_CHOICE)  
&emsp; &emsp;6、max_length  
&emsp; &emsp;7、default　　默认值  
&emsp; &emsp;8、verbose_name　　Admin中字段的显示名称  
&emsp; &emsp;9、name|db_column　　数据库中的字段名称  
&emsp; &emsp;10、unique=True　　不允许重复  
&emsp; &emsp;11、db_index = True　　数据库索引  
&emsp; &emsp;12、editable=True　　在Admin里是否可编辑  
&emsp; &emsp;13、error_messages=None　　错误提示  
&emsp; &emsp;14、auto_created=False　　自动创建  
&emsp; &emsp;15、help_text　　在Admin中提示帮助信息  
&emsp; &emsp;16、validators=[]  
&emsp; &emsp;17、upload-to   上传到哪个位置,更多与image,filepath配合使用
## 2.2 关系
&emsp; &emsp;1、一对一：OneToOneField（其他表）  
&emsp; &emsp;2、多对一：ForeignKey（其他表）   
&emsp; &emsp;3、多对多：ManyToManyField（其他表）   
&emsp; &emsp;4、一对多：Django ORM中，不能显示定义一对多的关系，但可以使用模型对象的*_set语法来反向调用多对一的关系。
## 2.3 查询
&emsp; &emsp;Django ORM可以通过一些方法来实现。其中的很多方法返回的是Django自定义的QuerySet类的迭代器。返回QuerySet的常见方法包括：   
&emsp; &emsp;    * all()  
 &emsp; &emsp;   * filter()  
 &emsp; &emsp;   * exclude()  
 &emsp; &emsp;   * annotate()  
 &emsp; &emsp;   * order_by()  
 &emsp; &emsp;   * reverse()  
 &emsp; &emsp;   * distinct()  
**Notes:values() 和 vlue_list() 与 all()区别:**   
  &emsp; &emsp;    .all()是取得所有列的数据，可以加.values()取出某一列，每一个元素为一个字典  
  &emsp; &emsp;    values_list()，获取到的元素为一个个元组,也可以加多个参数来获取多列:
##2.4 F表达式和Q表达式
   &emsp; &emsp; 当一般的查询语句已经无法满足我们的需求时，Django为我们提供了F和Q复杂查询语句。
    F查询：F表达式指代了一列，对于update操作时引用列的值有用。
    Q查询：Q表达式代表了WHERE的一个条件，可以用于多个WHERE条件的连接。这些都是Django ORM用来弥补缺陷的。就拿Q表达式来说。查询方法中跟多个参数的话，相当于多个WHERE条件。这些条件会默认为AND关系。
    Extra
    