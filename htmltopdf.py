
with open('check.txt', 'r') as inf:
    for line in inf:
        link = line.strip()
        if line:
            try:
                print (link)
                op=link.split('/bgm')[1].strip('/')+".pdf"
                print("op is"   +  op)
                config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
                pdfkit.from_url(link, op,configuration=config)
            except ValueError:
                print("Could not parse '{0}'".format(link))