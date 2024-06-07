import matplotlib.pyplot as plt

def create_lineGraph(years, amountSaved):

    #create a new figure and axis object
    fig, ax = plt.subplots()

    #plot the data
    ax.plot(years, amountSaved, marker='o', markerfacecolor='lightblue',color='black')

    #Name axis
    ax.set_xlabel('Years')
    ax.set_ylabel('Balance (in Millions of $)')
    
    #add grid lines
    ax.grid(True)

    plot_filename = "plot.png"
    fig.savefig(plot_filename, format='png')


