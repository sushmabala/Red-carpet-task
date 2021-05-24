from pydantic import BaseModel, Field


class UserList(BaseModel):
    id        : str
    username  : str
    password  : str
    first_name: str
    last_name : str
    gender    : str
    create_at : str
    status    : str

class UserEntry(BaseModel):
    username  : str
    password  : str
    role:str
    refUser:str
    reftoken:str

class loginEntry(BaseModel):
    username  : str
    password  : str

class loanEntry(BaseModel):
    customer_username  : str
    agent_username: str
    amount:int
    duration:int
    mandatory_requirement1:str
    mandatory_requirement2:str
    emi_chosen:bool

class approveloan(BaseModel):
    admin_username: str
    admin_token: str
    loan_cutomer_id:str
    status:str

class ViewCustomerLoan(BaseModel):
    customer_username  : str
    token  : str

class ViewLoan(BaseModel):
    username  : str
    token  : str

class ViewadminFilterLoan(BaseModel):
    admin_username  : str
    admin_token  : str


class UserListchecl(BaseModel):
    role       : str
    username  : str

class UserListcheclAgent(BaseModel):

    agent_username: str
    customer_username:str


class editloan(BaseModel):
    id:str
    customer_username  : str
    agent_username: str
    amount:int
    duration:int
    mandatory_requirement1:str
    mandatory_requirement2:str
    emi_chosen:bool
    admin_username:str
    admin_token:str





