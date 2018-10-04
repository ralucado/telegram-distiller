from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    def start_message(self):
        self.sndr_found = False
        self.vyl_found = False
        self.txt_found = False

    def handle_starttag(self, tag, attrs):
        if(('class','body') in attrs):
            #print(" --- A new message starts")
            self.start_message()
        if(('class','from_name') in attrs):
            #print(" --- A sender is found. Proceed to check name")
            self.sndr_found = True
        if(self.vyl_found and ('class','text') in attrs):
            self.txt_found = True
            #print(" --- A text from vyl is found")



    #def handle_endtag(self, tag):
       # print("Encountered an end tag :", tag)

    def handle_data(self, data):
        if(self.txt_found):
            print(data.strip())
            self.start_message()
        elif(self.sndr_found and 'Huebo' in data):
            #print(" --- A message from Vylion!")
            self.vyl_found = True

    def __init__(self):
        # initialize the base class
        HTMLParser.__init__(self)
        self.start_message()





parser = MyHTMLParser()
with open('HUEBOmessages.html','r') as f:
    output = f.read()
    parser.feed(output)

#parser.feed('<html><head><title class="whatever">Test</title></head>'
#            '<body> <div class="body">                        <div class="pull_right date details" title="02.04.2016 13:25:30">                            13:25                        </div>                        <div class="from_name">                            Huebo                         </div>                        <div class="reply_to details">                            In reply to <a href="#go_to_message5724" onclick="return GoToMessage(5724)">this message</a>                        </div>                        <div class="text">                            &quot;La segona prova FHC&quot;                        </div>                    </div></body></html>')