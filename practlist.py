coursestodo = ['BTECH','MTECH',"BCOMP.HONS","BBA","MASTERS"]
print("Courses available:",coursestodo)
print()
coursedone  = []
while True:
    course = input('Select the Course from above list:')
    coursedone.append(str.upper(course))
    print('You have completed',coursedone,'Course.','\n','Number of you have completed  courses' ,len(coursedone))
    print()
    coursestodo.remove(str.upper(course))
    print()
    print('Number of courses left',coursestodo,'\n',len(coursestodo),"Courses are left.")
    