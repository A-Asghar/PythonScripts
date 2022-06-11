#Take outlook emails from inbox and save them to txt files



import win32com.client

import os
from datetime import datetime,timedelta
import re
outlook = win32com.client.Dispatch('outlook.application')
mapi = outlook.GetNamespace("MAPI")
for account in mapi.Accounts:
	print(account.DeliveryStore.DisplayName)

inbox = mapi.GetDefaultFolder(6)
messages = inbox.Items

received_dt = datetime.now() -  timedelta(days=1)
received_dt = received_dt.strftime('%m/%d/%Y %H:%M %p')
messages = messages.Restrict("[ReceivedTime] >= '" + received_dt + "'")
#messages = messages.Restrict("[SenderEmailAddress] = 'contact@codeforests.com'")
#messages = messages.Restrict("[Subject] = 'Sample Report'")

#Let's assume we want to save the email attachment to the below directory
'''
outputDir = r"C:\\Users"
try:
	for message in list(messages):
		try:
			s = message.sender
			for attachment in message.Attachments:
				attachment.SaveASFile(os.path.join(outputDir, attachment.FileName))
				print(f"attachment {attachment.FileName} from {s} saved")
		except Exception as e:
			print("error when saving the attachment:" + str(e) )
except Exception as e:
	print("error when processing emails messages:" + str(e))
'''
outputDir = "C:\\Users\\Ali Asghar\\Desktop"
os.chdir(outputDir)
try:
	for message in list(messages):
		try:
			#print(message)
			

			
			name = str(message.subject)
			name = re.sub('[^A-Za-z0-9]+', '', name)+'.txt'
			message.SaveAs(outputDir + "//" + name , 0)
		except Exception as e:
			print(e)

		
except Exception as e:
	print("error when processing emails messages:" + str(e))



