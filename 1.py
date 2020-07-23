import sqlite3
import os
conn = sqlite3.connect('medical.db')
c=conn.cursor()

def initiate():
	c.execute("PRAGMA foreign_keys=ON")
	c.execute("CREATE TABLE patient (pid INTEGER PRIMARY KEY, name TEXT NOT NULL, weight REAL NOT NULL, height REAL NOT NULL, bloodgrp TEXT NOT NULL, city TEXT NOT NULL, phoneno INTEGER NOT NULL, dob TEXT NOT NULL, age INTEGER DEFAULT 0)")
	c.execute("CREATE TABLE test (testid INTEGER PRIMARY KEY, name TEXT, reldis TEXT)")
	c.execute("CREATE TABLE dept (depid INTEGER PRIMARY KEY, depname TEXT)")
	c.execute("CREATE TABLE doctor (docid INTEGER PRIMARY KEY, dname TEXT, dphoneno INTEGER, spec TEXT, explevel INTEGER check(length(explevel<=10)) )")
	c.execute("CREATE TABLE treatment (trid INTEGER PRIMARY KEY, name TEXT, avsuccess REAL, reldis TEXT)")
	
	c.execute("CREATE TABLE trplink (trpid INTEGER PRIMARY KEY, pid INTEGER, successrate REAL, trid INTEGER, FOREIGN KEY (pid) REFERENCES patient(pid), FOREIGN KEY(trid) REFERENCES treatment(trid))")
	c.execute("CREATE TABLE tplink (tpid INTEGER PRIMARY KEY, testid INTEGER NOT NULL, pid INTEGER DEFAULT 0, FOREIGN KEY (pid) REFERENCES patient(pid), FOREIGN KEY (testid) REFERENCES test(testid))")
	c.execute("CREATE TABLE tdeplink (tdepid INTEGER PRIMARY KEY, testid INTEGER NOT NULL, depid INTEGER DEFAULT 0, FOREIGN KEY (testid) REFERENCES test(testid), FOREIGN KEY (depid) REFERENCES dept(depid))")
	c.execute("CREATE TABLE docdeplink (docdepid INTEGER PRIMARY KEY, docid INTEGER NOT NULL, depid INTEGER DEFAULT 0, FOREIGN KEY (docid) REFERENCES doctor(docid), FOREIGN KEY (depid) REFERENCES dept(depid))")
	c.execute("CREATE TABLE trdeplink (trdepid INTEGER PRIMARY KEY, trid INTEGER NOT NULL, depid INTEGER DEFAULT 0, FOREIGN KEY (trid) REFERENCES treatment(trid), FOREIGN KEY (depid) REFERENCES dept(depid))")

def cleardb():
	os.system("rm medical.db")

def ins_into_patient(pval):
	c.execute("INSERT INTO patient(name,weight,height,bloodgrp,city,phoneno,dob) VALUES (?,?,?,?,?,?,?)",pval)
	conn.commit()
def ins_into_dept(pval):
	c.execute("INSERT INTO dept(depname) VALUES (?)",pval)
	conn.commit()
def ins_into_test(pval):
	c.execute("INSERT INTO test(name, reldis) VALUES (?,?)",pval)
	conn.commit()
def ins_into_doctor(pval):
	c.execute("INSERT INTO doctor(dname,dphoneno,spec,explevel) VALUES (?,?,?,?)",pval)
	conn.commit()
def ins_into_treatment(pval):
	c.execute("INSERT INTO treatment(name,avsuccess,reldis) VALUES (?,?,?)",pval)
	conn.commit()

def ins_into_trplink(pval):
	c.execute("INSERT INTO trplink(pid,successrate,trid) VALUES (?,?,?)",pval)
	conn.commit()
def ins_into_tplink(pval):
	c.execute("INSERT INTO tplink(testid,pid) VALUES (?,?)",pval)
	conn.commit()
def ins_into_tdeplink(pval):
	c.execute("INSERT INTO tdeplink(testid,depid) VALUES (?,?)",pval)
	conn.commit()
def ins_into_docdeplink(pval):
	c.execute("INSERT INTO docdeplink(docid,depid) VALUES (?,?)",pval)
	conn.commit()
def ins_into_trdeplink(pval):
	c.execute("INSERT INTO trdeplink(trid,depid) VALUES (?,?)",pval)
	conn.commit()

def select_all_patient():
	c.execute("SELECT * from patient")
	return c
def select_all_dept():
	c.execute("SELECT * from dept")
	return c
def select_all_test():
	c.execute("SELECT * from test")
	return c
def select_all_treatment():
	c.execute("SELECT * from treatment")
	return c
def select_all_doctor():
	c.execute("SELECT * from doctor")
	return c

def select_all_trp():
	c.execute("SELECT patient.pid, height, weight, bloodgrp, successrate, age, treatment.name, avsuccess, reldis FROM trplink INNER JOIN patient ON trplink.pid=patient.pid INNER JOIN treatment ON trplink.trid=treatment.trid")
	return c
def select_all_tp():
	c.execute("SELECT patient.pid, height, weight, bloodgrp, age, test.name, reldis FROM tplink INNER JOIN patient on tplink.pid=patient.pid INNER JOIN test on tplink.testid=test.testid")
	return c
def select_all_tdep():
	c.execute("SELECT depname, test.name, reldis FROM tdeplink INNER JOIN dept ON tdeplink.depid=dept.depid INNER JOIN test on tdeplink.testid=test.testid")
	return c
def select_all_docdep():
	c.execute("SELECT dname, spec, explevel, depname FROM docdeplink INNER JOIN doctor on docdeplink.docid=doctor.docid INNER JOIN dept on docdeplink.depid=dept.depid")
	return c
def select_all_trdep():
	c.execute("SELECT depname, name, avsuccess, reldis FROM trdeplink INNER JOIN dept on trdeplink.depid=dept.depid INNER JOIN treatment on trdeplink.trid=treatment.trid")
	return c

'''cli input'''
def cli_patient_input():
	print("INPUT PATIENT name, weight, height, bloodgrp, city, phoneno, dob")
	p=[]
	for i in range(7):
		x=input()
		p.append(x)
	ins_into_patient(p)
def cli_dept_input():
	print("INPUT DEPARTMENT depname")
	p=[]
	for i in range(1):
		x=input()
		p.append(x)
	ins_into_dept(p)
def cli_test_input():
	print("INPUT TEST name,related disease")
	p=[]
	for i in range(2):
		x=input()
		p.append(x)
	ins_into_test(p)
def cli_doctor_input():
	print("INPUT DOCTOR name,phone no,specialization,expertise level [1-10]")
	p=[]
	for i in range(4):
		x=input()
		p.append(x)
	ins_into_doctor(p)
def cli_treatment_input():
	print("INPUT TREATMENT name,average success rate,related disease")
	p=[]
	for i in range(3):
		x=input()
		p.append(x)
	ins_into_treatment(p)

def cli_trp_input():
	x=select_all_patient()
	print("PATIENT ID\tPATIENT NAME")
	for i in x:
		print(i[0], end='\t')
		print(i[1])
	x=select_all_treatment()
	print("TREATMENT ID\tTREATMENT NAME")
	for i in x:
		print(i[0], end='\t\t|\t')
		print(i[1])
	print("INPUT PATIENT ID,success rate FOR PATIENT,TREATMENT ID")
	p=[]
	for i in range(3):
		x=input()
		p.append(x)
	ins_into_trplink(p)

def cli_tp_input():
	x=select_all_patient()
	print("PATIENT ID\tPATIENT NAME")
	for i in x:
		print(i[0], end='\t\t|\t')
		print(i[1])
	x=select_all_test()
	print("TEST ID\tTEST NAME")
	for i in x:
		print(i[0], end='\t\t|\t')
		print(i[1])
	print("INPUT test id, PATIENT ID")
	p=[]
	for i in range(2):
		x=input()
		p.append(x)
	ins_into_tplink(p)

def cli_tdep_input():
	x=select_all_department()
	print("DEPT ID\tDEPT NAME")
	for i in x:
		print(i[0], end='\t\t|\t')
		print(i[1])
	x=select_all_test()
	print("TEST ID\tTEST NAME")
	for i in x:
		print(i[0], end='\t\t|\t')
		print(i[1])
	print("INPUT test id,dept id")
	p=[]
	for i in range(2):
		x=input()
		p.append(x)
	ins_into_tdeplink(p)

def cli_docdep_input():
	print("DOCTOR ID\tDOCTOR NAME")
	for i in x:
		print(i[0], end='\t\t|\t')
		print(i[1])
	x=select_all_department()
	print("DEPT ID\tDEPT NAME")
	for i in x:
		print(i[0], end='\t\t|\t')
		print(i[1])
	print("INPUT doctor id,dept id")
	p=[]
	for i in range(2):
		x=input()
		p.append(x)
	ins_into_docdeplink(p)

def cli_trdep_input():
	x=select_all_department()
	print("DEPT ID\tDEPT NAME")
	for i in x:
		print(i[0], end='\t\t|\t')
		print(i[1])
	x=select_all_treatment()
	print("TREATMENT ID\tTREATMENT NAME")
	for i in x:
		print(i[0], end='\t\t|\t')
		print(i[1])
	print("INPUT TREATMENT id,dept id")
	p=[]
	for i in range(2):
		x=input()
		p.append(x)
	ins_into_trdeplink(p)


