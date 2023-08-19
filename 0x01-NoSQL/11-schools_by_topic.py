#!/usr/bin/env python3
'''Task's module.
'''


def schools_by_topic(mongo_collection,topic):
    '''Returns the list of school having a specific topic.
    '''
    topic_filter = {
            'topics': {
                '$elemeMatch': {
                    '$eq': topic,
                    },
                },
            }
    return[doc for doc in mongo_collection.find(topic_filter)]
