
import datetime
def timelist(start, end):
    timearray = []
    delta = datetime.timedelta(minutes=30)
    start = datetime.datetime.strptime( start, '%H:%M' )
    end = datetime.datetime.strptime( end, '%H:%M' )
    t = start
    while t <= end :
        timearray.append( datetime.datetime.strftime( t, '%H:%M'))
        t += delta
    return ','.join(timearray)




