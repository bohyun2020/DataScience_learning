def explore_data(dataset, start, end, rows_and_columns=False):
    data_slice = dataset[start:end]
    for row in data_slice:
        print(row)
        print('\n') # add a new (empty) line after each row

    if rows_and_columns:
        print(f'The number of rows: {len(dataset)}')
        print(f'The number of columns: {len(dataset[0])}')


