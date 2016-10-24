from GUI import *
from GUISR import *
from threading import Thread
import subprocess
import os
import json
import sys
import time
thrd=None
app=wx.App(False)
frame=MyFrame1(None)
frame2=MyFrame2(None)
donescouting=0
scoutlist=[]
reportbox=[]
def closeframe(event):
	frame2.Hide()
frame2.Bind(wx.EVT_CLOSE,closeframe)
def showframe(event):
	frame2.Show()
frame.m_button113.Bind(wx.EVT_BUTTON,showframe)
def killscout(pid):
	try:
		startupinfo = subprocess.STARTUPINFO()
		startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
		subprocess.Popen(["TASKKILL","/F","/T","/pid",str(pid)],startupinfo=startupinfo)
	except:
		pass
def killimage():
	try:
		startupinfo = subprocess.STARTUPINFO()
		startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
		subprocess.Popen(["TASKKILL","/F","/T","/im","scout.exe"],startupinfo=startupinfo)
	except:
		pass
def onclose(event):
	killimage()
	sys.exit()
def checkprocess():
	global scoutprocess,thrd,lastupdate
	try:
		if frame.m_button1.IsEnabled():
			return
		else:
			if (time.time()-lastupdate)>20:
				killscout(scoutprocess.pid)
				lastupdate=time.time()
				frame.m_textCtrl5.SetValue("Error in connection. Trying again in 5 seconds.")
				frame.m_gauge2.SetValue(0)
				wx.CallLater(5000,execscout,None)
				return
			wx.CallLater(1000,checkprocess)
	except:
		wx.CallLater(1000,checkprocess)
		return
frame.Bind(wx.EVT_CLOSE,onclose)
if os.path.exists('config.json'):
	try:
		config=json.loads(open('config.json','r').read())
		if 'scoutpos' in config:
			frame.m_textCtrl1.SetValue(config['scoutpos'])
		if 'mailguy' in config:
			frame.m_textCtrl2.SetValue(config['mailguy'])
		if 'declarewar' in config:
			frame.m_textCtrl3.SetValue(config['declarewar'])
		if 'server' in config:
			frame.m_textCtrl51.SetValue(config['server'])
		if 'enablelog' in config:
			frame.m_checkBox1.SetValue(config['enablelog'])
		if 'usetim' in config:
			frame.m_checkBox3.SetValue(config['usetim'])
		if 'disableurl' in config:
			frame.m_checkBox4.SetValue(config['disableurl'])
		if 'evonyurl' in config:
			frame.m_checkBox2.SetValue(config['evonyurl'])
	except:
		pass
def handletext(value):
	global lastupdate
	lastupdate=time.time()
	frame.m_textCtrl5.write(value)
	try:
		enablelog=frame.m_checkBox1.GetValue()
		if enablelog:
			gg=open('log.txt','a')
			gg.write(value)
			gg.close()
	except:
		pass
def handleprogress(value):
	frame.m_gauge2.SetValue(value)
def handleerror(value):
	global lastupdate,scoutprocess
	try:
		killscout(scoutprocess.pid)
	except:
		pass
	lastupdate=time.time()
	frame.m_textCtrl5.SetValue("Error while building account. Trying again in 5 seconds.")
	frame.m_button1.Enable()
	frame.m_gauge2.SetValue(0)
	wx.CallLater(5000,execscout,None)
def clickreport(event):
	obj=event.GetEventObject().GetContainingSizer()
	value=obj.reporturl
	if 'http://' in value:
		value1=value[7:]
	if (frame.m_checkBox3.GetValue()):
		url='http://evonystuff.com/srViewer/srLoader.asp?srURL='+value1
	else:
		url=obj.showurl
	try:
		startupinfo = subprocess.STARTUPINFO()
		startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
		os.system(("start /max "+url))
	except:
		pass
def finishhandler(value):
	global donescouting,scoutlist,lastupdate,reportbox,scoutprocess
	try:
		killscout(scoutprocess.pid)
	except:
		pass
	lastupdate=time.time()
	urls=value.split('|||')
	frame.m_textCtrl5.SetValue(urls[0])
	reportbox[donescouting].m_button105.Enable()
	reportbox[donescouting].m_staticText17.SetLabel("Finished")
	reportbox[donescouting].m_textCtrl23.SetValue(urls[0])
	reportbox[donescouting].reporturl=urls[1]
	reportbox[donescouting].showurl=urls[0]
	reportbox[donescouting].m_button105.Bind(wx.EVT_BUTTON,clickreport)
	frame2.m_scrolledWindow6.Layout()
	donescouting+=1
	frame.m_gauge2.SetValue(0)
	if donescouting>=len(scoutlist):
		frame.m_button1.Enable()
		return
	else:
		wx.CallLater(1000,execscout,None)
def fatalerrorhandler(value):
	global lastupdate,donescouting,reportbox,scoutlist,scoutprocess
	try:
		killscout(scoutprocess.pid)
	except:
		pass
	val=value.strip().split('FATALERROR')[-1].strip()
	lastupdate=time.time()
	frame.m_textCtrl5.SetValue(val)
	frame.m_gauge2.SetValue(0)
	reportbox[donescouting].m_staticText17.SetLabel("Error")
	donescouting+=1
	if donescouting>=len(scoutlist):
		frame.m_button1.Enable()
def fff(comm):
	global scoutprocess,textlist,gaugepos
	startupinfo = subprocess.STARTUPINFO()
	startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
	p=subprocess.Popen(comm,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,startupinfo=startupinfo)
	scoutprocess=p
	for q in p.stdout:
		if 'PROGRESSREPORT' in q:
			q=int(q.strip().split('PROGRESSREPORT')[-1].strip())
			wx.CallAfter(handleprogress,q)
			continue
		if 'ERRORREPORT' in q:
			wx.CallAfter(handleerror,q)
			break
		if 'FATALERROR' in q:
			wx.CallAfter(fatalerrorhandler,q)
			break
		if 'FINISHREPORT' in q:
			q=q.strip().split('FINISHREPORT')[-1].strip()
			wx.CallAfter(finishhandler,q)
			break
		wx.CallAfter(handletext,q)
def getscoutlist(x):
	y=x.split(';')
	r=[]
	for j in y:
		g=j.strip().split(',')
		try:
			f=int(g[0].strip())+int(g[1].strip())*800
			r.append(f)
		except:
			pass
	return r
def initreports():
	global scoutlist,reportbox,donescouting
	for i in range(donescouting,len(scoutlist)):
		g=scoutlist[i]
		f=scoutbox(frame2.m_scrolledWindow6,frame2.bSizer17)
		coord=((g%800),int(g/800))
		f.m_button105.SetLabel(str(coord))
		f.m_button105.Disable()
		reportbox.append(f)
	frame2.m_scrolledWindow6.Layout()
def execscout(event):
	global thrd,enablelog,scoutlist,donescouting,lastupdate
	frame.m_button1.Disable()
	frame.m_textCtrl5.SetValue("Starting to build account for scouting....")
	if event!=None:
		scoutlist+=getscoutlist(frame.m_textCtrl1.GetValue().strip())
	if donescouting>=len(scoutlist):
		frame.m_textCtrl5.SetValue("Finished scouting all valid co-ordinates entered.")
		frame.m_button1.Enable()
		return
	if event!=None:
		initreports()
	scoutpos=scoutlist[donescouting]
	mailguy=frame.m_textCtrl2.GetValue()
	declarewar=frame.m_textCtrl3.GetValue()
	server=frame.m_textCtrl51.GetValue()
	enablelog=frame.m_checkBox1.GetValue()
	usetim=frame.m_checkBox3.GetValue()
	disableurl=frame.m_checkBox4.GetValue()
	evonyurl=frame.m_checkBox2.GetValue()
	try:
		f=open('config.json','w')
		d={'scoutpos':(frame.m_textCtrl1.GetValue().strip()),'mailguy':mailguy,'declarewar':declarewar,'server':server,'enablelog':enablelog,'usetim':usetim,'disableurl':disableurl,'evonyurl':evonyurl}
		json.dump(d,f)
		f.close()
	except:
		pass
	thrd=Thread(target=fff,args=(["scout.exe",server,mailguy,declarewar,str(scoutpos),str(usetim),str(disableurl),str(evonyurl)],))
	thrd.daemon=True
	thrd.start()
	lastupdate=time.time()
	wx.CallLater(1000,checkprocess)
frame.m_button1.Bind(wx.EVT_BUTTON,execscout)
frame.Show()
app.MainLoop()
