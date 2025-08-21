import time

tm = time.localtime()

print(f"{tm =}")
print(f"{tm.tm_year =}")
print(f"{tm.tm_mon =}")
print(f"{tm.tm_mday =}")
print(f"{tm.tm_hour =}")
print(f"{tm.tm_min =}")
print(f"{tm.tm_yday =}")

#working on day var
day: int = tm.tm_mday
mounth: int = tm.tm_mon
year: int = tm.tm_year
hour: int = tm.tm_hour
minit: int = tm.tm_min

isLeap = (year % 4 == 0) and (year % 100 !=0) and (year % 400 != 0)
print(f"{year} is a leap year - {isLeap}")
print(f"Date {day}/{mounth}/{year}, Time {hour}:{minit:0>2}")


day = 0
def yday(mounth):
    days_Per_Month = [31,28,31,30,31,30,31,31,30,31,30,31]
    if mounth > 1:#ignore 
        for i in range(mounth-2): # first -1 is so that we count the first day of the mounth second -1 = -2 is so we dont count this mounth
            days += days_Per_Month[i]
    return days
accumlated_Days = [31,59,90,120,151,181,212,243,273,304,334,365]
if mounth > 1:
    days = accumlated_Days[mounth -2]



