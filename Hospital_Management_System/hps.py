#Hospital Management System

class patient:

    def admit(self):
        name=input("Patient name ")
        id_no=int(input("Enter patient id "))
        ward_no=int(input("Enter ward no "))
        date=input("Enter date of admission ")
        doctor=input("Enter doctor name ")
        disease=input("Enter disease ")
        status=input("Enter status ")
        patient_info={"Patient name":name, "Id no":id_no, "Ward no":ward_no, "Disease type":disease, "Date of admission":date, "Doctor responsible":doctor, "status":status}
        patients[id_no]=patient_info
        
    def search(self):
        ch = int(input("Search By:\n 1.Name \n 2.Id \n 3.Ward number \n 4.Disease Type\n"))
        if ch == 1:
            name1=input("Enter name to be searched ")
            for i in patients.keys():
                if patients[i]['Patient name']==name1:
                    print(patients[i])
                    break
                else:
                    print("no entry of that patient")
                    break
        if ch ==2:
            idn=int(input('Enter the id.no to be searched '))
            for i in patients.keys():
                if patients[i]['Id no'] == idn:
                    print(patients[i])
                    break
                else:
                    print('no entry of that patient')
                    break
            
        if ch==3:
            w = int(input('Enter the ward.no to be searched '))
            for i in patients.keys():
                if patients[i]['Ward no'] == w:
                    print(patients[i])
                    break
                else:
                    print('no entry of that patient')
                    break
            
        if ch==4:
            dis = input('Enter the disease type to be searched ')
            for i in patients.keys():
                if dis in patients[i]['Disease type']:
                    print(patients[i])
                    break
                else:
                    print('no entry of that disease')
                    break
            
    
    def display(self):
        print(f"no.of patients admitted in hospital : {len(patients)}")
        for j in patients.keys():
            print(f"{patients[j]}\n")
            
def discharge(n):
    for i in list(patients.keys()):
        if patients[i]['Id no'] == n:
            del patients[i]
        else:
            print("wrong id no")
            break


patients={}
obj=patient()

while True:
    c=int(input("""\nEnter Choice  
1.Admit new Patient 
2.Discharge Patient 
3.Search Record
4.Display status of each ward
5.Exit 
"""))
    if c==1:
        obj.admit()
        
    elif c==2:
        x = int(input('Enter the id.no to be discharged '))
        discharge(x)
        
    elif c==3:
        obj.search()
        
        
    elif c==4:
        obj.display()
        
        
    elif c==5:
        exit(0)
        break
    else:
        print('Enter correct choice')
        break