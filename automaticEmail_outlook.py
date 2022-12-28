# Abstergo

import win32com.client

# Connect to Outlook
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

# Access the inbox
inbox = outlook.GetDefaultFolder(6)

# Search for unread emails
unread_emails = inbox.Items.Restrict("[Unread] = true")

# Retrieve the first unread email
email = unread_emails.GetFirst()

# Generate a response using the OpenAI API and GPT-3 model
import openai
openai.api_key = "your_api_key"

response_text = openai.Completion.create(
    engine="text-davinci-003",
    prompt=f"This is an email: {email.Body}\n Write your reply to this email here in a professional manner:\n",
    temperature=0.5,
    max_tokens=1024,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
).get('choices')[0].get('text')

# Send the response email
response = email.Reply()
response.Body = response_text
response.Send()

# Mark the original email as read
email.UnRead = False
email.Save()
