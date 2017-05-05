# 爬虫_链家合肥二手房情况
## 5W2H
## 1.研究的目的(Why):
	分析合肥二手房情况

## 2.研究的内容(What):
	A.各区域二手房总数
	B.各区域二手房价格区间 单价，总价

## 3.研究对象-分析谁(Who):
	合肥二手房情况

## 4.调查设计(Where)与研究方法(How):
	链家
	数据采集方法 :Python爬虫
	   main()入口函数
	   lianjia1()合肥各区县各房型总数
	   lianjia1()合肥各区县各房型总数-浏览器伪装
	   connLinajia() 数据库连接
	   insertLianjia() 文件写入数据库表
	   truncate() 情况表
	   makepie() 图标展示


	   数据库表结构
	  CREATE TABLE `lianjia_hefei` (
	    `id` int(11) NOT NULL AUTO_INCREMENT,
	    `area` varchar(30) DEFAULT NULL,
	    `fangxing` varchar(10) DEFAULT NULL,
	    `allhouse` int(10) DEFAULT NULL,
	    `createdate` datetime DEFAULT NULL,
	    PRIMARY KEY (`id`)
	  ) ENGINE=MyISAM AUTO_INCREMENT=31 DEFAULT CHARSET=gbk;
		研究方法: Sql分组

## 5.项目周期-分析多久(When):
    XXX

## 6.项目报价-花多少钱(When):

## 7.项目组成员-谁来分析(Who):





具体项目图表展示：https://zhuanlan.zhihu.com/p/26633979

R相关分析： https://github.com/guiyi/R/blob/master/mysql.R

<img src="https://pic1.zhimg.com/v2-1e30e53cee57c2e6d7e8197242daaba8_b.png" alt="" style="max-width:100%;">
<img src="https://pic4.zhimg.com/v2-f60ffad0fb4cc8a398806bfbc8ab432b_b.png" alt="" style="max-width:100%;">
<img src="https://pic1.zhimg.com/v2-15c561859b0e3b8db1d3085b1c213070_b.png" alt="" style="max-width:100%;">
