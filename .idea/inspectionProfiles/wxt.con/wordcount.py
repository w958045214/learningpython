#词频统计

#文本处理 分割单词

txt='''spark hive java hive hive spark scala flink java java SPARK'''

txt = txt.lower() #转小写
words = txt.split() #默认空格切分
#print(words)

#利用字典统计单词和个数
counts = {}
for word in words: #遍历列表中的元素也就是单词
    if len(word)==1: #单词的长度为1就退出本次循环
        continue
    else:
       counts[word] = counts.get(word,0)+1 #去counts字典里面获取元素spark,counts字典中没有这个spark,就为spark,0 然后 加1 就是spark:1 然后赋值到counts字典中

print(counts)