cities = ["Atlanta", "Baltimore", "Chicago", "Denver", "Los Angeles", "Seattle"]
cities.append("New York") 
cities = cities + ["Dubuque", "New Orleans"] 
longer_list_of_cities = cities + ["Dubuque", "New Orleans"] 
todays_tasks = []
todays_tasks = todays_tasks + ["Walk dog", "Buy groceries"] 
cities.insert(0, "New York") 
cities.insert(2, "Dallas") 
smaller_list_of_cities = cities[2:5]
tasks = ["email Frank", "call Sarah", "meet with Zach"] 
del tasks[0] 
del tasks[1] 
tasks.remove("call Sarah") 
tasks = ["email Frank", "call Sarah", "meet with Zach"]
latest_task_accomplished = tasks.pop(0) 
tasks_accomplished = []
tasks_accomplished.append(latest_task_accomplished)
# tasks_accomplished.append(tasks.pop(1)) 
tasks_accomplished.insert(1, tasks.pop(1))
latest_task_accomplished = tasks.pop()
city_to_check = "Tucson"
cleanest_cities = ["Cheyenne", "Santa Fe", "Tucson", "Great Falls", "Honolulu"]
for a_clean_city in cleanest_cities:
    if city_to_check == a_clean_city:
        print("It's one of the cleanest cities")
        break

first_names = ["BlueRay ", "Upchuck ", "Lojack ", "Gizmo ", "Do-Rag "]
last_names = ["Zzz", "Burp", "Dogbone", "Droop"]
full_names = []
for a_first_name in first_names:
    for a_last_name in last_names:
        full_names.append(a_first_name + " " + a_last_name)

city_to_check = input("Enter your city: ")
city_to_check = city_to_check.lower()
cleanest_cities = ["cheyenne", "santa fe", "tucson", "great falls", "honolulu"] 
for a_clean_city in cleanest_cities:
    if city_to_check == a_clean_city:
        city_to_check = city_to_check.title()
        print("Great news! " + city_to_check + " is one of the cleanest cities.")  

for a_clean_city in cleanest_cities:
    print(a_clean_city) 

customer_29876 = {"first name": "David", "last name": "Elliott", "address": "4803 Wellesley St."} 
address_of_customer = customer_29876["address"] 
customer_29876["city"] = "Toronto"
# del customer_29876["address"] 

for each_value in customer_29876.values():
    print(each_value) 

for each_key in customer_29876.keys():
    print(each_key) 

for each_key, each_value in customer_29876.items():
    print("The customer's " + each_key + " is " + each_value) 

things_to_remember = { 
    0: "the lowest number",
    "a dozen": 12,
    "snake eyes": "a pair of ones",
    13: "a baker's dozen",
}

customers = [
    {
        "customer id": 0,
        "first name":"John",
        "last name": "Ogden",
        "address": "301 Arbor Rd.",
    },
    {
        "customer id": 1,
        "first name":"Ann",
        "last name": "Sattermyer",
        "address": "PO Box 1145",
    },
    {
        "customer id": 2,
        "first name":"Jill",
        "last name": "Somers",
        "address": "3 Main St.",
    },
] 
new_first_name = "hamza"
new_last_name = "khan"
new_address =  "pk"
new_customer_id = len(customers)

new_dictionary = {
        "customer id": new_customer_id,
        "first name": new_first_name,
        "last name": new_last_name,
        "address": new_address,
}

customers.append(new_dictionary)







