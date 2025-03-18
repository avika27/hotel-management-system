import mysql.connector as mys

def all1():
    print('----------------------------------------')
    gid=int(input('enter the guest id'))
    cur.execute(('select * from guests where guest_id ={}').format(gid))
    i=cur.fetchone()
    row=cur.rowcount
    if row>0 and row>(-1):
        print('\n \t GUEST DETAILS ')
        print('First name - ',i[1])
        print('Last name - ',i[2])
        print('Check in date - ',i[3])
        print('Check out date - ',i[4])
        print('room no - ',i[5])
        print('Email - ',i[6])
        print('Phone Number - ',i[7])        
    else:
        print('record not found')
def addg():
    print('----------------------------------------')
    gid=int(input('Enter Guest id'))
    f=input('Enter First name')
    l=input('Enter Second name')
    r=int(input('Enter Room no'))
    cin=input('Enter Check in date')
    cout=input('Enter Check out date')
    email=input('Enter Email')
    p=input('Enter Phone Number')
    cur.execute(('insert into guests values({},"{}","{}","{}","{}",{},"{}","{}")').format(gid,f,l,cin,cout,r,email,p))
    mycon.commit()
    print('data added')
def remg():
    print('----------------------------------------')
    gid=input('enter eid')
    cur.execute(('delete from guests where guest_id={}').format(gid))
    mycon.commit()
    print('data cleared')
def upg():
    while True:
        print('----------------------------------------')
        print('\n \t \t Press 1 to Change First name')
        print('\n \t \t Press 2 to Change Last name')
        print('\n \t \t Press 3 to Change Check out date')
        print('\n \t \t Press 4 to Change Email')
        print('\n \t \t Press 5 to Change Phone no')
        print('\n \t \t Press 6 to Exit')
        print('----------------------------------------')
        choice=int(input('Enter the choice - '))
        if choice==1:
            gid=input('Enter guest id - ')
            fn=input('Enter new name - ')
            qu=("update guests set first_name='{}' where guest_id={}").format(fn,gid)
            cur.execute(qu) 
            mycon.commit()
            print('data changed')
        elif choice==2:
            gid=input('enter guest id - ')
            ln=input('enter new name - ')
            cur.execute(("update guests set last_name='{}' where guest_id={}").format(ln,gid))
            mycon.commit()
            print('data changed')
        elif choice==3:
            gid=input('Enter guest id - ')
            coutn1=input('Enter new check out date - ')
            cur.execute(('update guests set check_out_date="{}" where guest_id={}').format(coutn1,gid))
            mycon.commit()
            print('data changed')
        elif choice==4:
            gid=input('Enter guest id - ')
            en=input('Enter new email - ')
            cur.execute(('update guests set email="{}" where guest_id={}').format(en,gid))
            mycon.commit()
            print('data changed')
        elif choice==5:
            gid=input('Enter guest id - ')
            pn=input('Enter new phone - ')
            cur.execute(('update guests set phone_number="{}" where guest_id={}').format(pn,gid))
            mycon.commit()
            print('Data changed')
        elif choice==6:
            break 
        else:
            print('invalid')
        o=input('do you want to continue y or n')
        if o in 'nN':
            break
    
def upe():
    while True:
        print('----------------------------------------')
        print('\n \t \t Press 1 to Change First Name')
        print('\n \t \t Press 2 to Change last name')
        print('\n \t \t Press 3 to Change Position')
        print('\n \t \t Press 4 to Change Deptartment')
        print('\n \t \t Press 5 to Change Salary')
        print('\n \t \t Press 6 to Change Email')
        print('\n \t \t Press 7 to Change Phone no')
        print('\n \t \t press 8 to Exit')
        print('----------------------------------------')
        choice=int(input('enter the choice - '))
        if choice==1:
            eid=input('Enter employee id - ')
            fn=input('Enter new name - ')
            cur.execute(('update employees set first_name="{}" where employee_id="{}"').format(fn,eid))
            mycon.commit()
            print('Data changed')
        elif choice==2:
            eid=input('Enter employee id - ')
            ln=input('Enter new name - ')
            cur.execute(('update employees set last_name="{}" where employee_id="{}"').format(ln,eid))
            mycon.commit()
            print('Data changed')
        elif choice==3:
            eid=input('Enter employee id - ')
            pn=input('Enter position - ')
            cur.execute(('update employees set position="{}" where employee_id="{}"').format(pn,eid))
            mycon.commit()
            print('Data changed')
        elif choice==4:
            eid=input('Enter employee id - ')
            dn=input('Enter dept - ')
            cur.execute(('update employees set department="{}" where employee_id="{}"').format(dn,eid))
            mycon.commit()
            print('Data changed')
        elif choice==5:
            eid=input('Enter employee id - ')
            sn=input('Enter new sal - ')
            cur.execute(('update employees set salary={} where employee_id="{}"').format(sn,eid))
            mycon.commit()
            print('Data changed')
        elif choice==6:
            eid=input('Enter employee id - ')
            emn=input('Enter new email - ')
            cur.execute(('update employees set email="{}" where employee_id="{}"').format(emn,eid))
            mycon.commit()
            print('Data changed')
        elif choice==7:
            eid=input('Enter employee id - ')
            pn=input('Enter new phone - ')
            cur.execute(('update employees set phone_number="{}" where employee_id="{}"').format(pn,eid))
            mycon.commit()
            print('Data changed')
        elif choice==8:
             break
        else:
            print('inavlid')
        c1=input('do you want to continue y or n')
        if c1 in 'nN':
            break
    
def alle():
    print('----------------------------------------')
    eid=input('enter the employee id')
    cur.execute(('select * from employees where employee_id ="{}"').format(eid))
    i=cur.fetchone()
    row=cur.rowcount
    if row>0 and row>(-1):
        print('\n \t EMPLOYEE DETAILS ')
        print('First name - ',i[1])
        print('Last name - ',i[2])
        print('Position - ',i[3])
        print('Department - ',i[4])
        print('Hire daye - ',i[5])
        print('Salary - ',i[6])
        print('Email - ',i[7])
        print('Phone Number - ',i[8])
    else:
        print('record not found')
def dele():
    print('----------------------------------------')
    eid=input('enter eid')
    cur.execute(('delete from employees where employee_id="{}"').format(eid))
    mycon.commit()
    print('data cleared')
def adde():
    print('----------------------------------------')
    eid=input('enter eid')
    f=input('first name')
    l=input('second name')
    p=input('position')
    dept=input('enter dept')
    hire=input('enter hire date')
    sal=int(input('enter sal'))
    email=input('enter email')
    p=input('phone number')
    cur.execute(('insert into employees values("{}","{}","{}","{}","{}","{}",{},"{}","{}")').format(eid,f,l,p,dept,hire,sal,email,p))
    mycon.commit()
    print('data added')



front='y'            
while True:
    cont='y'
    print('----------------------------------------')
    print('\t \t Press 1 for guest ')
    print()
    print('\t \t Press 2 for employee')
    print('\n \t \t press 3 to exit ')
    print('----------------------------------------')
    ch=int(input('enter your choice = '))
    if ch==1:
        mycon=mys.connect(host='localhost',user='root',passwd='root',database='hotel')
        cur=mycon.cursor()
        while True:
            print('----------------------------------------')
            print('\n \t \t Press 1 for Guest Details')            
            print('\n \t \t Press 2 to Add Guest')            
            print('\n \t \t Press 3 to Remove Guest')
            print('\n \t \t Press 4 to Change details of Guest')
            print('\n \t \t Press 5 to Exit')
            print('----------------------------------------')
            c=int(input('enter your choice ='))
            
            print('----------------------------------------')
            
            if c==1:
                all1()
            elif c==2:
                addg()
            elif c==3:
                remg()
            elif c==4:
                upg()
                
            elif c==5:
                break
                
            else:
                print('invalid')
                
            cont=input('\ndo you want to continue y or n')
            if cont=='n':
                break           
    elif ch==2:
        mycon=mys.connect(host='localhost',user='root',passwd='root',database='hotel')
        cur=mycon.cursor()
        while True:
            print('----------------------------------------')
            print('\n \t \t Press 1 for Details of Employee')
            print('\n \t \t Press 2 to Remove a Employee')
            print('\n \t \t Press 3 add a New Employee')
            print('\n \t \t Press 4 to change Details of Employee')
            print('\n \t \t Press 5 to Exit')
            print('----------------------------------------')
            c2=int(input('enter  choice - '))
            if c2==1:
                alle()
            elif c2==2:
                dele()
            elif c2==3:
                adde()
            elif c2==4:
                upe()
            elif c2==5:
                break
            else:
                print('invalid')
            print()
            p=input('do you want to continue y or n')
            if p in 'nN':
                break
            
    elif ch==3:
        break
    else:
        print('invalid')
                
        

        
        

            
            

            
                
