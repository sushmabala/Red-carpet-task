# Red-CarpetUp-Task

The backend is made with Python Fastapi and uvicorn.
Postgres is used as a database.


Features :
1. List, view and edit users -  this can only be done by "agent" and "admin" roles
2. Create a loan request on behalf of the user -  This can only be done by "agent" role. Loan can have 3 states - "NEW", "REJECTED", "APPROVED".
3. Approval of loan request - This can only be done by an "admin" role.
4. Edit a loan (but not after it has been approved) -  This can be done only by "agent" role. But cannot be done if loan is in "Approved" state.
5. Ability to list and view loans  based on the filter applied. "customer" can only see his own loans .
6. Agent" and Admin can see everyone's loans filterd by date of loanRequest in descending.
7. Admin can view the loan filterd by approved and rejected 

<h2> Admin Registration <h2>
  
![1adminRegister](https://user-images.githubusercontent.com/67327058/117583175-556b5000-b123-11eb-8f23-15a2274c9894.png)

<h2> Admin Login <h2>
  
![2adminLogin](https://user-images.githubusercontent.com/67327058/117583176-5603e680-b123-11eb-804a-a2231c9cf28e.png)

<h2> Agent Registration <h2>
  
![3agentRegister](https://user-images.githubusercontent.com/67327058/117583177-569c7d00-b123-11eb-9a9d-7eeb74c0df2c.png)

<h2> Agent Login <h2>
  
![4agentLogin](https://user-images.githubusercontent.com/67327058/117583178-569c7d00-b123-11eb-8796-22a3f97f710f.png)

<h2> User Registration <h2>
  
![5userRegister](https://user-images.githubusercontent.com/67327058/117583179-57351380-b123-11eb-9edb-1b0cbca85476.png)

<h2> User Login <h2>
  
![6userLogin](https://user-images.githubusercontent.com/67327058/117583181-57cdaa00-b123-11eb-8733-e53502864c18.png)

<h2> Add Loan <h2>
  
![7addLoan](https://user-images.githubusercontent.com/67327058/117583182-57cdaa00-b123-11eb-88fa-e9c7b279a6eb.png)

<h2> Customer View Loan Request <h2>
  
![8CustomerViewLonRequest](https://user-images.githubusercontent.com/67327058/117583161-4f756f00-b123-11eb-8d58-b68dcb7d5700.png)

<h2> Edit Loan Request <h2>
  
![9editLoanRequest](https://user-images.githubusercontent.com/67327058/117583163-50a69c00-b123-11eb-8ba8-31d720c828d3.png)

<h2> Customer View Loan Request - After Update <h2>
  
![10CustomerViewLonRequestAfterUpdate](https://user-images.githubusercontent.com/67327058/117583164-513f3280-b123-11eb-9871-16476a6ebfe4.png)

<h2> Loan Approval <h2>
  
<h4>Loan can be aproved only by admin</h4>

![11LoanAproval](https://user-images.githubusercontent.com/67327058/117583165-513f3280-b123-11eb-8637-68cd66c7fe2c.png)

<h2> Customer View Loan Request - After Approval <h2>
  
![12CustomerViewLonRequestAfterAproval](https://user-images.githubusercontent.com/67327058/117583166-51d7c900-b123-11eb-8882-088d665ae319.png)

<h2> Loan Can't be edited <h2>

<h4>Loan can't be edited after approval</h4>

![13LoanCan'tBeEdited](https://user-images.githubusercontent.com/67327058/117583167-52705f80-b123-11eb-9032-959d7710ee36.png)

<h2> View Approved <h2>
  
<h4>admin can view the approved  Loans</h4>

![14ViewApproved](https://user-images.githubusercontent.com/67327058/117583168-52705f80-b123-11eb-8699-4bdadde472a6.png)

<h2> View Rejected <h2>
  
<h4>Admin can view the Rejected Loans</h4>

![15ViewRejected](https://user-images.githubusercontent.com/67327058/117583169-5308f600-b123-11eb-8469-66c0024f984e.png)

<h2> View Loans - Admin <h2>

<h4>admin can view the  Loans details filtered by time in descending</h4>

![16ViewLoansAdmin](https://user-images.githubusercontent.com/67327058/117583170-53a18c80-b123-11eb-9481-8e7f7ae881f8.png)

<h2> View Loans - Agent <h2>

<h4>Agent can view the Loans details of the customer under the respective agent and filtered by time in descending</h4>

![17ViewLoansAgent](https://user-images.githubusercontent.com/67327058/117583171-543a2300-b123-11eb-9622-b554576d6580.png)

<h2> View User - Admin <h2>

<h4>Admin can view all the agent and users</h4>

![19ViewUserAdmin](https://user-images.githubusercontent.com/67327058/117583172-543a2300-b123-11eb-9cde-309452a0fc1d.png)

<h2> View User Agent <h2>
<h4>Agent  can view the customers under the respective agent</h4>

![20ViewUserAgent](https://user-images.githubusercontent.com/67327058/117583173-54d2b980-b123-11eb-8357-71905f4f870e.png)




