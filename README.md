# outlook_to_vcard
# csv to vcf from Outlook russian version 
Example: python3 convert.py filename
Result in filename.vcf

format birthday not tested, only cut zero date.

i used delemiter as [;] if you need change it.
30 reader = csv.reader(source, delimiter=';', quotechar='"') # csv.DictReader
