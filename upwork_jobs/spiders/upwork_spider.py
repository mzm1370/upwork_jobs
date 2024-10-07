import scrapy

class UpworkJobSpider(scrapy.Spider):
    name = "upwork_jobs"
    start_urls = [
        'https://www.upwork.com/search/jobs/?q=python&sort=recency'
    ]

    def parse(self, response):
        # Check for 403 Forbidden error
        if response.status == 403:
            self.logger.error("Received 403 Forbidden error.")
            return  # Optionally handle it differently or retry

        jobs = []

        for job in response.css('section.air-card'):
            try:
                title = job.css('h4.job-title::text').get().strip()
                description = job.css('span.js-description-text::text').get().strip()
                details = job.css('div.job-details::text').get().strip()
                
                yield {
                    'Title': title,
                    'Description': description,
                    'Details': details
                }
            except AttributeError:
                continue
