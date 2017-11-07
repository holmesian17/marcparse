import pymarc

xml = '/home/holmesian/Documents/CatalogRecords/sandburg.xml'
booksxml = open('/home/holmesian/Documents/CatalogRecords/test.xml', 'w')


def getMarcInfo(record):
    booksxml.write('\t <record> \n')
    
    try:
        title = record['245']['a']
        #print('<title>' + title + '</title>')
        booksxml.write('\t\t<title>' + title + '</title>\n')

    except:
        pass

    try:
        title2 = record['245']['b']  
        #print('<title2>' + title2 + '</title2>')
        booksxml.write('\t\t<title2>' + title2 + '</title2>\n')
    except:
        pass

    try:
        author = record['100']['a']
        #print('<author>' + author + '</author>')
        booksxml.write('\t\t<author>' + author + '</author>\n')
    except:
        pass

    try:
        authorDates = record['100']['d']
        #print('<authorDates>' + authorDates + '</authorDates>')
        booksxml.write('\t\t<authorDates>' + authorDates + '</authorDates>\n')
    except:
        pass
    
    try:
        isbn = record['020']['a']
        #print('<isbn>' + isbn + '</isbn>')
        booksxml.write('\t\t<isbn>' + isbn + '</isbn>\n')
    except:
        pass

    try:
        LCCN = record['050']['a']
        #print('<LCCN>' + LCCN + '</LCCN>')
        booksxml.write('\t\t<LCCN>' + LCCN + '</LCCN>\n')
    except:
        pass

    try:    
        LCCN2 = record ['050']['b']
        #print('<LCCN2>' + LCCN2 + '</LCCN2>')
        booksxml.write('\t\t<LCCN2>' + LCCN2 + '</LCCN2>\n')
    except:
        pass

    try:
        dewey = record['082']['a']
        #print( '<dewey>' + dewey + '</dewey>' )
        booksxml.write('\t\t<dewey>' + dewey + '</dewey>\n')
    except:
        pass

    try:
        placePub = record['260']['a']
        #print('<placePub>' + placePub + '</placePub>')
        booksxml.write('\t\t<placePub>' + placePub + '</placePub>\n')
    except:
        pass

    try:
        publisher = record['260']['b']
        #print('<publisher>' + publisher + '</publisher>')
        booksxml.write('\t\t<publisher>' + publisher + '</publisher>\n')
    except:
        pass

    try:
        pubDate = record['260']['c']
        #print('<pubDate>' + pubDate + '</pubDate>')
        booksxml.write('\t\t<pubDate>' + pubDate + '</pubDate>\n')
    except: 
        pass

    try:
        extent = record['300']['a']
        #print('<extent>' + extent + '</extent>' )
        booksxml.write('\t\t<extent>' + extent + '</extent>\n' )
    except:
        pass

    try:
        itemDetails = record['300']['b']
        #print('<itemDetails>' + itemDetails + '</itemDetails>')
        booksxml.write('\t\t<itemDetails>' + itemDetails + '</itemDetails>\n')
    except:
        pass

    try:        
        dimensions = record['300']['c']
        #print('<dimensions>' + dimensions + '</dimensions>')
        booksxml.write('\t\t<dimensions>' + dimensions + '</dimensions>\n')
    except:
        pass

    try:
        generalNote = record['500']['a']
        #print('<generalNote>' + generalNote + '</generalNote>')
        booksxml.write('\t\t<generalNote>' + generalNote + '</generalNote>\n')
    except:
        pass

    try:
        summary = record['520']['a']
        #print('<summary>' + summary + '</summary>')
        booksxml.write('\t\t<summary>' + summary + '</summary>\n')
    except:
        pass

    try:
        subjectHeading = record.get_fields('650')
        #print('<subjectHeading>' + subjectHeading + '</subjectHeading>')
        booksxml.write('\t\t<subjectHeading>' + subjectHeading + '</subjectHeading>\n')
    except:
        pass

    #print('</record>')
    booksxml.write('\t</record>\n')

#print('<collection>')
booksxml.write('<?xml version="1.0" encoding="UTF-8"?>\n')
booksxml.write('<collection>\n')
pymarc.map_xml(getMarcInfo, xml)
#print('</collection>')
booksxml.write('</collection>')
booksxml.close()
