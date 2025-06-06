from apify_client import ApifyClient

token = "apify_api_KxyrcPz32hhLDmvgAPEkSp9SMgFcWV4Dx5mX"

client = ApifyClient(token)

# Prepare the Actor input
run_input = {
    "directUrls": ["https://www.instagram.com/humansofny/"],
    "resultsType": "posts",
    "resultsLimit": 200,
    "searchType": "hashtag",
    "searchLimit": 1,
    "addParentData": False,
}

# Run in Actor and wait for it to finish
run = client.actor("shu8hvrXbJbY3Eb9W").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)


