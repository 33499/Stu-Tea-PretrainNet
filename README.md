**Tea-Stu preTrainNet**	

​	我们所设计的预训练网络是一个非对称的老师-学生网络结构，对输入图片使用互补掩码的方法，老师网络与学生网络编码器的网络结构与网络参数相同，有利于编码器的训练学习，此外老师网络多了解码器部分，对老师网络输入可见的patch块经过编码器提取语义信息后做为解码器的输入，用于学习得到对老师网络不可见的patch块。