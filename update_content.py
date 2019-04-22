import json


class update_content:
    content_file = ''
    content = {}
    changes = {}

    def __init__(self, content_file, change_file):
        self.content_file = content_file
        self.content = self.load_json(content_file)
        self.changes = self.load_json(change_file)
        self.apply_changes()

    def apply_changes(self):
	for changes in self.changes.items():
	    print(changes)

    def display_content(self):
        print(self.content)

    def update_content(self, day, row, key, value):
        self.content[day][str(row)][key] = value

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

content = update_content('content.json','tmp/changes.json')
#content.update_content('sunday', 2, 'text', 'banana')
#content.display_content()
