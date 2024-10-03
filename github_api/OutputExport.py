import json

class OutputExport:

    @staticmethod
    def export_to_json(content, filename: str):
        filename_with_extension = f'{filename}.json'
        try:
            with open(filename_with_extension, 'w') as json_file:
                json.dump(content, json_file, indent=4, sort_keys=True)
        except OSError as e:
            print('>>> Error exporting to json file ', e)

    @staticmethod
    def export_to_raw(content, filename: str):
        filename_with_extension = f'{filename}.raw'
        try:
            f = open(filename_with_extension, "w")
            f.write(content)
            f.close()
        except OSError as e:
            print('>>> Error exporting to raw file ', e)

    @staticmethod
    def export_bytes(content, filename: str):
        try:
            with open(filename, 'wb') as binary_file:
                binary_file.write(content)
        except OSError as e:
            print('>>> Error exporting to binary file ', e)