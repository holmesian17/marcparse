import pymarc

xml = 'Documents/CatalogRecords/AU_MARC/PGA-Australiana.xml'

def getMarcInfo(record):
    try:
        title = record['245']['a']
    except TypeError:
        title = ''
    try:
        title2 = record['245']['b']
    except TypeError:
        title2 = ''
    try:
        author = record['100']['a']
    except TypeError:
        author = ''
    try:
        authorDates = record['100']['d']
    except TypeError:
        authorDates = ''
    try:
        isbn = record['020']['a']
    except TypeError:
        isbn = ''
    try:
        LCCN = record['050']['a']
    except TypeError:
        LCCN = ''
    try:         
        LCCN2 = record ['050']['b']
    except TypeError:
        LCCN2 = ''
    try:
        dewey = record['082']['a']
    except TypeError:
        dewey = ''
    try:
        placePub = record['260']['a']
    except:
        placePub = ''
    try:
        publisher = record['260']['b']
    except TypeError:
        publisher = ''
    try:
        pubDate = record['260']['c']
    except TypeError:
        pubDate = ''
    try:
        extent = record['300']['a']
    except TypeError:
        extent = ''
    try:
        itemDetails = record['300']['b']
    except TypeError:
        itemDetails = ''
    try:
        dimensions = record['300']['c']
    except TypeError:
        dimensions = ''
    try:
        generalNote = record['500']['a']
    except TypeError:
        generalNote = ''
    try:
        summary = record['520']['a']
    except TypeError:
        summary = ''
    try:
        subjectHeading = record['650']
    except TypeError:
        subjectHeading = ''

    try:    
        print('<record>'+
                '<title>' + title + '</title>' +
                '<author>' + author + '</author>' +
                '<authorDates>' + authorDates + '</authorDates>' +
                '<isbn>' + isbn + '</isbn>' +
                '</record>')
    except TypeError:
        print('')

print('<collection>')
pymarc.map_xml(getMarcInfo, xml)
print('</collection>')
