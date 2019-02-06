import pandas

def to_exel(data):
    email_data = pandas.DataFrame(
        data,
        columns=['Name', 'Address', 'Mail']
        )
    file = 'emails.xlsx'
    writer = pandas.ExcelWriter(file)
    email_data.to_excel(writer, "Sheet1")
    writer.save()





