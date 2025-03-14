

import csv
import os
from collections import Counter


class CustomerRecord:
    def __init__(self,customer_id,name,email,purchase_amount):
        self.error_count = []
        self.name = name.strip()
        self.email = email.strip()
        self.customer_id = customer_id.strip()
        self.purchase_amount = purchase_amount.strip()

    def is_valid(self):
      
        self.error = []  # Reset errors

        try:
            if not self.customer_id.isdigit():
                raise ValueError("Invalid customer_id (must be numeric)")
        except ValueError as e:
            self.error.append(str(e))

        try:
            if not isinstance(self.name, str) or not self.name.strip():
                raise ValueError("Invalid name (cannot be empty)")
        except ValueError as e:
            self.error.append(str(e))

        try:
            if "@" not in self.email or "." not in self.email.split("@")[-1]:
                raise ValueError(f"Invalid email format")
        except ValueError as e:
            self.error.append(str(e))

        try:
            if not self.purchase_amount.replace(".", "").isdigit():
                raise ValueError(f"Invalid purchase_amount: (must be numeric)")
        except ValueError as e:
            self.error.append(str(e))
        try:
            float(self.purchase_amount)
        except ValueError:
            self.error.append("Invalid purchase_amount format")
                
        return not self.error 

    
    def __str__(self):
        return(f"{self.customer_id}, {self.name}, {self.email}, {self.purchase_amount}")

class ErrorHandling:
    def __init__(self):
        self.file_path = os.path.join("Data", "source_data.csv")
        self.valid_counter = 0
        self.error_counter = Counter()
        self.read_file()

    def read_file(self):
        try:
            records = []
            invalid_records = []

            with open(self.file_path, "r", encoding="UTF-8") as file:
                reader = csv.reader(file)

                for row_number, row in  enumerate(reader, start=1):
                    try:
                        if not row or all(col.strip() == "" for col in row):  # Skip empty rows
                            raise IndexError("Empty row")
                        
                        if len(row) != 4:
                            raise ValueError(f"incorrect colum count: Expected 4 got {len(row)}")
                        record = CustomerRecord(*row[:4])
                     

                                           
                  
                        # customer_id,name,email,purchase_amount = row[:4]
                        if record.is_valid():
                            records.append(record)
                            self.valid_counter +=1  
                        else:
                            invalid_records.append((row_number,record.error))
                            self.error_counter.update(record.error)
                    except (IndexError,ValueError) as e:
                        self.error_counter[str(e)] +=1
                    

                for error_type, count in self.error_counter.items():
                    print(f"{error_type}: {count}")
               
                print(f"\nValid Records: {self.valid_counter}")
                print(f"Invalid Records: {sum(self.error_counter.values())}")
                print(f"Total Records Processed: {self.valid_counter + sum(self.error_counter.values())}")
                
            file.close
    

        except FileNotFoundError:
            print("can't found document")
        except Exception as e:
            print(f"Error: {e}")
    
    # def track_error(self,errors):
    #     for error in errors:
    #       self.error_count[error] = self.error_count.get(error,0) + 1

    # def increment_error(self,error_type):
    #     self.error_count[error_type] = self.error_count.get(error_type,0) +1


ErrorHandling()