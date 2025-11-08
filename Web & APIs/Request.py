# Python Requests Library - Basic Core Example
import requests

# # Basic GET request
# response = requests.get('https://httpbin.org/get')
# print(f"Status Code: {response.status_code}")
# print(f"Content: {response.text[:100]}...")

# # Understanding the response
# if response.status_code == 200:
#     print("Success!")
# elif response.status_code == 404:
#     print("Page not found")
# else:
#     print(f"Something else: {response.status_code}")

import json
# dump/load to string
'''s = json.dumps({'a':1,'b':2},indent=2)
obj=json.loads(s)
print(s)
print(obj)'''

# dump/load to file
'''with open('data.json','w') as f:
    json.dump(obj,f,indent=2)
with open("data.json") as f:
    data = json.load(f)
    print(data)
'''


# GET Request - Retrieve data from a server
# res = 'https://api.github.com/users/octocat'
# get_res = requests.get(res)
# print(f"status code : {get_res.status_code}")
# print(f"response body : {get_res.json()}")
# print(f"response headers : {get_res.headers}")
# print(f"Response Text:{get_res.text[:200]}...\n") # first 200 chars

# # Understanding the response
# if get_res.status_code == 200:
#     print(" Successful!\n")
# elif get_res.status_code == 404:
#     print("Resource Not Found!\n")
# else:
#     print(f"Something went wrong! Status Code: {get_res.status_code}\n")

# POST Request - Send data to a server
# post_url = 'https://httpbin.org/post'
# data = {'name': 'John', 'age': 30}
# post_res = requests.post(post_url,json=data)
# print(f"POST Status Code : {post_res.status_code}")
# print(f"POST Response Body : {post_res.json()}\n")

# PUT Request - Update data on a server
# put_url = 'https://httpbin.org/put'
# update_data = {'name': 'Jane', 'age': 25}
# put_res = requests.put(put_url, json=update_data)
# print(f"PUT Status Code : {put_res.status_code}")
# print(f"PUT Response Body : {put_res.json()}\n")

# DELETE Request - Remove data from a server
# delete_url = 'https://httpbin.org/delete'
# delete_res = requests.delete(delete_url)
# print(f"DELETE Status Code : {delete_res.status_code}")
# print(f"DELETE Response Body : {delete_res.json()}\n")

# GET with Headers & Parameters
# Headers	= Metadata like User-Agent, authentication, etc.
# Params =  Query parameters (?q=python&sort=stars) passed in a GET request

# search_url = 'https://api.github.com/search/repositories'
# headers = {'User-Agent': 'My-App/1.0'}
# params = {'q':"python",'sort':'stars'}

# search_res = requests.get(search_url, headers=headers, params=params)

# print("Search Status Code :", search_res.status_code)
# # json.dumps() — converts Python dict to readable JSON text , indent - Number of spaces used for indentation when pretty-printing JSON
# print("Search Response Body :", json.dumps(search_res.json(), indent=2)) 
