import json, sys

filename = sys.argv[1]
json_payload = ""

with open(filename, "r") as file_handle:
    json_payload = file_handle.read()

json_dict = json.loads(json_payload)
topics = json_dict['data']["topicTag"]
topics_count_dict = {}

overall_category = json_dict['data']['topicTag']['name']

for question in topics['questions']:
    for topic in question['topicTags']:
        if topic['name'] != overall_category:
            if topic['name'] in topics_count_dict:
                topics_count_dict[topic['name']] += 1
            else:
                topics_count_dict[topic['name']] = 1

sorted_topics = sorted(topics_count_dict.items(), key=lambda x: x[1], reverse=True)

for topic in sorted_topics:
    print("{} : {}".format(topic[0],topic[1]))

