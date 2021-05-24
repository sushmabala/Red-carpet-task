import datetime
import uuid
from typing import List
import asyncpg
import databases,sqlalchemy
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import FastAPI
from sqlalchemy import desc

from app import model as md
from app.pg_db import database,users,loan,engine
from app import query as q

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()
    q.superadmin()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()



@app.post("/Registerusers")
async def register_user(user: md.UserEntry):

    gID   = str(uuid.uuid1())
    gDate =str(datetime.datetime.now())
    ref_user=user.refUser
    ref_token=user.reftoken
    hashpass=user.password
    hashedpass=q.generate_hashedPassword(hashpass)
    query = users.insert().values(
        id = gID,
        username   = user.username,
        password   = hashedpass,
        create_at  = gDate,
        token     = "",
        role=user.role

    )

    if user.role=="admin":
        if(q.checktoken(ref_user,ref_token)==1):
            await database.execute(query)
            ins= {
                "payload":1,
                "Status": "Success"
            }
            json_compatible_item_data = jsonable_encoder(ins)
            return JSONResponse(content=json_compatible_item_data)
        else:

            json_compatible_item_data = jsonable_encoder(q.failure())
            return JSONResponse(content=json_compatible_item_data)

    if user.role=="customer":
        if q.uniqueUsername(user.username):
            if(q.isAgent(ref_user)==1):
                await database.execute(query)
                q.addRelation(ref_user,user.username)
                ins= {
                    "payload":1,
                    "Status": "Success"
                }
                json_compatible_item_data = jsonable_encoder(ins)
                return JSONResponse(content=json_compatible_item_data)
            else:

                json_compatible_item_data = jsonable_encoder(q.failure())
                return JSONResponse(content=json_compatible_item_data)
        else:
            ins= {"payload":0,"Status": "Failure","error":"Username exists"}
            json_compatible_item_data = jsonable_encoder(ins)
            return JSONResponse(content=json_compatible_item_data)

    if user.role=="agent":
        if(q.checktoken(ref_user,ref_token)==1):
            await database.execute(query)
            ins= {
                "payload":1,
                "Status": "Success"
            }
            json_compatible_item_data = jsonable_encoder(ins)
            return JSONResponse(content=json_compatible_item_data)
        else:

            json_compatible_item_data = jsonable_encoder(q.failure())
            return JSONResponse(content=json_compatible_item_data)
    else:

        json_compatible_item_data = jsonable_encoder(q.failure())
        return JSONResponse(content=json_compatible_item_data)

@app.post("/login")
async def login(user: md.loginEntry):
    username=user.username
    password=user.password
    hash=q.gethashedpassword(username)
    pasw=q.verify_hashedPassword(password,hash)

    if(q.login(username,hash)==1):
        token=q.addtoken(username)
        ins= {
            "payload":1,
            "Status": "Success",
            "Token":token
        }
        json_compatible_item_data = jsonable_encoder(ins)
        return JSONResponse(content=json_compatible_item_data)

    else:

        json_compatible_item_data = jsonable_encoder(q.failure())
        return JSONResponse(content=json_compatible_item_data)

@app.post("/AddLoan")
async def AddLoan(user: md.loanEntry):
    agent_username=user.agent_username
    customer_username=user.customer_username
    amount=user.amount
    duration=user.duration
    emi=user.emi_chosen
    manreq1=user.mandatory_requirement1
    manreq2=user.mandatory_requirement2
    gID   = str(uuid.uuid1())
    gDate =str(datetime.datetime.now())

    query = loan.insert().values(
        id = gID,
        agent_username  = agent_username,
        customer_username  = customer_username,
        create_at  = gDate,
        duration     = duration,
        emi_chosen=emi,
        mandatory_requirement1=manreq1,
        mandatory_requirement2=manreq2,
        amount=amount,
        status="new"
    )
    if(q.checkRelation(customer_username,agent_username)==1):
        if(q.loanvalidation(amount,duration,manreq1,manreq2,emi)):
            await database.execute(query)
            ins= {
                "payload":1,
                "Status": "Success",
            }
            json_compatible_item_data = jsonable_encoder(ins)
            return JSONResponse(content=json_compatible_item_data)
        else:
            ins= {
                "payload":0,
                "Status": "Failure",
                "error":"Validation Fails"
            }
        json_compatible_item_data = jsonable_encoder(ins)
        return JSONResponse(content=json_compatible_item_data)
    else:

        json_compatible_item_data = jsonable_encoder(q.failure())
        return JSONResponse(content=json_compatible_item_data)


@app.post("/approveLoanRequest")
async def approveloan(user: md.approveloan):
    admin_username=user.admin_username
    admin_token= user.admin_token
    loan_cutomer_id=user.loan_cutomer_id
    status=user.status
    state=["Rejected","Approved"]
    if(q.checktoken(admin_username,admin_token)==1):
        if status in state:
            q.approveloan(loan_cutomer_id,status)
            ins= {
                "payload":1,
                "Status": "Success",
            }
            json_compatible_item_data = jsonable_encoder(ins)
            return JSONResponse(content=json_compatible_item_data)
        else:
            ins= {
                "payload":0,
                "Status": "Invalid Approval Status",
            }
        json_compatible_item_data = jsonable_encoder(ins)
        return JSONResponse(content=json_compatible_item_data)

    else:

        json_compatible_item_data = jsonable_encoder(q.failure())
        return JSONResponse(content=json_compatible_item_data)


@app.post("/editLoanRequest")
async def editloan(user: md.editloan):
    loan_cutomer_id=user.id
    agent_username=user.agent_username
    customer_username=user.customer_username
    amount=user.amount
    duration=user.duration
    emi=user.emi_chosen
    manreq1=user.mandatory_requirement1
    manreq2=user.mandatory_requirement2
    gID   = str(uuid.uuid1())
    gDate =str(datetime.datetime.now())
    admin_username=user.admin_username
    admin_token=user.admin_token

    if(q.checktoken(admin_username,admin_token)==1):
        print(1)
        if(q.loanvalidation(amount,duration,manreq1,manreq2,emi)):
            print(2)
            if (q.statuscheck(loan_cutomer_id)==1):
                print(3)
                q.editloan(loan_cutomer_id,agent_username,customer_username,amount,duration,emi,manreq1,manreq2)
                ins= {
                    "payload":1,
                    "Status": "Success",
                }
                json_compatible_item_data = jsonable_encoder(ins)
                return JSONResponse(content=json_compatible_item_data)
            else:
                ins= {
                    "payload":0,
                    "Status": "Cant Edit Approved or Rejected laon",
                }
            json_compatible_item_data = jsonable_encoder(ins)
            return JSONResponse(content=json_compatible_item_data)
        else:
            ins= {
                "payload":0,
                "Status": "Failure",
                "error":"Validation Fails"
            }
        json_compatible_item_data = jsonable_encoder(ins)
        return JSONResponse(content=json_compatible_item_data)

    else:
        json_compatible_item_data = jsonable_encoder(q.failure())
        return JSONResponse(content=json_compatible_item_data)




@app.post("/viewusers/admin",response_model=List[md.UserListchecl])
async def find_users(loans:md.ViewLoan):
    username=loans.username
    token=loans.token
    if(q.checktoken(username,token)==1):
        role=q.findRole(username)
        if role == 'admin':
            query = users.select()
            return await database.fetch_all(query)
        if role=='agent':
            query=engine.execute("select relation.customer_username,users.role from users join relation on relation.agent_username=users.username where relation.agent_username=%(token)s",{ "token":username}).fetchall()
            return (query)
    else:

        json_compatible_item_data = jsonable_encoder(q.failure())
        return JSONResponse(content=json_compatible_item_data)

@app.post("/viewusers/agent",response_model=List[md.UserListcheclAgent])
async def find_usersAgent(loans:md.ViewLoan):
    username=loans.username
    token=loans.token
    if(q.checktoken(username,token)==1):
        role=q.findRole(username)
        if role=='agent':
            query=engine.execute("select relation.customer_username,relation.agent_username,users.role from users join relation on relation.agent_username=users.username where relation.agent_username=%(token)s",{ "token":username}).fetchall()
            return (query)
    else:

        json_compatible_item_data = jsonable_encoder(q.failure())
        return JSONResponse(content=json_compatible_item_data)

@app.post("/loans")
async def find_all_Loans(loans:md.ViewLoan):
    username=loans.username
    token=loans.token
    if(q.checktoken(username,token)==1):
        role=q.findRole(username)
        if role == 'admin':
            query = loan.select().order_by(desc(loan.c.create_at))
            return await database.fetch_all(query)
        elif role=='agent':
            print(12)
            query = loan.select().where(loan.c.agent_username==username).order_by(desc(loan.c.create_at))
            return await database.fetch_all(query)
        else:

            json_compatible_item_data = jsonable_encoder(q.failure())
            return JSONResponse(content=json_compatible_item_data)
    else:

        json_compatible_item_data = jsonable_encoder(q.failure())
        return JSONResponse(content=json_compatible_item_data)

@app.get("/loans/Rejected")
async def find_all_RejectedLoans(loans:md.ViewadminFilterLoan):
    username=loans.admin_username
    token=loans.admin_token
    if(q.checktoken(username,token)==1):
        query = loan.select().where(loan.c.status == 'Rejected')
        return await database.fetch_all(query)
    else:

        json_compatible_item_data = jsonable_encoder(q.failure())
        return JSONResponse(content=json_compatible_item_data)


@app.get("/loans/Approved")
async def find_all_RejectedLoans(loans:md.ViewadminFilterLoan):
    username=loans.admin_username
    token=loans.admin_token
    if(q.checktoken(username,token)==1):
        query = loan.select().where(loan.c.status == 'Approved')
        return await database.fetch_all(query)
    else:

        json_compatible_item_data = jsonable_encoder(q.failure())
        return JSONResponse(content=json_compatible_item_data)
@app.post("/viewCustomerLoanRequest")
async def find_all_viewCustomerLoanReques(loans:md.ViewCustomerLoan):
    username=loans.customer_username
    token=loans.token

    if(q.checktoken(username,token)==1):

        query = loan.select().where(loan.c.customer_username == username)
        return await database.fetch_all(query)
    else:

        json_compatible_item_data = jsonable_encoder(q.failure())
        return JSONResponse(content=json_compatible_item_data)
