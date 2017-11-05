import pymarc

xml = 'Documents/CatalogRecords/AU_MARC/PGA-Australiana.xml'

def getMarcInfo(record):
    try:
        title = record['245']['a']
        if title is None:
            title = ''
    except TypeError:
        title = ''
    try:
        title2 = record['245']['b']
        if title2 is None:
            title2 = ''
    except TypeError:
        title2 = ''
    try:
        author = record['100']['a']
        if author is None:
            author = ''
    except TypeError:
        author = ''
    try:
        authorDates = record['100']['d']
        if authorDates is None:
            author = ''
    except TypeError:
        authorDates = ''
    try:
        isbn = record['020']['a']
        if isbn is None:
            isbn = ''
    except TypeError:
        isbn = ''
    try:
        LCCN = record['050']['a']
        if LCCN is None:
            LCCN = ''
    except TypeError:
        LCCN = ''
    try:         
        LCCN2 = record ['050']['b']
        if LCCN2 is None:
            LCCN2 = ''
    except TypeError:
        LCCN2 = ''
    try:
        dewey = record['082']['a']
        if dewey is None:
            dewey = ''
    except TypeError:
        dewey = ''
    try:
        placePub = record['260']['a']
        if placePub is None:
            placePub = ''
    except:
        placePub = ''
    try:
        publisher = record['260']['b']
        if publisher is None:
            publisher = ''
    except TypeError:
        publisher = ''
    try:
        pubDate = record['260']['c']
        if pubDate is None:
            pubDate = ''
    except TypeError:
        pubDate = ''
    try:
        extent = record['300']['a']
        if extent is None:
            extent =''
    except TypeError:
        extent = ''
    try:
        itemDetails = record['300']['b']
        if itemDetails is None:
            itemDetails = ''
    except TypeError:
        itemDetails = ''
    try:
        dimensions = record['300']['c']
        if dimensions is None:
            dimensions = ''
    except TypeError:
        dimensions = ''
    try:
        generalNote = record['500']['a']
        if generalNote is None:
            generalNote = ''
    except TypeError:
        generalNote = ''
    try:
        summary = record['520']['a']
        if summary is None:
            summary = ''
    except TypeError:
        summary = ''
    try:
        subjectHeading = record['650']
        if subjectHeading is None:
            subjectHeading = ''
    except TypeError:
        subjectHeading = ''
    
    try:
        print('<record>'+
                '<title>' + title + '</title>' +
                '<title2>' + title2 + '</title>' +
                '<author>' + author + '</author>' +
                '<authorDates>' + authorDates + '</authorDates>' +
                '<isbn>' + isbn + '</isbn>' +
                '<LCCN>' + LCCN + '</LCCN>' +
                '<LCCN2>' + LCCN2 + '</LCCN2>' +
                '<dewey>' + dewey + '</dewey>' +
                '<placePub>' + placePub + '</placePub>' +
                '<publisher>' + publisher + '</publisher>' +
                '<pubDate>' + pubDate + '</pubDate>' +
                '<extent>' + extent + '</extent>' +
                '<itemDetails>' + itemDetails + '</itemDetails>' +
                '<dimensions>' + dimensions + '</dimensions>' +
                '<generalNote>' + generalNote + '</generalNote>' +
                '<summary>' + summary + '</summary>' +
                '<subjectHeading>' + subjectHeading + '</subjectHeading>'
                                '</record>')
    except:
        print('')

print('<collection>')
pymarc.map_xml(getMarcInfo, xml)
print('</collection>')
