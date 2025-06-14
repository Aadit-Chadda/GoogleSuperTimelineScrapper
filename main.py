from GetVideos import get_all_links
from commentsTiktok import get_comments
import json

# search varible contains the google URL (URL data includes: site, search words, hashtags, date-before, date-after
search = "https://www.google.com/search?q=site%3Atiktok.com+%22%23budlight%22+after%3A2023-04-14+before%3A2023-05-14&sca_esv=3daf0913dc600547&biw=1440&bih=785&sxsrf=AE3TifPoRNG2qv5BMrmN4ZpsQW5oM6w4gQ%3A1749640840610&ei=iGZJaMn6JM-7seMPzafU0Q0&ved=0ahUKEwjJ3qeGoOmNAxXPXWwGHc0TNdo4FBDh1QMIEA&uact=5&oq=site%3Atiktok.com+%22%23budlight%22+after%3A2023-04-14+before%3A2023-05-14&gs_lp=Egxnd3Mtd2l6LXNlcnAiPnNpdGU6dGlrdG9rLmNvbSAiI2J1ZGxpZ2h0IiBhZnRlcjoyMDIzLTA0LTE0IGJlZm9yZToyMDIzLTA1LTE0SLddUPkOWJFXcAF4AJABAJgBmAGgAcoHqgEDMC43uAEDyAEA-AEBmAIAoAIAmAMAiAYBkgcAoAe7ArIHALgHAMIHAMgHAA&sclient=gws-wiz-serp"

# running the method to get links of TikTok videos
links = get_all_links(search)

print("\n\n\n")
print(len(links))  # number of all the links collected
print("\n\n\n\n\n")

# list of all the links
for link in links:
    print(link)

# emptying the json file before putting newer comments into it
open('output.json', 'w').close()

# running the method to get all the comments in all the videos
get_comments(links)

