import pandas as pd
from datetime import datetime
import os

log_file_path = 'password/log.csv'


def add_log(type, username, status):
    date = datetime.now().strftime('%d/%m/%Y')
    time = datetime.now().strftime('%H:%M:%S')
    
    last_id = 0
    if os.path.exists(log_file_path) and os.path.getsize(log_file_path) > 0:

        df = pd.read_csv(log_file_path)
        last_id = df['id'].max()  


    new_id = int (last_id + 1)
    log_entry = {
        'id': new_id,
        'date': date,
        'time': time,
        'user': username,
        'processus': type,
        'details': status
    }


    log_entry_df = pd.DataFrame([log_entry])


    if os.path.exists(log_file_path) and os.path.getsize(log_file_path) > 0:

        df = pd.read_csv(log_file_path)
        df = pd.concat([df, log_entry_df], ignore_index=True)
    else:

        df = log_entry_df

    df.to_csv(log_file_path, index=False)
    
    return

