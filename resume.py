print("Ask Me Anything")
i = int(input(''' 1 : For Name Profile : 
 2 : For Carier Objective : 
 3 : For Skills : 
 4 : For Education :
 6 : For Projects :
 7 : For Language :'''))

if(i == 1):
    print("Vighnesh Madankar From Narkhed Dist- Nagpur, Mob ~ 787553455, ")

elif(i == 2):
    print("Objetive : Dedicated and enthusiastic software engineer with a strong foundation in computer science and a passion for IT Technology. Seeking an entry-level position to apply my programming skills and contribute to innovative projects.")

elif(i == 3):
    print('''Skills
Programming Languages: Python
Database: Mysql
IDEs: Visual Studio Code, Eclipse, Web Development: HTML, CSS, JavaScript
Operating Systems: Windows, Linux
Other Tools: Microsoft Office Suite''')
    
elif( i == 4):
    print('''Education
2021/12 – 2024/01 Bangalore, KA, IN MCA
Jain University Bangalore
80.4%
2018/06 – 2021/09 Amravati, MH, IN BCA
Sant Gadge Baba Amravati University
69.36%''')
    
elif(i == 5):
    print("""Certificates
>> Responsive Web Design
>> Splunk for Security Analytics and Monitoring
>> AWS Cloud Practitioner Essentials certification
>> Excel Essential Training (Office 365/Microsoft 365) (LinkedIn)""")

elif(i == 6):
    print('''Projects
Python Scripting Project - Reverse Shell Development
Developed a reverse shell for remote access to Windows 10 systems.
Implemented features for port scanning and keylogging.
Year: 2023
Final Project BCA - Responsive Website on Pollution
Designed and developed a responsive website addressing environmental pollution.
Utilized HTML, CSS, and JavaScript technologies.
Role: Web Developer
Year: 2021
Hiding Text in an Image - Python Script
Created a GUI-based Python script using steganography to hide text within images and extract hidden text.
Demonstrated proficiency in Python scripting and data securit
Year: 2024''')

elif(i == 7):
    print('''English ~ Read, Write, Speak
Hindi ~ Read, Write, Speak
Marathi ~ Read, Write, Speak''')


else:
    print("please enter correct opption")
