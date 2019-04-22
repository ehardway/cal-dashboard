import json


class gen_table:
    content_file = ''
    days = []
    table_row0 = []
    table_row1 = []
    table_row2 = []
    table_row3 = []
    table_row4 = []
    table_row5 = []
    content = {}
    table_data = {}

    def __init__(self, content_file, days):
        self.content_file = content_file
        self.days = days
        self.build_table_data()
        self.build_table_body()
        self.display_table()

    @staticmethod
    def save_json(data, file_name):

        try:
            with open(file_name, 'w') as fp:
                json.dump(data, fp)
        except (FileNotFoundError, FileExistsError, IOError) as err:
            print(err)

    @staticmethod
    def load_json(file_name):

        try:
            with open(file_name, 'r') as fp:
                return json.load(fp)
        except (FileExistsError, IOError) as err:
            print(err)

    def build_table_data(self):
        self.content = dict(self.load_json(self.content_file))
        for day in self.content.keys():
            for day_data in self.content[day].items():
                key = str(day) + ":" + str(day_data[0])
                self.table_data[key] = []
                if day_data[1]['function'] == 'date':
                    for days in self.days:
                        if str(days.format('dddd')).lower() == day.lower():
                            text = str(days.format('DD-MMM')) + "<br>" + str(days.format('dddd'))
                            self.table_data[key].append({'text': text})
                elif day_data[1]['function'] == 'info':
                    self.table_data[key].append({'text': day_data[1]['text']})
                self.table_data[key].append({'bgcolor': day_data[1]['bgcolor']})

    def build_table_body(self):
        for table_data in self.table_data.items():
            if ":0" in table_data[0]:
                self.table_row0.append(self.build_td(table_data[1]))
            elif ":1" in table_data[0]:
                self.table_row1.append(self.build_td(table_data[1]))
            elif ":2" in table_data[0]:
                self.table_row2.append(self.build_td(table_data[1]))
            elif ":3" in table_data[0]:
                self.table_row3.append(self.build_td(table_data[1]))
            elif ":4" in table_data[0]:
                self.table_row4.append(self.build_td(table_data[1]))
            elif ":5" in table_data[0]:
                self.table_row5.append(self.build_td(table_data[1]))

    def build_row(self, table_row):
        row = ''
        for cell in table_row:
            row = row + cell
        return row

    def build_td(self, td_data):
        cell = "<td bgcolor=" + td_data[1]['bgcolor'] + ">"
        cell = cell + td_data[0]['text']
        cell = cell + "</td>"
        return cell

    def display_table(self):
        print("<table border=1 width=100%>")

        print("<tr height=25%>")
        print("<td></td>")
        for table_row in self.table_row0:
            print(self.build_row(table_row))
        print("</tr>")

        print("<tr height=25%>")
        print("<td>1</td>")
        for table_row in self.table_row1:
            print(self.build_row(table_row))
        print("</tr>")

        print("<tr height=25%>")
        print("<td>2</td>")
        for table_row in self.table_row2:
            print(self.build_row(table_row))
        print("</tr>")

        print("<tr height=25%>")
        print("<td>3</td>")
        for table_row in self.table_row3:
            print(self.build_row(table_row))
        print("</tr>")

        print("<tr height=25%>")
        print("<td>4</td>")
        for table_row in self.table_row4:
            print(self.build_row(table_row))
        print("</tr>")

        print("<tr height=25%>")
        print("<td>5</td>")
        for table_row in self.table_row5:
            print(self.build_row(table_row))
        print("</tr>")

        print("</table>")

