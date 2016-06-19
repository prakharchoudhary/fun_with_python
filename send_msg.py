from twilio.rest import TwilioRestClient
#twilio is a python package we will use for this simple script(install twilio in windows usiong "pip install twilio" in command line)

#you need to sign up on www.twilio.com/try-twilio to get th etwo below fields
account_sid = "ACe0eb3b561e800b2ca6c9a724beb53ce0"
auth_token = "*********************"	#this is not my auth_key, i did it bcz leaving blank fields looks wierd.
client = TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(
	body = "Hey! This works!!",
	#enter the message to be sent
	to = "**********",
	#enter the reciever's phone no.
	from_ = "*********")
	#twilio no. assigned to us.
print message.sid