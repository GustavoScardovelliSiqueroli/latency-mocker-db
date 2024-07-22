import csv
import os


class CsvService:

    @staticmethod
    def get_next_test_id(csv_path):
        next_id = 1

        if os.path.exists(csv_path) and os.path.getsize(csv_path) > 0:
            with open(csv_path, 'r') as csvfile:
                reader = csv.reader(csvfile)
                next(reader, None)
                for row in reader:
                    try:
                        current_id = int(row[0])
                        if current_id >= next_id:
                            next_id = current_id + 1
                    except ValueError:
                        pass
        return next_id

    @staticmethod
    def data_to_csv(data: dict):
        print(data)
        csv_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '../..', 'result.csv'))

        next_test_id = CsvService.get_next_test_id(csv_path)

        with open(csv_path, 'a', newline='') as csvfile:
            fieldnames = ['test_id', 'action', 'quantity', 'runtime']
            writer = csv.writer(csvfile)

            if os.path.getsize(csv_path) == 0:
                writer.writerow(fieldnames)

            for x, y in data.items():
                writer.writerow((next_test_id , x, f'{y["quantity"]}', f'"{y["runtime"]}"'))
