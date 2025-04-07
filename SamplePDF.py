from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer



def create_pdf(judgeName, courtName, courtLocation, petitionerName, petitionerAddress, petitionerRelativeName, accussedName, accussedAddress, 
               accussedRelativesName, FIRNumber, policeStationName, underSection, NDOH, Place, currentDate, applicantName, councilName, applicationType) :

    # Create a SimpleDocTemplate object
    print ('Application Type: ', applicationType)
    filename = f'{applicationType}.pdf'
    doc = SimpleDocTemplate(filename, pagesize=letter)
    # Get the width and height of the page
    width, height = letter
    
    # Get a sample stylesheet
    styles = getSampleStyleSheet()
    
    # Create a list to hold the PDF elements
    elements = []

    # Application Type
    subTitle = Paragraph("Application to Exemption from Personal Presence", styles['BodyText'])
    elements.append(subTitle)

    # Spacer
    spacer = Paragraph("<br/><br/>", styles['BodyText'])
    elements.append(spacer)

    # Add a title
    title = Paragraph(f"IN THE COURT OF Hon'ble {judgeName} , {courtName}, {courtLocation}", styles['Title'])
    elements.append(title)

    # Spacer
    spacer = Paragraph("<br/><br/>", styles['BodyText'])
    elements.append(spacer)

    # Add a subtitle
    subtitle = Paragraph("In the matter of", styles['BodyText'])
    elements.append(subtitle)

    # Both Parties Info
    data2 = [[petitionerName],
             ['Son/daughter of', petitionerRelativeName],             
              [petitionerAddress]]
    
    table2 = Table(data2)
    table2.setStyle(TableStyle(
        [('ALIGN',(-1,-1),(-1,-1),'LEFT')]
    ))

    data3 = [['Accused'],
             [accussedName],
             ['Son/daughter of', accussedRelativesName],              
             [accussedAddress]
             ]
    
    table3 = Table(data3)
    table3.setStyle(TableStyle(
        [('ALIGN',(-1,-1),(-1,-1),'LEFT')]
    ))

    combinedData = [[table2,' VERSUS ',table3]]
    combinedTable = Table(combinedData)
    elements.append(Spacer(1, 12)) 
    elements.append(combinedTable)

    data4  = [[' ']]
    table4 =  Table(data4)
    table4.setStyle(TableStyle(
        [('ALIGN', (-1,-1), (-1,-1),'LEFT')])
    )
    
    data5 =  [['FIR No: ', FIRNumber],
             ['PS No: ', policeStationName],
             ['Under Section: ', underSection]]
    table5 = Table(data5)
    table5.setStyle(TableStyle(
        [('ALIGN', (-1,-1),(-1,-1),'LEFT')]
    ))
    combinedData1 = [[table4,' ',table5]]
    combinedTable1 = Table(combinedData1)
    elements.append(combinedTable1)

    #Spacer
    elements.append(spacer)
    
    #Subject
    if applicationType == "exemption" :
        Subjects  = Paragraph(f'APPLICATION IN BEHALF OF APPLICANTS : {petitionerName}  <br/>FOR EXEMPTION OF PERSONAL PRESENCE OF MENTIONED CASE.')
        elements.append(Subjects)
        elements.append(spacer)
    if applicationType == "documentRelease" :
        Subjects  = Paragraph(f'APPLICATION IN BEHALF OF APPLICANTS : {petitionerName}  <br/>FOR Document Release.')  
        elements.append(Subjects)
        elements.append(spacer)  
    

    # Story:
    if applicationType == "exemption" :
        body_text = Paragraph(
            "Most Respectfully Showeth :-  <br/>"
            f"1. That the above noted matter is pending trial in this Hon'ble Court and fixed for {NDOH} ... <br/><br/>"
            f"2. That the complainant MS. {petitionerName}  S/O  {petitionerRelativeName} R/O  {petitionerAddress} has instituted above noted proceddings <br/><br/>"
            "3. That the complainant has instituted the present procedding out of malice, ill, will, personal vendetta, grudge and to teach a lesson to the"
            "applicant and entire proceedings is sheer misused and abused of process of law and the same has been instituted with ulterior and oblique motive. <br/><br/>"
            "4. That if the present application is not allowed, then the applicants shall suffer irreparable loss and injury"
            "which cannot be compendated in terms of money and no useful purpose would be served by making them attend to every court date.<br/><br/>"
            "5. That the applicant shall appear before this Hon'ble Court as and whenever this Hon'ble Court direct the "
            " applicant to do so or the time of recording of statement of accussed U/S .... or at the time of deliverance of judgement in the above matter. <br/><br/>"
            "6. That the applicants shall not misuse and abuse the liberty of concession and privilages confirmed by this Hon'ble Court.<br/><br/>"
            "7. That the applicants are ready to abide by any condition laid down by this Hon'ble Court. <br/><br/>",
            styles['BodyText']
        )
        elements.append(body_text)
        elements.append(spacer)


    if applicationType == "documentRelease" :
        body_text = Paragraph(
            "Most Respectfully Showeth :-  <br/>"
            f"1. That the above noted matter is filled trial in this Hon'ble Court and fixed for {NDOH} ... <br/><br/>"
            f"2. That the complainant MS. {petitionerName}  S/O  {petitionerRelativeName} R/O  {petitionerAddress} has instituted above noted proceddings <br/><br/>"
            f"3. That the complainant has instituted the present procedding. As a advocate of {petitionerName} require to read the case therefore i need document release from the custody. <br/><br/>"
            "4. That if the present application is not allowed, then the applicants shall suffer irreparable loss and injury dwu to unavailablity of document."
            "which cannot be compendated in terms of money and no useful purpose would be served by making them attend to every court date.<br/><br/>"
            "5. That the applicant shall appear before this Hon'ble Court as and whenever this Hon'ble Court direct the "
            " applicant to do so or the time of recording of statement of accussed U/S .... or at the time of deliverance of judgement in the above matter. <br/><br/>"
            "6. That the applicants shall not misuse and abuse the liberty of concession and privilages confirmed by this Hon'ble Court.<br/><br/>"
            "7. That the applicants are ready to abide by any condition laid down by this Hon'ble Court. <br/><br/>",
            styles['BodyText']
        )         
        elements.append(body_text)
        elements.append(spacer)

    # Prayer
    PrayerHeader = Paragraph("Prayer ", styles['Title'])
    elements.append(PrayerHeader) 
    Prayer = Paragraph("It is, therefore, most respectfully prayed that this Honourable Court may kindly be pleased to: <br/>"
                        "a. Allow the applicants be exempted from personal presence on all dates of the trial for the time being. <br/>"
                        "b. Pass any other order which this Honourable Court deem fit and proper under the abovesaid facts and circumstances of the case.<br/>", styles['BodyText'])
    elements.append(Prayer)


    # Add some space between elements
    spacer = Paragraph("<br/><br/>", styles['BodyText'])
    elements.append(spacer)

    # End Notes

    data6 = [['Place: ',Place],
             ['Dated: ', currentDate]]
    
    table6 = Table(data6)
    table6.setStyle(TableStyle(
        [('ALIGN',(-1,-1),(-1,-1),'LEFT')]
    ))

    data7 = [['Applicants: ', applicantName ],
             ['Council: ', councilName]
             ]
    
    table7 = Table(data7)
    table7.setStyle(TableStyle(
        [('ALIGN',(-1,-1),(-1,-1),'LEFT')]
    ))

    combinedData6 = [[table6,' THROUGH ',table7]]
    combinedTable6 = Table(combinedData6)
    elements.append(Spacer(1, 12)) 
    elements.append(combinedTable6)

    # Build the PDF
    doc.build(elements)

# if __name__ == "__main__":
#     create_pdf("enhanced_hello_world.pdf")