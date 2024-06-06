import matplotlib.pyplot as plt

def create_lineGraph(years, amountSaved):

    #create a new figure and axis object
    fig, ax = plt.subplots()

    #plot the data
    ax.plot(years, amountSaved, marker='o')

    #set labels and title
    ax.set_xlabel('Years')
    ax.set_ylabel('Balance ($)')
    ax.set_title('Investment Growth Over Time')
    
    #add grid lines
    ax.grid(True)

    plot_filename = "plot.png"
    fig.savefig(plot_filename, format='png')


