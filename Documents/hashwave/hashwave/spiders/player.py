import scrapy


class PlayerSpider(scrapy.Spider):
    name = "hashwave"
    allowed_domains = ['www.espncricinfo.com/']
    start_urls = ['http://www.espncricinfo.com/india/content/player/36084.html']

    def parse(self,response):

        player_name = response.xpath('//h1/text()').extract()

        country = response.xpath('//h3[@class = "PlayersSearchLink"]/b/text()').extract()

        full_name = response.xpath('//p[1][@class = "ciPlayerinformationtxt"]/span/text()').extract()

        born = response.xpath('//p[2][@class = "ciPlayerinformationtxt"]/span/text()').extract()

        current_age = response.xpath('//p[3][@class = "ciPlayerinformationtxt"]/span/text()').extract()

        mt = response.xpath('//p[4][@class = "ciPlayerinformationtxt"]/span/text()').extract()
        major_teams=[]
        major_teams.append(mt)

        playing_role = response.xpath('//p[5][@class = "ciPlayerinformationtxt"]/span/text()').extract()

        batting_style = response.xpath('//p[6][@class = "ciPlayerinformationtxt"]/span/text()').extract()

        bowling_style = response.xpath('//p[7][@class = "ciPlayerinformationtxt"]/span/text()').extract()

        image = response.xpath('//div[2]/img/@src').extract()

        geo_details = " "

        url = ["http://www.espncricinfo.com/india/content/player/36084.html"]

        for item in zip(player_name, country, full_name, born, current_age, major_teams,
                       playing_role, batting_style, bowling_style, image, geo_details, url):
                scraped = {
                'player_name' : item[0],
                'country' : item[1],
                'full_name' : item[2],
                'born' : item[3],
                'current_age' : item[4],
                'major_teams' : item[5],
                'playing_role' : item[6],
                'batting_style' : item[7],
                'bowling_style' : item[8],
                'image' : item[9],
                'geo_details' : item[10],
                'url' : item[11]
                }
        yield scraped
