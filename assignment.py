import urllib2
import scrapy
import json

def load_json(url, path):
    start = urllib2.urlopen(url)
    htmlSource = start.read()
    start.close()
    sel = scrapy.Selector(text=htmlSource)
    series = str(''.join(sel.xpath('//div[@class="cb-nav-subhdr cb-font-12"]/a/@title').extract()[0]))
    match_name = str(''.join(sel.xpath('//h1[@class="cb-nav-hdr cb-font-18 line-ht24"]/text()').extract()).split('-')[0].strip())
    venue = str(''.join(sel.xpath('//div[@class="cb-nav-subhdr cb-font-12"]/a/@title').extract()[1]))
    date = str(''.join(sel.xpath('//div[@class="cb-nav-subhdr cb-font-12"]//span/text()').extract()[-3].split(',')[0]))
    time = str(''.join(sel.xpath('//div[@class="cb-nav-subhdr cb-font-12"]//span/text()').extract()[-2].split(',')[0]))
    match_result = str(''.join(sel.xpath('//div[@class="cb-col cb-scrcrd-status cb-col-100 cb-text-complete"]//text()').extract()))
    
    team1, team1_score, team2, team2_score = sel.xpath('//div[@class="cb-col cb-col-100 cb-scrd-hdr-rw"]/span/text()').extract()

    first_batsmen = str(','.join(sel.xpath('//div[@id="innings_1"]/div[@class="cb-col cb-col-100 cb-ltst-wgt-hdr"]//div[@class="cb-col cb-col-27 "]/a/text()').extract())).split(',')
    first_dict = {}
    for i in first_batsmen:
        record = sel.xpath('//div[@id="innings_1"]/div[@class="cb-col cb-col-100 cb-ltst-wgt-hdr"]//div[@class="cb-col cb-col-27 "]/a[contains(text(), "%s")]/../../div//text()' % i.strip()).extract()
        runs_scored, balls_faced, fours, sixes, SR  = record[-5:]
        first_dict[i.strip()] = {'runs_scored': str(runs_scored), 'balls_faced': str(balls_faced), 'fours': str(fours), 'sixes': str(sixes), 'SR': str(SR)}
       
    first_bowler = str(','.join(sel.xpath('//div[@id="innings_1"]/div[@class="cb-col cb-col-100 cb-ltst-wgt-hdr"]//div[@class="cb-col cb-col-40"]/a/text()').extract())).split(',')
    first_bowler_dict = {}
    for i in first_bowler:
        record = sel.xpath('//div[@id="innings_1"]/div[@class="cb-col cb-col-100 cb-ltst-wgt-hdr"]//div[@class="cb-col cb-col-40"]/a[contains(text(), "%s")]/../../div//text()' % i.strip()).extract()
        O, M, R, W, NB, WD, ECO = record[-7:]
        first_bowler_dict[i.strip()] = {'O': str(O), 'M': str(M), 'R': str(R), 'W': str(W), 'NB': str(NB), 'WD': str(WD), 'ECO': str(ECO)}


    second_batsmen = str(','.join(sel.xpath('//div[@id="innings_2"]/div[@class="cb-col cb-col-100 cb-ltst-wgt-hdr"]//div[@class="cb-col cb-col-27 "]/a/text()').extract())).split(',')
    second_dict = {}
    for i in second_batsmen:
        record = sel.xpath('//div[@id="innings_2"]/div[@class="cb-col cb-col-100 cb-ltst-wgt-hdr"]//div[@class="cb-col cb-col-27 "]/a[contains(text(), "%s")]/../../div//text()' % i.strip()).extract()
        runs_scored, balls_faced, fours, sixes, SR  = record[-5:]
        second_dict[i.strip()] = {'runs_scored': str(runs_scored), 'balls_faced': str(balls_faced), 'fours': str(fours), 'sixes': str(sixes), 'SR': str(SR)}

    second_bowler = str(','.join(sel.xpath('//div[@id="innings_2"]/div[@class="cb-col cb-col-100 cb-ltst-wgt-hdr"]//div[@class="cb-col cb-col-40"]/a/text()').extract())).split(',')
    second_bowler_dict = {}
    for i in second_bowler:
        record = sel.xpath('//div[@id="innings_2"]/div[@class="cb-col cb-col-100 cb-ltst-wgt-hdr"]//div[@class="cb-col cb-col-40"]/a[contains(text(), "%s")]/../../div//text()' % i.strip()).extract()
        O, M, R, W, NB, WD, ECO = record[-7:]
        second_bowler_dict[i.strip()] = {'O': str(O), 'M': str(M), 'R': str(R), 'W': str(W), 'NB': str(NB), 'WD': str(WD), 'ECO': str(ECO)}


    first_inning = {"team": str(team1),
            "score": str(team1_score.replace(u'\xa0', ' ')), 
            "batsmen": first_dict,
            "bowlers": first_bowler_dict}

    Second_inning = {"team": str(team1),
            "score": str(team1_score.replace(u'\xa0', ' ')),
            "batsmen": second_dict,
            "bowlers": second_bowler_dict}

    Total_Output = {"series": series,
    "match_name": match_name, 
    "venue": venue,
    "date": date,
    "time": time,
    "match_result": match_result,
    "scorecard": {"First Inning": first_inning, "Second Inning": Second_inning}
    }

    with open('%s/result.json' % path, 'w') as fp:
        json.dump(Total_Output, fp)


if __name__ == '__main__':
    url = raw_input("Enter the URL: ")
    output_file_path = raw_input("Enter Ouput File Path(Full path): ")
    load_json(url, output_file_path)

