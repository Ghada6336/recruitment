def main():
	
        print("Welcome to the special recruitment program, please answer the following questions:")       
        skills = ["Python", "C++", "JavaScript", "Meeting", "Leeting", "Eating"]
        cv={}
        cv["name"] =input('What is your name?')
        cv["age"]= int(input ('How old are you?'))
        cv["experience"]= int(input ('How many years of experience do you have?'))
        cv["skills"]=[]

        for num, skill in enumerate(skills,1):
                print (num, skill)
                
       
        
                
                
        n=int(input('Choose another skill from above by entering its number:'))
        cv["skills"].append(skills[n-1])
                
        print (cv)
        m=int(input('Choose another skill from above by entering its number:'))
        cv["skills"].append(skills[m-1])
        print (cv)      
       
                
                
        if (cv["age"]>=25 and cv["age"]<=40 and cv["experience"]>5 )and ( "Eating" in cv["skills"])  :
            print ("accepted")
        else:
            print ("rejected")
        
        
                 
                 
                

if __name__ == '__main__':
	main()
