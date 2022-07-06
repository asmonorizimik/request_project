import requests
import json,os
print("WELCOME LETS LEARN NAVGURUKUL API COURSES!!\n")
url= 'http://saral.navgurukul.org/api/courses'
try:
    def get_url_link(link):
        if(os.path.isfile("request.json")):
            with open("request.json","r") as file:
                d=json.load(file)
            availCourse=d["availableCourses"]
            return availCourse
        else:
        
            link = requests.get(url)
            x=link.json()
            with open("request.json","w") as f:
                json.dump(x,f,indent=6)

    def coursesList():
        i=0
        availCourse=get_url_link(url)
        while i<len(availCourse):
            courseName=availCourse[i]["name"]
            course_id=int(availCourse[i]["id"])
            print(str(i+1)+":",courseName,course_id)
            i+=1
    coursesList()

    def available_course():
        course_list=get_url_link(url)
        id_list = []
        course_name = []
        i = 0
        while i < len(course_list):
            id_list.append(course_list[i]['id'])
            course_name.append(course_list[i]['name'])
            i+=1
        global id
        id=int(input("enter chapter number between 1 to 200:\n"))-1
        course_id = id_list[id]
        print("your course id is ",course_id)
        print("Course Name:",course_name[id])
        secondApi = "https://saral.navgurukul.org/api/courses" + "/" +str(id_list[id])+ "/" + "exercises"
        link2 = requests.get(secondApi)
        x=link2.json()
        with open("sec_api.json","w") as file1:
            json.dump(x,file1,indent=4)
        with open("sec_api.json","r") as file2:
            exercise=json.load(file2)
        parent_ex=exercise["data"]
        return parent_ex

    def main():
        parentExList=available_course()
        parentExName=[]
        parentExId=[]
        slug_list=[]
        i=0
        print("EXERCISE:-")
        while i<len(parentExList):
            print(" "+str(i+1)+":"+parentExList[i]["name"],parentExList[i]["id"])
            parentExName.append(parentExList[i]["name"])
            slug_list.append(parentExList[i]["slug"])
            parentExId.append(parentExList[i]["id"])
            i+=1
        
        select_exercise=int(input("select exercise number:\n"))-1
        print("Exercise Name: ",parentExName[select_exercise])
        third_api = "http://saral.navgurukul.org/api/courses/" + str(id) + "/" + "exercise/getBySlug?slug=" + str(slug_list[select_exercise])
        link2 = requests.get(third_api)
        x=link2.json()
        with open("third_api.json","w") as file1:
            json.dump(x,file1,indent=4)
        with open("third_api.json","r") as file2:
            exercise=json.load(file2)
        slug_ex=exercise["slug"]
        print("Exercise slug Name:",slug_ex,"\n")
        print("Github link: ",exercise["github_link"],"\n")
        print("CONTENT:-\n")
        content=json.loads((exercise["content"]).strip("\n"))
        print(content[0])
        print("select: 'N' for next chapter:\n'P' for previous:\n'S'(start again)to load the whole content again:")
        def select():
            select=input().upper()
            return select
        def select_opt():
            select1=select()
            for n in range(1,len(slug_ex)):
                if select1=="N" and select1<=slug_ex:
                    n=n+1
                    print("Exercise Name: ",parentExName[n])
                    print("CONTENT:-\n")
                    content=json.loads((exercise["content"]).strip("\n"))
                    print(content[0])
                    select_opt()
                if select1=="P" and select1<=slug_ex:
                    n=n-1
                    print("Exercise Name: ",parentExName[n])
                    print("CONTENT:-\n")
                    content=json.loads((exercise["content"]).strip("\n"))
                    print(content[0]) 
                    select_opt()
                else:
                    print("invalid/page not found")
                    select_opt()            

            if select1=="S":
                main()
            else:
                print("page not found")
                main()
        select_opt()
    main()
except:
    print("\nOpps!!! No internet connection!!! Pliz try again later...")


##checking network error: