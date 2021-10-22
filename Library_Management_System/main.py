//library Management System
def add_book():
    name=input("Enter book Title: ")
    auth=input("Enter author name: ")
    genre=input("Enter book genre : ")
    status=input("Enter status: ")
    dic={"Name":name,"Author ":auth,"Genre ":genre,"Status ":status}
    li_dic.append(dic)
    
def rem_book():
    n=int(input("Enter the book number you want to delete: "))
    print(li_dic[n-1])
    del li_dic[n-1]
    print("Deleted.")

def issue_book():
    n=int(input("Enter the book number : "))
    d=li_dic[n-1]
    del d["Status "]
    d['Status']="Issued"
    print(d)
    print("Done")

def ret_book():
    n=int(input("Enter the book number : "))
    d=li_dic[n-1]
    del d["Status"]
    d['Status']="Returned"
    print(d)
    print("Done")

def display():
    print("List of Books: ")
    n=0
    for ele in li_dic:
        n=n+1
        print(n)
        print(','.join(['{0} : {1}  '.format(k,v) for k,v in ele.items()]))

def search():
    name1=input("Enter name to be searched : ")
    for ele in li_dic:
        name2=ele.get('Name')
        if name1 == name2:
            print(ele)


li_dic=[]
while(True):
    choice= input("Please select from the following menu: \n"
                  "To Add Book enter    :1\n"
                  "To remove book enter :2\n"
                  "To issue book enter  :3\n"
                  "To return book enter :4\n"
                  "To display book list :5\n"
                  "To search book       :6\n"
                  "Enter your choice:  ")
    if choice =="1":
        add_book()
    if choice =="2":
        rem_book()
    if choice =="3":
        issue_book()
    if choice =="4":
        ret_book()
    if choice =="5":
        display()
    if choice =="6":
        search()


