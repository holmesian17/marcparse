import pymarc


xml = '/home/holmesian/Documents/CatalogRecords/Columbia-extract-20170930-014.xml'
booksxml = open('/home/holmesian/Documents/CatalogRecords/formatted.xml', 'w')


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
        subjectHeading650a = record['650']['a']
        booksxml.write('\t\t<subjectHeading>' + subjectHeading650a + '</subjectHeading>\n')
        #print('<subjectHeading>' + subjectHeading + '</subjectHeading>')  
    except:
        pass
    
    try:
        subjectHeading650ax = record['650']['a'] + '-' + record['650']['x']
        booksxml.write('\t\t<subjectHeading>' + subjectHeading650ax + '</subjectHeading>\n')
    except:
        pass

    try:
        subjectHeading650ae = record['650']['a'] + '-' + record['650']['e']
        booksxml.write('\t\t<subjectHeading>' + subjectHeading650ae + '</subjectHeading>\n')
    except:
        pass

    try:
        subjectHeading650av = record['650']['a'] + '-' + record['650']['v']
        booksxml.write('\t\t<subjectHeading>' + subjectHeading650av + '</subjectHeading>\n')
    except:
        pass 

    try:
        subjectHeading650ay = record['650']['a'] + '-' + record['650']['y']
        booksxml.write('\t\t<subjectHeading>' + subjectHeading650ay + '</subjectHeading>\n')
    except:
        pass

    try:
        subjectHeading650az = record['650']['a'] + '-' + record['650']['z']
        booksxml.write('\t\t<subjectHeading>' + subjectHeading650az + '</subjectHeading>\n')
    except:
        pass

    try:
        subjectHeading650azv = record['650']['a'] + '-' + record['650']['z'] + '-' + record['650']['v']
        booksxml.write('\t\t<subjectHeading>' + subjectHeading650azv + '</subjectHeading>\n')
    except:
        pass

    try:
        subjectHeading650ayz = record['650']['a'] + '-' + record['650']['y'] + '-' + record['650']['z']
        booksxml.write('\t\t<subjectHeading>' + subjectHeading650ayz + '</subjectHeading>\n')
    except:
        pass

    try:
        subjectHeading650azx = record['650']['a'] + '-' + record['650']['z'] + '-' + record['650']['x']
        booksxml.write('\t\t<subjectHeading>' + subjectHeading650azx + '</subjectHeading>\n')
    except:
        pass

    try:
        subjectHeading650ayx = record['650']['a'] + '-' + record['650']['y'] + '-' + record['650']['x']
        booksxml.write('\t\t<subjectHeading>' + subjectHeading650ayx + '</subjectHeading>\n')
    except:
        pass        

    try:
        subjectHeading600a = record['600']['a']
        booksxml.write('\t\t<subjectHeading>' + subjectHeading600a + '</subjectHeading>\n')
    except:
        pass  

    try:
        subjectHeading600ad = record['600']['a'] + '-' + record['600']['d']
        booksxml.write('\t\t<subjectHeading>' + subjectHeading600ad + '</subjectHeading>\n')
    except:
        pass 

    try:
        subjectHeading600adx = record['600']['a'] + '-' + record['600']['d'] + '-' + record['600']['x']
        booksxml.write('\t\t<subjectHeading>' + subjectHeading600adx + '</subjectHeading>\n')
    except:
        pass  

    try:
        subjectHeading610a = record['610']['a']
        booksxml.write('\t\t<subjectHeading>' + subjectHeading610a + '</subjectHeading>\n')
    except:
        pass  

    try:
        subjectHeading647a = record['647']['a']
        booksxml.write('\t\t<subjectHeading>' + subjectHeading647a + '</subjectHeading>\n')
    except:

        pass         

    try:
        subjectHeading648a = record['648']['a']
        booksxml.write('\t\t<subjectHeading>' + subjectHeading648a + '</subjectHeading>\n')
    except:
        pass 

    try:
        subjectHeading651a = record['651']['a']
        booksxml.write('\t\t<subjectHeading>' + subjectHeading651a + '</subjectHeading>\n')
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
