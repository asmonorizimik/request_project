import requests
import json


def get_saral_url(link):
	res = requests.get(link)
	return res.text
response_text = get_saral_url("http://saral.navgurukul.org/api/courses")

data = json.loads(response_text)
coursesList = (data['availableCourses'])

def Available_courses():
	courses_index = 0
	while courses_index < len(coursesList):
		cousre_name = coursesList[courses_index]["name"]
		courses_id = coursesList[courses_index]["id"]
		print(courses_index +1,cousre_name,courses_id)
		courses_index = courses_index + 1
Available_courses()
print()

def available_course_id():
	id_list = []
	course_name = []
	id_index = 0  
	while id_index < len(coursesList):
		id_list.append(coursesList[id_index]['id'])
		course_name.append(coursesList[id_index]['name'])
		id_index = id_index + 1

	user_id = int(input("enter the id no: ")) -1
	course_id = id_list[user_id]
	print("your course id is ",course_id)
	print(course_name[user_id])
	secondApi = "https://saral.navgurukul.org/api/courses" + "/" +str(id_list[user_id])+ "/" + "exercises"
	restext = get_saral_url(secondApi)
	dic_data = json.loads(restext)
	return ([dic_data["data"],id_list[user_id]])

idlistdata = available_course_id()
id_listdata = (idlistdata[0])
user_id = (idlistdata[1])

print("\n")

def parentchildExercise(list_data):
	parent_index = 0
	while parent_index < len(list_data):
		parent_Exercise = list_data[parent_index]['name']
		childExerciseslist = list_data[parent_index]['childExercises']
		print(parent_index+1,parent_Exercise)
		child_index = 0
		while child_index < len(childExerciseslist):
			if "parent_exercise_id" in childExerciseslist[child_index]:
				print(5*" ", child_index+1,"-", childExerciseslist[child_index]['name'])
			child_index = child_index + 1
		parent_index = parent_index + 1
parentchildExercise(id_listdata)	


exercise = int(input("enter the exercise no: ""\n"))

def id_single_data():
	exercise_index = 0
	Slug_list = []
	while exercise_index < len(id_listdata):
		parent_Exercise = id_listdata[exercise]['name']
		parent_slug = id_listdata[exercise]['slug']
		Slug_list.append(parent_slug)
		childExerciseslist = id_listdata [exercise]['childExercises']
		print(exercise_index,parent_Exercise)
		child_index2 = 0
		while child_index2 < len(childExerciseslist):
			if "parent_exercise_id" in childExerciseslist[child_index2]:
				child_slug = childExerciseslist[child_index2]['slug']
				Slug_list.append(child_slug)
				print(" ",child_index2+1,"-", childExerciseslist[child_index2]['name'])
			child_index2 = child_index2 + 1
		break
	return [Slug_list]
selected_data = id_single_data()
slug_list = selected_data[0]
content = int(input("enter the exercise no to get the content: "))
print("CONTENT","\n")

def third_api():
	third_api = "http://saral.navgurukul.org/api/courses/" + str(user_id) + "/" + "exercise/getBySlug?slug=" + str(slug_list[content])
	text_content = get_saral_url(third_api)
	dict_type_slug = json.loads(text_content)
	print(dict_type_slug['content'],"\n")
third_api()

for i in range(len(slug_list)):
	pre_next = input("enter the 'n' for next and 'p' previous: ")
	if pre_next == "n":
		content = content+1
		if content < len(slug_list):
			third_api()
		else:
			print(":( sorry.......your page is not  found")
			break
		print("\n")

	elif pre_next == "p":
		content = content-1
		if content >= 0:
			third_api()
		else:
			print("page not found")
			break
		print("\n")
	else:
		print("invalid input")
		break