#encoding:utf-8
'''由于文件较大，需要读取一行处理一行，直接写进文件中
'''
import xlwt
import xlsxwriter
import re
def proLine(line):
	#print line
	tmp=line.replace(u'：',u':').split(u'|')
	date=tmp[0]
	province=tmp[2]
	city=tmp[4]
	work_order=tmp[5]
	sent=''.join(tmp[6:])
	#sent为剩余要处理的文本
	#首先对sent以";"进行切分
	#然后对切分后的每一个元素以":"进行切割，可以得到[方面：具体内容]
	w_tmp=sent.split(u';')
	aspects=[]
	contents=[]
	for w in w_tmp:
		#print w
		if ':' in w:
			ind=w.index(u':')
			aspects.append(w[:ind])
			contents.append(w[ind+1:])
		else:
			pass
	return date,province,city,work_order,aspects,contents
		
def process(src,res):
	wb=xlsxwriter.Workbook(res)
	#wt=xlwt.Workbook()
	#ws=wt.add_sheet('sheet')
	ws=wb.add_worksheet(u'sheet1')
	num=1
	ws.write(0,0,u"日期")
	ws.write(0,1,u"省份")
	ws.write(0,2,u"城市")
	ws.write(0,3,u"工单号")
	ws.write(0,4,u"模板")
	#ws.write(0,5,"内容")
	
	with open(src,'r') as f_r:
		for line in f_r:
			line=line.decode('utf-8').strip()
			if line:
				data=proLine(line)
				ws.write(num,0,data[0])
				ws.write(num,1,data[1])
				ws.write(num,2,data[2])
				ws.write(num,3,data[3])
				ws.write(num,4,u'.*'.join(data[4])+u'.*')
				num+=1
	#wt.save(res)
	wb.close()
	
def choose(model,src,res,res2):
	flag=True
	flag_model=True
	with open(res2,'w') as f_w2:
		with open(res,'w') as f_w:
			with open(src,'r') as f_r:
				for line in f_r:
					line=line.decode('utf-8').strip()
					if line:
						if u':' in line:
							tmp=line.split(':')
							if len(tmp)>3:
								for w in model:
									pattern=re.compile(w)
									match = pattern.match(line)
									if match:
										flag_model=False
										break
								if flag_model==True:
									f_w.write((line+'\n').encode('utf-8'))
								else:
									flag_model=True									
							else:
								f_w2.write((line+'\n').encode('utf-8'))
						elif u';' in line:
							tmp=line.split(';')
							if len(tmp)>3:
								for w in model:
									pattern=re.compile(w)
									match = pattern.match(line)
									if match:
										flag_model=False
										break
								if flag_model==True:
									f_w.write((line+'\n').encode('utf-8'))
								else:
									flag_model=True	
							else:
								f_w2.write((line+'\n').encode('utf-8'))
						else:
							f_w2.write((line+'\n').encode('utf-8'))
model=[
	u'.*1 、故障时间.*故障号码为.*2 、故障现象为.*3 、是否曾欠费停机.*4 、周围人是否使用正常.*5 、故障地点为.*6 、是否个别网站/第三方应用无法使用.*7 、其他为.*客户要求.*',
	u'.*主活动名称:.*主活动ID:.*子活动名称:.*操作员组织:.*操作员工号:.*操作员:.*渠道类型:.*办理时间:.*反映.*',
	u'.*1、葫芦岛家庭宽带客户:.*2、设备信息：.*3、联系电话：.*4、故障地点：.*5、预处理内容：.*结果:.*客户要求：.*',
	u'.*1、营口家庭宽带客户:.*2、设备信息：.*3、联系电话：.*4、故障地点：.*5、预处理内容：.*结果:.*客户要求：.*',
	u'.*1、本溪家庭宽带客户:.*2、设备信息：.*3、联系电话：.*4、故障地点：.*5、预处理内容：.*结果:.*客户要求：.*',
	u'.*1、大连家庭宽带客户:.*2、设备信息：.*3、联系电话：.*4、故障地点：.*5、预处理内容：.*结果:.*客户要求：.*',
	u'.*1、沈阳家庭宽带客户:.*2、设备信息：.*3、联系电话：.*4、故障地点：.*5、预处理内容：.*结果:.*客户要求：.*',
	u'.*1、锦州家庭宽带客户:.*2、设备信息：.*3、联系电话：.*4、故障地点：.*5、预处理内容：.*结果:.*客户要求：.*',
	u'.*1、抚顺家庭宽带客户:.*2、设备信息：.*3、联系电话：.*4、故障地点：.*5、预处理内容：.*结果:.*客户要求：.*',
	u'.*1、铁岭家庭宽带客户:.*2、设备信息：.*3、联系电话：.*4、故障地点：.*5、预处理内容：.*结果:.*客户要求：.*',
	u'.*1、盘锦家庭宽带客户:.*2、设备信息：.*3、联系电话：.*4、故障地点：.*5、预处理内容：.*结果:.*客户要求：.*',
	u'.*1、朝阳家庭宽带客户:.*2、设备信息：.*3、联系电话：.*4、故障地点：.*5、预处理内容：.*结果:.*客户要求：.*',
	u'.*1、阜新家庭宽带客户:.*2、设备信息：.*3、联系电话：.*4、故障地点：.*5、预处理内容：.*结果:.*客户要求：.*',
	u'.*1、丹东家庭宽带客户:.*2、设备信息：.*3、联系电话：.*4、故障地点：.*5、预处理内容：.*结果:.*客户要求：.*',
	u'.*1、鞍山家庭宽带客户:.*2、设备信息：.*3、联系电话：.*4、故障地点：.*5、预处理内容：.*结果:.*客户要求：.*',
	u'.*1、.*家庭宽带客户:.*2、设备信息：.*3、联系电话：.*4、故障地点：.*5、预处理内容：.*结果:.*客户要求：.*',
	u'.*1、.*家庭宽带客户:.*2、设备信息：.*3、联系电话：.*4、故障地点：.*5、预处理内容：.*',
	u'.*1 、故障开始时间为.*2 、故障现象为.*3 、手机4G上网是否正常(或是否在所有地点均不好用).*4 、多次重启设备是否恢复.*5 、故障地点.*6 、是否个别网站/第三方应用无法使用（选是时填写网站或软件名）.*7 、其他.*客户要求.*',
	u'.*1 、故障开始时间.*2 、故障现象.*3 、手机4G上网是否正常(或是否在所有地点均不好用).*4 、故障地点.*5 、是否个别网站/第三方应用无法使用（选是时填写网站或软件名）.*6 、其他.*客户要求.*',
	u'.*1 、故障类型.*2 、故障开始时间.*3 、故障号码.*4 、周围人是否使用正常（关开4G开关或更换手机是否正常）.*5 、故障地点.*6 、其他信息及客户要求.*',
	u'.*1 、故障开始时间.*2 、故障现象.*3 、手机4G上网是否正常(或是否在所有地点均不好用).*4 、故障地点.*5 、是否个别网站/第三方应用无法使用（选是时填写网站或软件名）.*6 、其他.*客户要求.*',
	u'.*该客户通过服务质量监督电话申诉，.*',
	u'.*主活动名称:.*主活动ID:.*子活动名称:.*操作员组织:.*操作员工号:.*渠道类型:.*办理时间:.*',
	u'.*1 、故障开始时间.*2 、故障现象.*3 、多次重启设备.*4 、故障地点.*5 、是否个别网站/第三方应用无法使用（选是时填写网站或软件名）.*6 、其他.*客户要求.*',
	u'【客户信息】客户编号:.*客户名称:.*集团级别:.*客户服务等级:.*集团客户经理联系人:.*集团客户经理联系电话:.*客户经理:.*客户经理电话:.*客户区域所在城市:.*所在区县:.*产品实例标识:.*业务保障等级:.*业务服务时限:.*业务类型:.*【投诉现象】:.*投诉人信息】回复号码:.*客户联系电话:.*【处理建议流程】.*',
	u'1 、故障开始时间.*2 、故障现象.*3 、手机4G上网是否正常(或是否在所有地点均不好用).*4 、其他.*客户要求.*',
	
		]
if __name__=='__main__':
	import sys
	#process(sys.argv[1].decode('gbk'),sys.argv[2].decode('gbk'))
	choose(model,sys.argv[1].decode('gbk'),sys.argv[2].decode('gbk'),sys.argv[3].decode('gbk'))
	
				
				
				
				