import facebook

# TODO
'''
1. Use the facebook API to first collect data of first 5000 people with the mentioned name.
2. Count the number of the males and females based on the data.
3. If no females exist for a name give it the tag 'male'.
4. If no females exist for a name give it the tag 'female'.
5. Else term it as unisex.
'''
graph = facebook.GraphAPI(access_token="")