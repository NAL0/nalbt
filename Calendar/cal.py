import calendar
import os

u = calendar.monthcalendar(2019, 3)

try:
    
    os.makedirs('templates')
    os.makedirs("templates/Calendar")
    os.makedirs("templates/Calendar/includes")
except Exception as e:
    pass

finally:
    sf = open('templates/Calendar/includes/Calendar2.html','a', encoding = 'utf-8')
    for lis in u:
        sf.write("<tr>\n")
        for unit in lis:
                sf.write("<td>"+ str(unit)+ "</td>\n")

        sf.write("</tr>\n")

    sf.close()
