import pandas as pd
import graphs
import table
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate, Paragraph, Spacer, Image
import os

def generate_pdf_report(filename, graphFileName, title, df):
    # Create a document template
    doc = SimpleDocTemplate(filename, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()
    body_style = styles['BodyText']

    # Add title
    title_style = styles['Title']
    elements.append(Paragraph(title, title_style))

    # Add content
    content = """
This is a sample PDF report generated using Python and ReportLab.
It includes a line graph generated using Matplotlib and a table from a pandas DataFrame.
"""
    elements.append(Paragraph(content, body_style))
    elements.append(Spacer(1, 12))

    # Add the plot image
    elements.append(Spacer(1, 12))
    elements.append(Paragraph('Line Graph:', title_style))
    elements.append(Spacer(1, 12))
    img = Image(graphFileName, width=500, height=300)
    elements.append(img)

    #Add analysis on the graph
    final_year = df['Year'].iloc[-1]
    final_amount_saved = df ['Amount Saved'].iloc[-1]
    analysis = f"Looking over this information you will be saving funds for a total of {final_year} years. At the end of the final year the amount you will have saved is saved is <b>${final_amount_saved:,.2f}</b>."
    elements.append(Paragraph(analysis,body_style))

    # Add the DataFrame as a table
    elements.append(Spacer(1, 12))
    elements.append(Paragraph('Data Table:', title_style))
    elements.append(Spacer(1, 12))

    # Convert DataFrame to list of lists
    data = [df.columns.to_list()] + df.values.tolist()

    # Create a table
    table = Table(data)
    
    # Add style to the table
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])
    table.setStyle(style)

    elements.append(table)
    
    # Build the PDF
    doc.build(elements)

    # Remove the temporary plot file
    os.remove(graphFileName)

# Example usage
# filename = "report_with_graph_and_table.pdf"
# title = "Sample Report with Graph and Table"
# content = """
# This is a sample PDF report generated using Python and ReportLab.
# It includes a line graph generated using Matplotlib and a table from a pandas DataFrame.
# """
# x_data = np.linspace(0, 10, 100)
# y_data = np.sin(x_data)

# year = [1,2,3,4,5,6,7,8,9,10,11,12]
# amountSaved = [10000,20000,30000,40000,50000,60000,70000,80000,90000,100000,110000,120000]

# dataframe = table.createPandasDataframe(year, amountSaved)

# # Generate the plot and save it as an image file
# graphs.create_lineGraph(year, amountSaved)
# graphFileName = "plot.png"

# generate_pdf_report(filename, graphFileName, title, content, dataframe)