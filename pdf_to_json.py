import pdfplumber
import pandas as pd

def extract_tables_from_pdf(filename):
    tables = []
    try:
        with pdfplumber.open(filename) as pdf:
            for page in pdf.pages:
                # Extract table assuming tables with borders
                table = page.extract_table()
                print(table)
                if table:
                    tables.append(table)
        return tables
    except Exception as e:
        print(f"Error opening PDF file: {e}")
        return None
    

    # def save_tables_as_csv(tables, filename):
    # base_filename = filename.split('.')[0]
    # for i, table in enumerate(tables):
    #     header = table[0]
    #     data = table[1:]
    #     df = pd.DataFrame(data, columns=header)
    #     csv_filename = f"{base_filename}_table_{i+1}.csv"
    #     df.to_csv(csv_filename, index=False, encoding='utf-8-sig')
    #     print(f"Saved table {i+1} as {csv_filename}")


    # if __name__ == "__main__":
filename = r"HSBC.pdf"  # Replace with your PDF file
tables = extract_tables_from_pdf(filename)
print("tables")