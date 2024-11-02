import pandas as pd
import io


def create_excel_file(sheet_name: str, df: pd.DataFrame):
    '''
    Create an excel file by a pandas dataframe
    '''
    # Generate a sample DataFrame
    # df = pd.DataFrame({
    #     'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    #     'Age': [24, 27, 22, 32],
    #     'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
    # })

    # Save the DataFrame to an Excel file in memory
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name=sheet_name)
    output.seek(0)  # Move to the beginning of the stream

    return output
