为anaconda的jupyter notebook设置初始化目录

在使用jupyter进行编程时，初始化目录可能不是自己想要的目录，那么下面讲解修改成自己想要的目录。

1） 在命令行中输入jupyter notebook --generate-config，会产生一个配置文件

　　我的会显示Writing default config to: C:\Users\allen\.jupyter\jupyter_notebook_config.py这样的提示。

 

2） 找到对应的文件，搜索c.NotebookApp.notebook_dir

　　将前面的#注释去掉，在后面填上自己想要设置的初始化目录。比如我设置成c.NotebookApp.notebook_dir = u'D:\chengxu\ML'

　　以后就会将'D:\chengxu\ML'这个目录成为初始化的目录。