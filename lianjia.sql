#每月二手房详情
SELECT
	month(createdate) as every_month,
	FORMAT(sum(totalPrice),2) as all_amount, #所有价格
	FORMAT(sum(unitPrice),2) as all_single_price,  #单价合计
	FORMAT(sum(mianji),2) as all_mianji,  #面积合计
	count(1) as all_sell,				 #总可卖套数
	FORMAT(sum(totalPrice) / count(1),2) as avg_house_amount, #平均单套价格
	FORMAT(sum(unitPrice) / count(1),2)  as avg_pre_price,  #平均每平方价格
  FORMAT(sum(mianji) / count(1),2)  as avg_mianji
FROM
	lianjia_hefei_info;
GROUP BY every_month

#各区二手房详情
SELECT
	area,
	FORMAT(sum(totalPrice),2) as all_amount, #所有价格
	FORMAT(sum(unitPrice),2) as all_single_price,  #单价合计
	FORMAT(sum(mianji),2) as all_mianji,  #面积合计
	count(1) as all_sell,				 #总可卖套数
	FORMAT(sum(totalPrice) / count(1),2) as avg_house_amount, #平均单套价格
	FORMAT(sum(unitPrice) / count(1),2)  as avg_pre_price,  #平均每平方价格
  FORMAT(sum(mianji) / count(1),2)  as avg_mianji
FROM
	lianjia_hefei_info

GROUP BY area
order by avg_pre_price ;


#各区各房型二手房详情
SELECT
	area,fx,
	FORMAT(sum(totalPrice),2) as all_amount, #所有价格
	FORMAT(sum(unitPrice),2) as all_single_price,  #单价合计
	FORMAT(sum(mianji),2) as all_mianji,  #面积合计
	count(1) as all_sell,				 #总可卖套数
	FORMAT(avg(totalPrice),2) as avg_house_amount1,
	FORMAT(sum(totalPrice) / count(1),2) as avg_house_amount, #平均单套价格
  FORMAT(avg(unitPrice),2) as avg_pre_price1,
	FORMAT(sum(unitPrice) / count(1),2)  as avg_pre_price,  #平均每平方价格
  FORMAT(avg(mianji),2) as avg_mianji1,
  FORMAT(sum(mianji) / count(1),2)  as avg_mianji
FROM
	lianjia_hefei_info
where area <> 'L2'
GROUP BY area,fx
order by avg_pre_price ;


#各区二手房可卖数量，最高/最低（总价，单价 ）
select area,count(1),max(totalPrice),min(totalPrice),max(unitPrice),min(unitPrice),FORMAT(avg(unitPrice),2),FORMAT(avg(totalPrice),2) from lianjia_hefei_info
where area <> 'L2'
group by area
order by min(unitPrice);


#各区各房型二手房可卖数量，最高/最低（总价，单价 ）
select area,fx,max(totalPrice),min(totalPrice),max(unitPrice),min(unitPrice),FORMAT(avg(unitPrice),2),FORMAT(avg(totalPrice),2) from lianjia_hefei_info
where area <> 'L2'
group by area,fx
order by area,fx,min(unitPrice);



****************************************************************************************************************
delete  from lianjia_hefei where createdate like '%2017-06-05%'

#各区域可卖套数
SELECT
	month(createdate) as every_month,
	area,
	sum(allhouse) amount
FROM
	lianjia_hefei
GROUP BY
	area,every_month
ORDER BY
	area,every_month,amount DESC;


#各区域各房型可卖套数
SELECT
	area,
	fangxing,
	sum(allhouse) amount
FROM
	lianjia_hefei
GROUP BY
	area_en,
	fangxing_en
ORDER BY
	fangxing_en,
	amount DESC;


#各房型可卖套数
SELECT
	fangxing,
	sum(allhouse) amount
FROM
	lianjia_hefei
GROUP BY
	fangxing_en
ORDER BY
	amount DESC;


#各区域各房型可卖套数
SELECT
	area,
	sum(allhouse) amount,
	FORMAT(
		sum(allhouse) / (
			SELECT
				sum(amount)
			FROM
				(
					SELECT
						area,
						sum(allhouse) amount
					FROM
						lianjia_hefei
					GROUP BY
						area
					ORDER BY
						amount DESC
				) b
		) * 100,
		2
	) AS present
FROM
	lianjia_hefei
GROUP BY
	area
ORDER BY
	amount DESC







