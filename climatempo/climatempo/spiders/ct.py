import scrapy
from datetime import datetime
import time


class ClimatempoSpider(scrapy.Spider):
    name = 'ct'
    start_urls = ['https://www.climatempo.com.br/previsao-do-tempo/agora/cidade/363/portoalegre-rs']

    def parse(self, response, **kwargs):
        while True:
	        updated_at = datetime.now()
	        temperature_celsius = response.xpath('.//span[@class="-bold -gray-dark-2 -font-55 _margin-l-20 _center"]//text()').get()
	        description = response.xpath('.//span[@class="col"]//text()').get()
	        #description = description.split("Sensação - ")[1]
	        sensation = response.xpath('.//*[@id="mainContent"]/div[7]/div[4]/div[1]/div[2]/div[1]/div/div[3]/span[2]//text()').get()
	        umidity = response.xpath('.//*[@id="mainContent"]/div[7]/div[4]/div[1]/div[2]/div[1]/div/div[4]/ul/li[2]/div[2]/p/span//text()').get()
	        pressure = response.xpath('.//*[@id="mainContent"]/div[7]/div[4]/div[1]/div[2]/div[1]/div/div[4]/ul/li[3]/div[2]/span//text()').get()
	        wind = response.xpath('//*[@id="mainContent"]/div[7]/div[4]/div[1]/div[2]/div[1]/div/div[4]/ul/li[1]/div[2]//text()[2]').get()
	     
	        yield{
	          'updated_at' : updated_at,
	          'temperature_celsius' : temperature_celsius,
	          'description' : description,
	          'sensation' : sensation,
	          'umidity' : umidity,
	          'pressure' : pressure,
	          'wind' : wind,
	        }
	        time.sleep(3600) #change this to time you prefer(in seconds). 1 hour same as 3600 seconds
