def camel_case(string):
   string.strip()
   arr = string.split(" ")
   for i in range(len(arr)):
       arr[i] = arr[i].capitalize()  
   return "".join(arr)




print(camel_case("this is a test conversion"))