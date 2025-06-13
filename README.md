#Documenting processes for sentimental analyzes of comments to understand corporate outrage responses
### *- Aadit Chadda (Trent University)*

**Repository URL:** https://github.com/Aadit-Chadda/GoogleSuperTimelineScrapper *(GitHub)*

##Post Collection
**Objective:** Collect comments data from posts made after a transgression event that causes backlash online, and then data after the companies response to the backlash. 

**Media:** Using ***TikTok*** comments as our base information. As it is the prominent open conversation platform, where people freely present their views not only through their posts but also their response to the posts (comments).

**Method:** Using google search to get a list of most relevant posts ranked in the time period required. The google search engineered input looks like this:

*site:tiktok.com "#budlight" after:2023-04-01 before:2023-04-14*

Using ***selenium*** to retrieve post links from the first 5 pages of the google search. We stop after 5 pages, because our TikTok API on average can bulk comments from 20-50 videos at a time, and feeding in more data causes the program to crash. Also since Google search is ranked and pretty advanced, also our search engineering is inherently neutral to the topic at hand, we can get accurate snippet of the global online environment of the timeframe we wish to capture. 

**Output:** In the end we are presented with a list of about 50 TikTok posts, which is then feeded into our comments processing system . 


##Comment Collection
**Objective:** Collect all the first level comments from every TikTok posts that were collected in the first phase of the program. 

**Media:** Using the native TikTok App – comments – API to collect comments data from the TikTok posts. 

**Method:** Iterate through all the TikTok post links feeding them into TikTok API. And collecting the following information from every call made

- Username
- Comment
- Number of replies on the comment
- Title of the post
- URL of the post
- DateTime stamp of the comment

Most API calls made cannot grab all the comments in a single fail swoop. However the API calls also keep track of 2 variables, the *“has_more”* and *“curs”* which can be manipulated and iterated through over and over again to get all the first layer comments in the post. 

**Contingency:** The TikTok API is vulnerable to crashes after retrieving large amounts of data. This prevents us from large numbers of the videos. Also creates a need for human interference. So, when the program eventually crashes we can copy all the links that were not scrapped. Put them in a list, and run the API program again now on these newer videos, and then add the comments to our original **“output.json”** file to create a masterlist of all comments related to the topic at hand.

**Output:** All of this data is iterated through on multiple levels, to collect all the comments from all the videos in our data system. This data is then consolidated in an output.json file. 
The structure of the file looks like:  

```
{
        "user_name": "calem.white",
        "comment": "Same company😭😭",
        "replies": 0,
        "title": "#buschlight",
        "url": "https://www.tiktok.com/@chelsea_swatek/video/7218347888634531115",
        "datetime": "2019-08-07 00:00:00" 
    },
```

##Comment Analysis
**Objective:** Conduct a comprehensive sentimental analysis on the comments which were harvested in the step before to analyze their polarity with respect to the company under scrutiny. 

**Example:**
```
Title: “Boycott bud light”
Comment: “You’re so stupid”
Analysis: is a comment that is inherently high in polarity and negative, but actually comes to defend the company, so the scale should score it highly positively. Referencing that a positive side of the scale is supporting the company and the negative side of the scale is an expression of outrage directed towards the company. 
```

**Media:** After trying multiple complex ways to solve this problem. The simplest way to solve the problem in all of its nuances and complexities is to simply use a ChatGPT API.

**Method:** To perform a coherent, usable sentiment analysis, we must take into account more information than just the polarity of the contents in the comment. To perform this complex sentimental analysis, we take a multi-step approach.

After settling on ***ChatGPT API (gpt-4.1-nano)*** we play around with its settings to get the exact input output configuration that we want and make sure that the call contexts’ are cost effective and the comment analysis is comprehensive in its context understanding. To accomplish this we provide context, such as the title of the video, date posted, and sentiment of the comment towards the company in question. 

While making the API calls we must be cautious to not overload the **TKM (Token per minute)**. So we can analyse around 220 comments in under 60 seconds, before taking a load-off break for 60 seconds. With this rate we can analyse 10,000 comments in under 3 hours. 

The ChatGPT API is the only cost-incurring function of the system. We get charged approx $0.10 for 10K tokens used. And analyzing each comment costs us under 150 tokens. 

**Output:** We analyze the comments on a range between -100 (negative) to +100 (positive). The analysis is firstly added to an analyser list csv file within the operation loop, to still have some saved data in case the program crashes mid-operation. After the full loop has run through and all comments in our database are analyzed, we add the analysis of the comment with the rest of the data gathered on it into a csv file. In the end all .JSON and analyses are converted into a .CSV file. 


