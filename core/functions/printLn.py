def printLn(current_token):
        for i in range(len(current_token.get("value"))):
            print(current_token.get("value")[i].get("value"), end="")
        
        print(current_token.get("args").get("endsWith").get("value"), end="")