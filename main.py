from GetVideos import get_all_links
from commentsTiktok import get_comments
import json

# search varible contains the google URL (URL data includes: site, search words, hashtags, date-before, date-after
search = "https://www.google.com/search?q=site:tiktok.com+%22%23budlight%22+after:2023-04-01+before:2023-04-14&sca_esv=a99f4f1e2fb679d4&sxsrf=AHTn8zps5n1EF4Qr5vp3ukRupttIkcuMpA:1745596694597&ei=FrELaJeeJJKtptQP7suC0AM&start=0&sa=N&sstk=Af40H4U_QC2PCgjPmOZRD3KgtmOCqmk6HPw0i22ExDqKrN6XfP3NzSRTK-e7ZehR5VYdvCXr_8hbS_BEhskbzHiCkzkikPwl0rSLGZn4-lqir8hAUhMhMSUwsIV2OnGBm_Ce&ved=2ahUKEwiXgZy3xvOMAxWSlokEHe6lADo4ChDx0wN6BAgJEAI&biw=1440&bih=785&dpr=2"

# running the method
links = get_all_links(search)

print(len(links))
print("\n\n\n\n\n")

for link in links:
    print(link)

open('output.json', 'w').close()

get_comments(links)

# Change data type in the comments output.json to include post_id and date in each "comment" entry

