# To Split a .csv File to multiple .csv files
# Applications: When we have Computational Power Constraints, we can use .csv file in parts.
# Also, to view large .csv files but with "not so good GPU/CPU" and many more.

def split_csv_file(filename, lines_per_file):
    with open(filename, 'r') as file:
        header = file.readline()
        file_count = 1
        for i, line in enumerate(file, start=1):
            if i % lines_per_file == 1:
                if file_count > 1:
                    out_file.close()
                out_filename = f"{filename.rsplit('.', 1)[0]}_{file_count}.csv"
                out_file = open(out_filename, 'w')
                out_file.write(header)
                file_count += 1
            out_file.write(line)
        out_file.close()


# Add the Path of File which is to be Split
file_path = ""

# Add the Rows per After split .csv file would contain
rows_per_file = 100

# Calling the Function to Split .csv to Multiple .csv files
split_csv_file(file_path, rows_per_file)