# Using the TikTok Native App API to retrieve all the first layer comments made on the posts
# This file is different, because when the first order of TikTok runs crashes,
# we create a list of the videos that were not scrapped, and run them over here in this file
# the comments are added to output1.json Then copied from here and pasted into our original output.json file
# most of the code in this file in identical to commentsTiktok.py
# with the exception to how videos are fed into the scrapping function

# importing all required libraries
import requests
import json
import utc

# post_uri = "https://www.tiktok.com/@hungrymanbutteranch/video/7219118527607983406"  # TikTok reel link url

headers = {
    'accept': '*/**',
    'accept-language': 'en-US,en;q=0.9, fa;q=0.8',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.tiktok.com/explore',
    'sec-ch-ua': '"Google Chrome"; v="129", "Not-A?Brand"; v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}


# Creating a request to the TikTok API for the comments
def req(post_id, curs):
    # post_id and curs are the external variables that are fed into the url formatting to get the desired comments
    url = f'https://www.tiktok.com/api/comment/list/?WebIdLastTime=1729409061&aid=1988&app_language=en&app_name=tiktok_web&aweme_id={post_id}&browser_language=en-GB&browser_name=Mozilla&browser_online=true&browser_platform=MacIntel&browser_version=5.0%20%28Linux%3B%20Android%206.0%3B%20Nexus%205%20Build%2FMRA58N%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F128.0.0.0%20Mobile%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&count=200&cursor={curs}&data_collection_enabled=true&device_id=7427755272205075973&device_platform=web_mobile&focus_state=false&from_page=video&history_len=3&is_fullscreen=true&is_page_visible=true&odinId=7427755310612186117&os=android&priority_region=&referer=&region=CA&screen_height=1146&screen_width=1534&tz_name=America%2FToronto&user_is_login=false&verifyFp=verify_latio6ct_5FzXpKng_5ZAZ_4unS_AkTf_iCW6vWcdOHIQ&webcast_language=en&msToken=qQqwH0ExH-xY6AzFnFs0j_wVEckhRYWRx333JYcTAeFVrG8lEVaWXPdpNNNjLuJEpba7iKL-0zawApLPRqtf5y2izVrEsx1vg5A738_qWf8YDQyUJ7pNcmCvcI9fBer50jhGlZYwgbQHOW3ISBksR6xPhkY=&X-Bogus=DFSzswVuqE0ANJoutQDZ3GhyS0lt&_signature=_02B4Z6wo00001VebAhQAAIDAZDtjuzmji8FXuwaAADL1f2'

    response = requests.get(url=url, headers=headers)
    info = response.text
    # print("info: ")
    # print(info)
    raw_data = json.loads(info)  # loading the data into a parsable json format
    # print(raw_data)

    return raw_data


# Creating a parser method to chop down and get only the desired information form the API calls made
def parser(data, comments):
    comment = data['comments']  # Getting only the comments data from the data that was scrapped by our API in the app
    print("number of comments in this pull: \t")
    print(len(comment))  # total number of comments in this parser
    # print(comment)

    # list of all the data in the comments API that we want to keep a track of
    coms = []  # comment body
    replys = []  # no. of replies to the comment
    names = []  # name of the person who commented
    times = []  # datetime of the comment made
    titles = []  # title of the video the comment was made on
    urlis = []  # url of the video

    # parsing through json comment retrieved and selecting the fields of our interest
    for cm in comment:
        # print(cm)
        com = cm['share_info']['desc']
        reply_num = cm['reply_comment_total']
        name = cm['user']['nickname']
        time = cm['create_time']
        title = cm['share_info']['title']
        urli = cm['share_info']['url']

        # chopping down comment body we don't need
        if "comment: " in com:
            com = com.split("comment: ")[1]

        # in case the comment is empty
        if com == "":
            com = cm['text']
        # print(com)

        # in case the comment user name field is empty
        if name == "":
            name = "anonymous"

        # in case the comment date time field is empty
        if time == "":
            time = utc.now()  # if the datetime field is empty we use the current datetime as a default
            time = str(time)  # making sure to convert the datetime field to a string for easy parsing
        else:
            time = utc.fromtimestamp(time)  # retrieving the datetime from the timestamp in the json file
            time = str(time)  # making sure to convert the datetime field to a string for east parsing

        # in case the title of the video is empty
        if title == "":
            title = "Error couldn't be retrieved"

        # in case the url of the video is empty
        if urli == "":
            urli = "Error couldn't be retrieved"

        # print(name)

        # print(reply_num)

        # print()

        # Adding the data retrieved from each comment to the file where we keep track of teh video field metadata
        coms.append(com)
        replys.append(reply_num)
        names.append(name)
        times.append(time)
        titles.append(title)
        urlis.append(urli)

    # creating a final master dictionary list of all meta data retrieved from the API calls made
    for i in range(len(comment)):
        comments.append({
            "user_name": names[i],
            "comment": coms[i],
            "replies": replys[i],
            "titles": titles[i],
            "urlis": urlis[i],
            "times": times[i],
            "comapany": "BudLight"  # ToDo Name of the company added here. Can be changed from a case to case basis
        })

    return data


# Get comments from post function
def get_comments(posts):
    # iterating through the list of post urls to get the comments from each post one at a time
    for post_url in posts:
        print(post_url)
        post_id = post_url.split("/")[-1]  # getting the post if from the post url list created

        comments = []  # empty list to store all comments that are retrieved
        # comments.append({'post_url': post_url})

        curs = 0  # setting initial value of the cursor to 0

        # creating a loop that iterates till all the comments are retrieved from the post
        while True:
            # print(len(comments))

            raw_data = req(post_id, curs)  # calling the request to TikTok API function
            same_data = parser(raw_data, comments)  # calling the comment parsing function

            if same_data['has_more'] == 1:  # if more comments are still available to be scrapped in the post
                curs += 200  # we update the cursor to get more data
                print('moving to the next cursor')
            else:  # if no more data is available in the post we break the loop and move to the next comment
                print('no more data available')
                break

        print()

        # pushing all the data to a json file in the end of each post analysis
        with open('output1.json', 'a', encoding='utf-8') as f:
            json.dump(comments, f, ensure_ascii=False, indent=4)

    print("\ndata has been saved into a JSON file")


# list of all the videos whose comments need to be scrapped
posts = [
    "https://www.tiktok.com/@zakkittle/video/7223213680941485354",
    "https://www.tiktok.com/@stephenamon_/video/7223839056256437510",
    "https://www.tiktok.com/@sterling_archer_ba/video/7222793317883333930",
    "https://www.tiktok.com/@newoldheads/video/7221932764721941802",
    "https://www.tiktok.com/@silverbackgreybeard/video/7225656897964150062",
    "https://www.tiktok.com/@darcealearlgates/video/7221956957366652203",
    "https://www.tiktok.com/@funnycleanvideos/video/7227278269509389610",
    "https://www.tiktok.com/@pjadz/video/7230545398425767211",
    "https://www.tiktok.com/@_laura_elisa/video/7228036362782510378",
    "https://www.tiktok.com/@chefload/video/7225757610274737450",
    "https://www.tiktok.com/@bigboytater/video/7226340084356828462",
    "https://www.tiktok.com/@scrizzapp/video/7225956910254542126",
    "https://www.tiktok.com/@arnegeerdts/video/7230103582169730309",
    "https://www.tiktok.com/@spencerjordan/video/7231701360624848170",
    "https://www.tiktok.com/@throughbeingcooltattoo/video/7227528018653138219",
    "https://www.tiktok.com/@miggys79/video/7223800498464230702",
    "https://www.tiktok.com/@feralgigi/video/7222330177219513643",
    "https://www.tiktok.com/@leighlou1970/video/7227963733866204458",
    "https://www.tiktok.com/@newslitproject/video/7223500471430860074",
    "https://www.tiktok.com/@realmattthewelder/video/7225367108186574123",
    "https://www.tiktok.com/@thealabamaboss/video/7230690770984897838",
    "https://www.tiktok.com/@moethunder092/video/7224282931450154246",
    "https://www.tiktok.com/@nwslsoccer/video/7223824375068282155"
]

# calling the function to get comments
get_comments(posts)
