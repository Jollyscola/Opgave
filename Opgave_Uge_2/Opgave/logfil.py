import os

# path = "Data/app_log.txt"

# print(os.path.join())

class logfile:

    def __init__(self):
        self.input_path = os.path.join("Data","app_log.txt")
        self.output_path = {
             "Info" : os.path.join("data", "log_info.txt"),
             "Warning": os.path.join("data", "log_warrning.txt"),
             "Error": os.path.join("data","log_error.txt"),
             "Success": os.path.join("data","log_success.txt") 
        }
        self.fileread()

    def  fileread(self):

        try:
            clease_line = []
            categorized_logs = {
                 "Info": [],
                 "Warning": [],
                 "Error": [],
                 "Success": []
            }

            with open(self.input_path,"r",encoding="utf-8") as file:
                    lines = file.readlines()
                    for line in lines:
                        strippe_line = line.strip()
                        if strippe_line:
                            log_type = self.get_log_type(strippe_line)
                           
                            if log_type:
                                # print(categorized_logs[log_type])
                                clease_line.append(strippe_line)
                                categorized_logs[log_type].append(strippe_line)
                    file.close
                    print(clease_line[:10])
                    for log_type, log_line in categorized_logs.items():
                        #  print(log_line)
                         if log_line:
                            with open(self.output_path[log_type], "w", encoding="utf-8") as new_file:
                                   new_file.write("\n".join(log_line) + "\n")
                                   new_file.close
                         print(f"{len(categorized_logs[log_type])} messages saved in: {log_type}")   
                    print(f"amount of saved in all files: {len(clease_line)}")   
           
                

        except FileNotFoundError:
            print("there are no file")                
        except Exception as e:
            print(f"Error {e}") 

    def display_file(self,line):
        if(self.fileread):
              print(line)
        else:
             print("something went wrong")
    def get_log_type(self,line):
            if"INFO" in line:
                return 'Info'
            elif "WARNING" in line:
                 return 'Warning'
            elif "ERROR" in line:
                 return 'Error'
            elif "SUCCESS" in line:
                 return "Success"
            else:
                return None
logfile()
                         
                        

