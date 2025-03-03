

import csv
import os


class ErrorHandling:
    def __init__(self):
        self.sound_path = os.path.join("Data", "source_data.csv")
        self.destination_path = os.path.join("Data","destination_data.csv")
        self.readfile()

    def readfile(self):
        try:
            clease_data = []

            with open(self.sound_path, "r", encoding="UTF-8") as file:
                reader = csv.reader(file)

                for row in reader:
                    if any(row):
                        clease_data.append(row)
                print(clease_data)
            file.close
            with open(self.destination_path,"w", encoding="UTF-8") as new_file:
                writer = csv.writer(new_file)
                writer.writerow(clease_data)

        except FileNotFoundError:
            print("can't found document")
        except Exception as e:
            print("Error: " + e)

ErrorHandling()