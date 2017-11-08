import pymarc


xml = '/home/holmesian/Documents/CatalogRecords/Columbia-extract-20170930-014.xml'
booksxml = open('/home/holmesian/Documents/CatalogRecords/formatted.csv', 'w')


def getMarcInfo(record):

    try:
        title = record['245']['a']
        #print('<title>' + title + '</title>')
        booksxml.write(title + ',')

    except:
        booksxml.write(',')

    try:
        title2 = record['245']['b']  
        #print('<title2>' + title2 + '</title2>')
        booksxml.write(title2 + ',')
    except:
        booksxml.write(',')

    try:
        author = record['100']['a']
        #print('<author>' + author + '</author>')
        booksxml.write(author + ',')
    except:
        booksxml.write(',')

    try:
        authorDates = record['100']['d']
        #print('<authorDates>' + authorDates + '</authorDates>')
        booksxml.write(authorDates + ',')
    except:
        booksxml.write(',')
    
    try:
        isbn = record['020']['a']
        #print('<isbn>' + isbn + '</isbn>')
        booksxml.write(isbn + ',')
    except:
        booksxml.write(',')

    try:
        LCCN = record['050']['a']
        #print('<LCCN>' + LCCN + '</LCCN>')
        booksxml.write(LCCN + ',')
    except:
        booksxml.write(',')

    try:    
        LCCN2 = record ['050']['b']
        #print('<LCCN2>' + LCCN2 + '</LCCN2>')
        booksxml.write(LCCN2 + ',')
    except:
        booksxml.write(',')

    try:
        dewey = record['082']['a']
        #print( '<dewey>' + dewey + '</dewey>' )
        booksxml.write(dewey + ',')
    except:
        booksxml.write(',')

    try:
        placePub = record['260']['a']
        #print('<placePub>' + placePub + '</placePub>')
        booksxml.write(placePub + ',')
    except:
        booksxml.write(',')

    try:
        publisher = record['260']['b']
        #print('<publisher>' + publisher + '</publisher>')
        booksxml.write(publisher + ',')
    except:
        booksxml.write(',')

    try:
        pubDate = record['260']['c']
        #print('<pubDate>' + pubDate + '</pubDate>')
        booksxml.write(pubDate + ',')
    except: 
        booksxml.write(',')

    try:
        extent = record['300']['a']
        #print('<extent>' + extent + '</extent>' )
        booksxml.write(extent + ',')
    except:
        booksxml.write(',')

    try:
        itemDetails = record['300']['b']
        #print('<itemDetails>' + itemDetails + '</itemDetails>')
        booksxml.write(itemDetails + ',')
    except:
        booksxml.write(',')

    try:        
        dimensions = record['300']['c']
        #print('<dimensions>' + dimensions + '</dimensions>')
        booksxml.write(dimensions + ',')
    except:
        booksxml.write(',')

    try:
        generalNote = record['500']['a']
        #print('<generalNote>' + generalNote + '</generalNote>')
        booksxml.write(generalNote + ',')
    except:
        booksxml.write(',')

    try:
        summary = record['520']['a']
        #print('<summary>' + summary + '</summary>')
        booksxml.write(summary + ',')
    except:
        booksxml.write(',')

    try:
        subjectHeading650a = record['650']['a']
        booksxml.write(subjectHeading650a + ',')
        #print('<subjectHeading>' + subjectHeading + '</subjectHeading>')  
    except:
        booksxml.write(',')
    
    try:
        subjectHeading650ax = record['650']['a'] + '-' + record['650']['x']
        booksxml.write(subjectHeading650ax + ',')
    except:
        booksxml.write(',')

    try:
        subjectHeading650ae = record['650']['a'] + '-' + record['650']['e']
        booksxml.write(subjectHeading650ae + ',')
    except:
        booksxml.write(',')

    try:
        subjectHeading650av = record['650']['a'] + '-' + record['650']['v']
        booksxml.write(subjectHeading650av + ',')
    except:
        booksxml.write(',') 

    try:
        subjectHeading650ay = record['650']['a'] + '-' + record['650']['y']
        booksxml.write(subjectHeading650ay + ',')
    except:
        booksxml.write(',')

    try:
        subjectHeading650az = record['650']['a'] + '-' + record['650']['z']
        booksxml.write(subjectHeading650az + ',')
    except:
        booksxml.write(',')

    try:
        subjectHeading650azv = record['650']['a'] + '-' + record['650']['z'] + '-' + record['650']['v']
        booksxml.write(subjectHeading650azv + ',')
    except:
        booksxml.write(',')

    try:
        subjectHeading650ayz = record['650']['a'] + '-' + record['650']['y'] + '-' + record['650']['z']
        booksxml.write(subjectHeading650ayz + ',')
    except:
        booksxml.write(',')

    try:
        subjectHeading650azx = record['650']['a'] + '-' + record['650']['z'] + '-' + record['650']['x']
        booksxml.write(subjectHeading650azx + ',')
    except:
        booksxml.write(',')

    try:
        subjectHeading650ayx = record['650']['a'] + '-' + record['650']['y'] + '-' + record['650']['x']
        booksxml.write(subjectHeading650ayx + ',')
    except:
        booksxml.write(',')        

    try:
        subjectHeading600a = record['600']['a']
        booksxml.write(subjectHeading600a + ',')
    except:
        booksxml.write(',')  

    try:
        subjectHeading600ad = record['600']['a'] + '-' + record['600']['d']
        booksxml.write(subjectHeading600ad + ',')
    except:
        booksxml.write(',') 

    try:
        subjectHeading600adx = record['600']['a'] + '-' + record['600']['d'] + '-' + record['600']['x']
        booksxml.write(subjectHeading600adx + ',')
    except:
        booksxml.write(',')  

    try:
        subjectHeading610a = record['610']['a']
        booksxml.write(subjectHeading610a + ',')
    except:
        booksxml.write(',')  

    try:
        subjectHeading647a = record['647']['a']
        booksxml.write(subjectHeading647a + ',')
    except:

        booksxml.write(',')         

    try:
        subjectHeading648a = record['648']['a']
        booksxml.write(subjectHeading648a + ',')
    except:
        booksxml.write(',') 

    try:
        subjectHeading651a = record['651']['a']
        booksxml.write(subjectHeading651a + ',')
    except:
        booksxml.write(',') 

    #print('</record>')
    booksxml.write('\n')

#print('<collection>')
booksxml.write('title,title2,author,authorDates,isbn,LCCN,LCCN2,dewey,placePub,publisher,pubDate,extent,itemDetails,dimensions,generalNote,summary,subjectHeading650a,subjectHeading650ax,subjectHeading650ae,subjectHeading650av,subjectHeading650ay,subjectHeading650az,subjectHeading650ayz,subjectHeading650azx,subjectHeading650ayx,subjectHeading600a,subjectHeading600ad,subjectHeading610a,subjectHeading647a,subjectHeading648a,subjectHeading651a\n')
pymarc.map_xml(getMarcInfo, xml)
#print('</collection>')
booksxml.close()
