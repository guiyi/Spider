# 爬虫_链家合肥二手房情况
## main()入口函数
### lianjia1()合肥各区县各房型总数
### lianjia1()合肥各区县各房型总数-浏览器伪装
### connLinajia() 数据库连接
### insertLianjia() 文件写入数据库表
### truncate() 情况表
### makepie() 图标展示


## 数据库表结构
CREATE TABLE `lianjia_hefei` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `area` varchar(30) DEFAULT NULL,
  `fangxing` varchar(10) DEFAULT NULL,
  `allhouse` int(10) DEFAULT NULL,
  `createdate` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=31 DEFAULT CHARSET=gbk;



具体项目图表展示：https://zhuanlan.zhihu.com/p/26633979
