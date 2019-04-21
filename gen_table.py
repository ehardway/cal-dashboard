import json
import pendulum


class gen_table:
    content_file = ''
    days = []
    table_body = ''
    content = {}
    table_data = {}

    def __init__(self, content_file, days):
        self.content_file = content_file
        self.days = days
        self.build_table_data()

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
                self.table_data[key].append({'bgcolor':  day_data[1]['bgcolor']})
        print(self.table_data)
