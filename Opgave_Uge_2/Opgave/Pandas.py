import os
import pandas as pd

class PandasProcessing:
    def __init__(self):
        self.file_path = os.path.join("Data", "DKHousingPricesSample100k.csv")
        self.df = None
        self.read_csv_file()

    def read_csv_file(self):
        try:
      
            try:
                self.df = pd.read_csv(self.file_path, encoding="utf-8", engine="python")
            except UnicodeDecodeError:
                print("\n⚠️ UTF-8 failed. Trying ISO-8859-1...")
                self.df = pd.read_csv(self.file_path, encoding="ISO-8859-1", engine="python")
            print(self.df.head(10))
            
            if "region" in self.df.columns:
                region_counts = self.df["region"].value_counts()

                print(region_counts)
            else:


            if "region" in self.df.columns and "purchase_price" in self.df.columns:
                self.df["purchase_price"] = pd.to_numeric(self.df["purchase_price"])
    

                # avg_price_region = avg_price_region
                avg_price_region = self.df.groupby("region")["purchase_price"].mean()
                avg_price_region = avg_price_region.apply(lambda x: f"{x:,.2f} DK")
                print(avg_price_region)
            

            

        except FileNotFoundError:
            print("Error: File not found.")
        except Exception as e:
            print(f"Unexpected error: {e}")


PandasProcessing()

