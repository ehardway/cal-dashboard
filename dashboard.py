import pendulum

dt = pendulum.now()

mon = dt.start_of('week')
tue = mon.add(days=1)
wed = mon.add(days=2)
thu = mon.add(days=3)
fri = mon.add(days=4)
sat = mon.add(days=5)
sun = mon.add(days=-1)

days = [
    sun,
    mon,
    tue,
    wed,
    thu,
    fri,
    sat
]

# Header of the table
header = '<tr>\n'

for day in days:
    header = header + "<th>" + str(day.format('DD-MMM')) + "<br>" + str(day.format('dddd')) + "</th>\n"

header = header + "</tr>\n"

# Body of table
table_body =  ''

for rows in days:
    table_body = table_body + "<tr>"
    for day in days:
        table_body = table_body + "<td height=50> Next Level </td>"
    table_body = table_body + "</tr>"


table_head = "<table border=1 width=100%>\n"
table_end = "</table>\n"

print(table_head + header + table_body + table_end)

