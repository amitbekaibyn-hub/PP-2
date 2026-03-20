s={"symbat":80,"samat":70,"aibyn":90}
for key,value in s.items():
    if value>=95:
        print("Gpa 4.0")
    elif value<=95 and value>=90:
        print("Gpa 3.67")
    elif value<=90 and value>=85:
        print("Gpa 3.33")
    elif value<=85 and value>=80:
        print("Gpa 3.0")
    elif value<=80 and value>=75:
        print("Gpa 2.67")
    elif value<=75 and value>=70:
        print("Gpa 2.33")
    else:
        print("retak")