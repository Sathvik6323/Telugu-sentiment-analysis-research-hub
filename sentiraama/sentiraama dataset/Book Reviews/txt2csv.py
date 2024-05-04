import csv
# Open the input and output files
with open('book_pos.txt', 'r', encoding='utf-8') as infile, open('book_pos.csv', 'w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    
    # Write CSV header
    writer.writerow(['Review', 'Label'])
    
    # Read lines from the input file
    lines = infile.readlines()
    review = ''
    
    # Loop through each line
    for line in lines:
        # Check if the line contains the delimiter
        if '______' in line:
            # Write the review to CSV and reset it
            writer.writerow([review.strip(), '1'])  # Label all reviews as '0'
            review = ''
        else:
            # Append the line to the current review
            review += line.strip() + ' '

    # Write the last review to CSV
    writer.writerow([review.strip(), '1'])  # Label all reviews as '0'
