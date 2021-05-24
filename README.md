# red-carpetUp-Task

The backend is made with Python Fastapi and uvicorn.
Postgres is used as a database.
Docker is used for deployment. 

Features with Screenshots:
1. List, view and edit users -  this can only be done by "agent" and "admin" roles
2. Create a loan request on behalf of the user -  This can only be done by "agent" role. Loan can have 3 states - "NEW", "REJECTED", "APPROVED".
3. Approval of loan request - This can only be done by an "admin" role.
4. Edit a loan (but not after it has been approved) -  This can be done only by "agent" role. But cannot be done if loan is in "Approved" state.
5. Ability to list and view loans  based on the filter applied. "customer" can only see his own loans .
6. Agent" and Admin can see everyone's loans filterd by date of loanRequest in descending.
7. Admin can view the loan filterd by approved and rejected 

# adminRegister
![1adminRegister](https://user-images.githubusercontent.com/67327058/117583175-556b5000-b123-11eb-8f23-15a2274c9894.png)

# adminLogin
![2adminLogin](https://user-images.githubusercontent.com/67327058/117583176-5603e680-b123-11eb-804a-a2231c9cf28e.png)

# agentRegister
![3agentRegister](https://user-images.githubusercontent.com/67327058/117583177-569c7d00-b123-11eb-9a9d-7eeb74c0df2c.png)

# agentLogin
![4agentLogin](https://user-images.githubusercontent.com/67327058/117583178-569c7d00-b123-11eb-8796-22a3f97f710f.png)

# userRegister
![5userRegister](https://user-images.githubusercontent.com/67327058/117583179-57351380-b123-11eb-9edb-1b0cbca85476.png)

# userLogin
![6userLogin](https://user-images.githubusercontent.com/67327058/117583181-57cdaa00-b123-11eb-8733-e53502864c18.png)

# addLoan
![7addLoan](https://user-images.githubusercontent.com/67327058/117583182-57cdaa00-b123-11eb-88fa-e9c7b279a6eb.png)

# CustomerViewLonRequest
![8CustomerViewLonRequest](https://user-images.githubusercontent.com/67327058/117583161-4f756f00-b123-11eb-8d58-b68dcb7d5700.png)

# editLoanRequest
![9editLoanRequest](https://user-images.githubusercontent.com/67327058/117583163-50a69c00-b123-11eb-8ba8-31d720c828d3.png)

# CustomerViewLonRequestAfterUpdate
![10CustomerViewLonRequestAfterUpdate](https://user-images.githubusercontent.com/67327058/117583164-513f3280-b123-11eb-9871-16476a6ebfe4.png)

# LoanAproval
<h4>Loan can be aproved only by admin</h4>

![11LoanAproval](https://user-images.githubusercontent.com/67327058/117583165-513f3280-b123-11eb-8637-68cd66c7fe2c.png)

# CustomerViewLonRequestAfterAproval
![12CustomerViewLonRequestAfterAproval](https://user-images.githubusercontent.com/67327058/117583166-51d7c900-b123-11eb-8882-088d665ae319.png)

# LoanCan'tBeEdited

<h4>Loan can't be edited after aproval</h4>

![13LoanCan'tBeEdited](https://user-images.githubusercontent.com/67327058/117583167-52705f80-b123-11eb-9032-959d7710ee36.png)

# ViewApproved
<h4>admin can view the approved  Loans</h4>

![14ViewApproved](https://user-images.githubusercontent.com/67327058/117583168-52705f80-b123-11eb-8699-4bdadde472a6.png)

# ViewRejected
<h4>admin can view the rejected Loans</h4>

![15ViewRejected](https://user-images.githubusercontent.com/67327058/117583169-5308f600-b123-11eb-8469-66c0024f984e.png)

# ViewLoansAdmin

<h4>admin can view the  Loans details filtered by time in descending</h4>

![16ViewLoansAdmin](https://user-images.githubusercontent.com/67327058/117583170-53a18c80-b123-11eb-9481-8e7f7ae881f8.png)

# ViewLoansAgent

<h4>agent can view the  Loans details of the customer under the respective agent and filtered by time in descending</h4>

![17ViewLoansAgent](https://user-images.githubusercontent.com/67327058/117583171-543a2300-b123-11eb-9622-b554576d6580.png)

# ViewUserAdmin

<h4>admin can view all the agent and users</h4>

![19ViewUserAdmin](https://user-images.githubusercontent.com/67327058/117583172-543a2300-b123-11eb-9cde-309452a0fc1d.png)

# ViewUserAgent
<h4>agent  can view the customers under the respective agent</h4>

![20ViewUserAgent](https://user-images.githubusercontent.com/67327058/117583173-54d2b980-b123-11eb-8357-71905f4f870e.png)

# DataBase Structure
![DB](https://user-images.githubusercontent.com/67327058/117583174-556b5000-b123-11eb-8626-32c01d464dca.png)

# Docker

<h4>sudo docker-compose up</h4>

![DockerRun](https://user-images.githubusercontent.com/67327058/117611801-bf1a4700-b181-11eb-80a2-c6df384ebbf6.jpeg)





