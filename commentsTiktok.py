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


def req(post_id, curs):
    url = f'https://www.tiktok.com/api/comment/list/?WebIdLastTime=1729409061&aid=1988&app_language=en&app_name=tiktok_web&aweme_id={post_id}&browser_language=en-GB&browser_name=Mozilla&browser_online=true&browser_platform=MacIntel&browser_version=5.0%20%28Linux%3B%20Android%206.0%3B%20Nexus%205%20Build%2FMRA58N%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F128.0.0.0%20Mobile%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&count=200&cursor={curs}&data_collection_enabled=true&device_id=7427755272205075973&device_platform=web_mobile&focus_state=false&from_page=video&history_len=3&is_fullscreen=true&is_page_visible=true&odinId=7427755310612186117&os=android&priority_region=&referer=&region=CA&screen_height=1146&screen_width=1534&tz_name=America%2FToronto&user_is_login=false&verifyFp=verify_latio6ct_5FzXpKng_5ZAZ_4unS_AkTf_iCW6vWcdOHIQ&webcast_language=en&msToken=qQqwH0ExH-xY6AzFnFs0j_wVEckhRYWRx333JYcTAeFVrG8lEVaWXPdpNNNjLuJEpba7iKL-0zawApLPRqtf5y2izVrEsx1vg5A738_qWf8YDQyUJ7pNcmCvcI9fBer50jhGlZYwgbQHOW3ISBksR6xPhkY=&X-Bogus=DFSzswVuqE0ANJoutQDZ3GhyS0lt&_signature=_02B4Z6wo00001VebAhQAAIDAZDtjuzmji8FXuwaAADL1f2'

    response = requests.get(url=url, headers=headers)
    info = response.text
    # print("info: ")
    # print(info)
    raw_data = json.loads(info)
    # print(raw_data)

    return raw_data


def parser(data, comments):
    comment = data['comments']
    print("number of comments in this pull: \t")
    print(len(comment))
    # print(comment)

    coms = []
    replys = []
    names = []
    times = []
    titles = []
    urlis = []

    for cm in comment:
        # print(cm)
        com = cm['share_info']['desc']
        reply_num = cm['reply_comment_total']
        name = cm['user']['nickname']
        time = cm['create_time']
        title = cm['share_info']['title']
        urli = cm['share_info']['url']

        if "comment: " in com:
            com = com.split("comment: ")[1]

        if com == "":
            com = cm['text']
        # print(com)

        if name == "":
            name = "anonymous"

        if time == "":
            time = utc.now()
            time = str(time)
        else:
            time = utc.fromtimestamp(time)
            time = str(time)

        if title == "":
            title = "Error couldn't be retrieved"

        if urli == "":
            urli = "Error couldn't be retrieved"

        # print(name)

        # print(reply_num)

        # print()

        coms.append(com)  # got it
        replys.append(reply_num)  # got it
        names.append(name)  # got it
        times.append(time)
        titles.append(title)
        urlis.append(urli)

    for i in range(len(comment)):
        comments.append({
            "user_name": names[i],
            "comment": coms[i],
            "replies": replys[i],
            "titles": titles[i],
            "urlis": urlis[i],
            "times": times[i],
            "company": "BudLight"  # ToDo Name of the company added here. Can be changed from a case to case basis
        })

    return data


def get_comments(posts):
    for post_url in posts:
        print(post_url)
        post_id = post_url.split("/")[-1]

        comments = []
        # comments.append({'post_url': post_url})

        curs = 0

        while True:
            # print(len(comments))

            raw_data = req(post_id, curs)
            same_data = parser(raw_data, comments)

            if same_data['has_more'] == 1:
                curs += 200
                print('moving to the next cursor')
            else:
                print('no more data available')
                break

        print()

        with open('output.json', 'a', encoding='utf-8') as f:
            json.dump(comments, f, ensure_ascii=False, indent=4)

    print("\ndata has been saved into a JSON file")


# posts = {post_uri}
# get_comments(posts)
