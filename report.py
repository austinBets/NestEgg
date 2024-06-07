from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate, Paragraph, Spacer, Image, PageTemplate, Frame
import os

def generate_pdf_report(filename, graphFileName, df, age, retirementAge):
    # Create a document template
    doc = SimpleDocTemplate(filename, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()
    body_style = styles['BodyText']

    # Add title
    title_style = styles['Title']
    elements.append(Paragraph("The Power of Compound Interest", title_style))

    # Add the line graph plot
    elements.append(Spacer(1, 12))
    img = Image(graphFileName, width=500, height=300)
    elements.append(img)

    #Add analysis on the graph
    finalYear = df['Year'].iloc[-1]
    finalAmountSaved = df ['End of Year Balance'].iloc[-1]
    analysis = f"If you are currently {age} and, you expect to retire when you are {retirementAge}. You will be saving for {retirementAge-age}. You will retire in the year <b>{finalYear}</b> with an expected balance of <b>{finalAmountSaved}</b>. This number is assuming you recieved a <b>3%</b> raise every year and your yearly rate of return was <b>9%</b>"
    elements.append(Paragraph(analysis,body_style))

    # Add the DataFrame as a table
    elements.append(Spacer(1, 12))
    elements.append(Paragraph('Interest Compounded Yearly', title_style))
    elements.append(Spacer(1, 12))

    # Convert DataFrame to list of lists
    data = [df.columns.to_list()] + df.values.tolist()

    #calculate column width
    numCols = len(data[0])
    colWidth = 500 / numCols
    colWidths = [colWidth] * numCols

    # Create a table
    table = Table(data, colWidths=colWidths)
    
    # Add style to the table
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])
    table.setStyle(style)

    elements.append(table)
    
    # Build the PDF
    doc.build(elements)

    # Remove the temporary plot file
    os.remove(graphFileName)
