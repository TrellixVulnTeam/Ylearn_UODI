from resources.modules.ylearnmodules import *

def study_(subject, classId):
    subject = request.args.get('subject')
    classId = request.args.get('class')

    classId = int(classId)

    if classId <= 4:
        classId = '4'
    elif classId <= 7:
        classId = '5'

    if subject == 'Math':
        dbpath = '/lessons/math.db3'
    elif subject == 'Eng':
        dbpath = '/lessons/english.db3'
    elif subject == 'Sst':
        dbpath = '/lessons/sst.db3'
    elif subject == 'Sci':
        dbpath = '/lessons/science.db3'
    
    lessons = getLessonData(subject, dbpath, classId)
    print(type(classId))
    return render_template('ChildDashboard/lesson.html', lessons = lessons, subject=subject, child = getChild(session.get('user')))