spam= ['apples', "banans" ,"tofu", "cats"]
def mylistTostring(list):
    result = ""
    for index, item in enumerate(list):
    
        
        if index != len(list)  - 1:
            result = result +  item +  ", " 
        else: 
            result = result + "and " + item

    print(result)


mylistTostring(spam)