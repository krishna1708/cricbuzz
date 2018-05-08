# cricbuzz
HTML page parsing

Please install following module before run the program
   1) urllib2  (To get the response from the given URL)
   2) scrapy (To write the xpaths using scrapy selector to extract the infromation from the given URL response)
   3) json     (To write the output to json file)

Steps to run the program:
   1) Download the attached file (assignment.py)
   2) Run the file using following command
             sudo python assignment.py
   3) It will ask to enter the inputs as follows (with example url and path)
             Enter the URL: http://www.cricbuzz.com/live-cricket-scorecard/19873/indw-vs-engw-6th-match-womens-t20i-tri-series-in-india-2018
             Enter Ouput File Path(Full path): /home/krishna/Desktop
   4) After program has run, it will create result.json file in the mentioned path in the user input
 
Note: this program is only works for ODI, T20 matches which are completed already. 

