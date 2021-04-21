
#```
# Author : Stiiwo
# Time : 2021-04-21
# github : stwtgithub
#```

import base64
import itertools
import time
from progress.bar import Bar

bar = Bar('Processing', max=100, fill='#', suffix='%(percent)d%%')


def ErrorCharPermutation(s, n):	
	#错误字符替换，没有列全，少了几种情况
	if n == "q":				
		s = "9" + s[1:]
	elif n == "I":			
		s = s[0:2] + "1" + s[3:]
	elif n == "B1":			
		s = s[0:4] + "8" + s[5:]
#	elif n == "b"
#		s = s[0:4] + "6" + s[5:]
	elif n == "g":
		s = s[0:6] + "9" + s[7:]
	elif n == "z1":
		s = s[0:7] + "2" + s[8:]
	elif n == "z2":
		s = s[0:8] + "2" + s[9:]	
	elif n == "z3":
		s = s[0:13] + "2" + s[14:]
	elif n == "z4":
		s = s[0:17] + "2" + s[18:]
	elif n == "s":
		s = s[0:11] + "5" + s[12:]
	return s

def UpperLowerPermutation(s, count):	
	# 将任意count个字符小写,返回所有集合

	def nPen(s, i):# 将第i个字符小写（1开始）
		i = i-1
		k = i+1
		tmp = s[:i] + s[i].lower() + s[k:]
		return tmp
	tempindex = list(range(1,20))
	newlist = []
	new = ""

	templist = list(itertools.combinations(tempindex,count))
	for tempindex_i in templist:
		new = s
		for each in tempindex_i:
			new = nPen(new, each)
		newlist.append(new)
	return newlist

s = "QWIHBLGZZXJSXZNVBZW"	#19

errorchar = ["q", "I", "B1", "g", "z1", "z2", "z3", "z4", "s"]



combination = list(itertools.combinations(errorchar,6))		#假设错误字符为6个,遍历所有组合

res = []
corr_count = 0

for i in combination:
	tmp = s
	for n in i:
		tmp = ErrorCharPermutation(tmp, n)
		tmp_list = UpperLowerPermutation(tmp, 5)		#假设大小写变化为5个
		# print(len(tmp_list))
		for tmp_i in tmp_list:
			res.append(tmp_i)
			try:
				f = base64.b64decode(tmp_i + "=").decode('utf-8')
				corr_count = corr_count + 1
				if "Aman" in f:			#过滤找出正确答案
					if "very" in f:
						print (f)
			except:
				pass
	bar.next()
bar.finish()

print("测试总数 ： " , len(res))
print ("正确数量 ： " , corr_count)
