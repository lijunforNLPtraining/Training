2019/1/10

本实验参考了普林斯顿的论文，采用非监督学习的方式，计算测试集样本与随机选取出来的正负样本的相似度的平均值
其中在计算相似度的方法时，严格采用了论文中核心的算法方式，但效果并不好，其中a参数默认的是0.01，虽然大部分pw
也是这个数量级，但还是无法解释，所以表现不好的原因可能有这个因素
该实验比较有意义，这是第一次使用非监督学习，比较有意思，同事该论文的算法可以仔细推敲
