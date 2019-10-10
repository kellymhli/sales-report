def print_using_lists(filename):
    """Take in a file object and print sales report."""

    # Generate two lists 
    salespeople = []
    melons_sold = []

    # Parse out the salesperson and number of melons sold from each line
    for line in filename:
        line = line.rstrip() # Remove trailing whitespace
        entries = line.split('|') # Create list of data
        salesperson = entries[0]
        melons = int(entries[2])

        # Add the salesperson's name to one list at a specific index
        # At the same index in melons_sold, log the total melons sold 
        if salesperson in salespeople:
            position = salespeople.index(salesperson)
            melons_sold[position] += melons
        else:
            salespeople.append(salesperson)
            melons_sold.append(melons)

    # Print salesperson and num of melons they sold
    for i in range(len(salespeople)):
        print(f'{salespeople[i]} sold {melons_sold[i]} melons')


def print_using_dict(filename):
    """Take in a file object and print sales report."""

    sales_data = {}

    # Parse out the salesperson and number or melons sold from each line
    for line in filename:
        line = line.rstrip()

        salesperson, total_cost, melons = line.split('|') # Unpack list

        # Add salesperson to and increment melons sold in dictionary
        sales_data[salesperson] = sales_data.get(salesperson, 0)
        sales_data[salesperson] += int(melons)

    # Print salesperson and num of melons they sold
    for person, total_melons in sales_data.items():
        print(f'{person} sold {total_melons} melons')


if __name__ == '__main__':

    # Open file and pass into print_using_dict function
    f = open('sales-report.txt')
    print_using_dict(f)
    f.close()



