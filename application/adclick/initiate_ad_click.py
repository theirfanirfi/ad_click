from application.models.models import Job
from application.adclick.settings import *
from application.adclick.google_process import Google

def execute(job: Job):
    search_keywords = job.keywords.split(',')
    print("Using search keywords")
    print(search_keywords)
    ad_site = None
    print(job.website)
    
    iter = int(job.number_of_runs)
    print(iter)



# if len(search_keywords) == 0:
#     print("Please place search keywords one per line in keywords.txt")
#     exit()


# site_random = input("Do you want the ad click to be random? (y/n) ")
# if site_random == "y" or site_random == "Y":
#     ad_site = None
# else:
#     ad_site = input("Enter the url of the advertisement's website: ")

# iter = int(input("Enter the number of times you want to run: "))

    if use_proxy:
        per_proxy = searches_per_proxy
    else:
        per_proxy = iter

        proxy_count = 0

        g = Google()

        for _ in range(iter):
            if proxy_count >= per_proxy:
                proxy_count = 0
                g.swap_proxy()

            g.process(search_keywords, ad_site)
            
            proxy_count += 1

        g.close()
