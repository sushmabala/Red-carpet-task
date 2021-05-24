import datetime
import random
import string
import uuid

from passlib.handlers.pbkdf2 import pbkdf2_sha256

from app import model as md
from app import pg_db
# from pg_db import database,users,pg_db.engine
def generate_hashedPassword(password):
    return pbkdf2_sha256.hash(password)


def verify_hashedPassword(password, hash):
    return pbkdf2_sha256.verify(password, hash)

def login(username,password):
    res=pg_db.engine.execute('SELECT username,token FROM users where username =%(username)s and password =%(token)s',{"username":username, "token":password}).fetchone()
    if res!=None:
        return  1

def addtoken(username):
    token=id_generator()
    pg_db.engine.execute("UPDATE users SET token=%(token)s WHERE username=%(username)s",{"username":username, "token":token})
    return token

def checktoken(username,token,):
    print("jh")
    res=pg_db.engine.execute('SELECT username,token FROM users where username =%(username)s and token =%(token)s',{"username":username, "token":token}).fetchone()
    #res=pg_db.engine.execute("SELECT username,token FROM users where username ='superadmin' and token ='super123' ")
    print(res)
    if res!=None:
        return 1

def failure():
    ins= {
        "payload":0,
        "Status": "Failure",
    }
    return  ins

def superadmin():
    res=pg_db.engine.execute("select count(*) from users")
    for r in res:
        if r[0]==0:
            pg_db.engine.execute("INSERT INTO users (id,username, password, role,create_at,token) VALUES ('1','superadmin', 'super123', 'admin','2021-05-04T05:43:57.844+00:00','xfghjiukn')")


def isAgent(name):
    res=pg_db.engine.execute('SELECT username,token FROM users where username =%(username)s and role=%(token)s',{"username":name, "token":"agent"}).fetchone()
    print(res)
    if res is not None:
        return 1
def addRelation(agent_username,customer_username):
    gID   = str(uuid.uuid1())
    gDate =str(datetime.datetime.now())
    pg_db.engine.execute("INSERT INTO relation (id,agent_username, customer_username,create_at) VALUES (%(id)s,%(agent_username)s, %(customer_username)s, %(gDate)s)",{"id":gID, "agent_username":agent_username,"customer_username":customer_username,"gDate":gDate})

def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def uniqueUsername(username):
    res=pg_db.engine.execute('SELECT username FROM users ').fetchall()
    usernameList=[]
    print(res)
    for r in res:
        print(r[0])
        usernameList.append(r[0])
    if username not in usernameList:
        return 1

def gethashedpassword(username):
    res=pg_db.engine.execute('SELECT password FROM users where username =%(username)s ',{"username":username}).fetchone()
    return res[0]

def checkRelation(customerName,AgentName):
    res=pg_db.engine.execute('SELECT agent_username,customer_username FROM relation where agent_username =%(username)s and customer_username =%(token)s',{"username":AgentName, "token":customerName}).fetchone()
    print(res)
    if res!=None:
        return 1

def loanvalidation(amount,duration,rm1,rm2,emi):
    if not (amount>50000 and amount<1000000):
        return False
    if not (duration>12 and duration<60):
        return False
    if not emi==True:
        return False
    if not rm1=='PAN_CARD':
        return False
    if not rm2=='SALARY_SLIP':
        return False
    return True

def approveloan(id,status):
    pg_db.engine.execute("UPDATE loan SET status=%(token)s WHERE id=%(username)s",{"username":id, "token":status})
    return

def findRole(username):
    res=pg_db.engine.execute('SELECT role FROM users where username =%(username)s ',{"username":username}).fetchone()
    return res[0]

def statuscheck(id):
    res=pg_db.engine.execute('SELECT status FROM loan where id =%(id)s',{"id":id}).fetchone()
    print(res)
    for r in res:
        if r=="new":
            return 1

def editloan(loan_cutomer_id,agent_username,customer_username,amount,duration,emi,manreq1,manreq2):
    pg_db.engine.execute("UPDATE loan SET agent_username=%(agent)s,customer_username=%(customer)s,amount=%(amt)s,duration=%(dur)s,emi_chosen=%(emi)s,mandatory_requirement1=%(man1)s,mandatory_requirement2=%(man2)s WHERE id=%(id)s",{"id":loan_cutomer_id,"agent":agent_username,"customer":customer_username,"amt":amount,"dur":duration,"emi":emi,"man1":manreq1,"man2":manreq2})
    return
