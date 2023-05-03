import os
import re
from twilio.rest import Client

# Set up your Twilio account credentials
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

# Set up the carrier domains to use for appending email addresses
carrier_domains = {
    'AT&T': '@txt.att.net',
    'T-Mobile USA, Inc': '@tmomail.net',
    'Verizon': '@vtext.com',
    'Sprint': '@messaging.sprintpcs.com',
    'US Cellular': '@email.uscc.net',
    'Boost Mobile': '@myboostmobile.com',
    'Cricket': '@sms.mycricket.com',
    'MetroPCS': '@mymetropcs.com',
    'Tracfone': '@mmst5.tracfone.com',
    'Virgin Mobile': '@vmobl.com',
    'Republic Wireless': '@text.republicwireless.com',
    'Straight Talk': '@mypixmessages.com',
    'Page Plus': '@vtext.com',
    'Google Fi': '@msg.fi.google.com',
    'Consumer Cellular': '@mailmymobile.net',
    'Xfinity Mobile': '@vtext.com',
    'Mint Mobile': '@mailmymobile.net',
    'Visible': '@vtext.com',
    'C Spire': '@cspire1.com',
    'H2O Wireless': '@mms.att.net',
    'Net10 Wireless': '@mms.att.net',
    'Red Pocket Mobile': '@txt.att.net',
    'Simple Mobile': '@smtext.com',
    'TextNow': '@textnow.me',
    'Total Wireless': '@vtext.com',
    'Ultra Mobile': '@t-mobile-sms.com',
    'Wing': '@wingalpha.com',
    'Xfinity Mobile': '@vtext.com',
    'Altice Mobile': '@sms.optimum.net',
    'Cricket Wireless': '@mms.cricketwireless.net',
    'Freedom Mobile': '@txt.freedommobile.ca',
    'GreatCall': '@vtext.com',
    'GCI': '@msg.gci.net',
    'Inland Cellular': '@inlandlink.com',
    'Lycamobile': '@mail2txt.com',
    'MobiPCS': '@mobipcs.net',
    'Mosaic Telecom': '@smsmail.mosaictelecom.net',
    'Nemont': '@sms.nemont.net',
    'Pioneer Cellular': '@zsend.com',
    'Q Link Wireless': '@qlinkwireless.com',
    'Rogers': '@sms.rogers.com',
    'Simple Freedom': '@text.simplefreedom.net',
    'Southern Linc': '@page.southernlinc.com',
    'Syringa Wireless': '@rinasms.com',
    'Tbaytel': '@tbayteltxt.net',
    'Teleflip': '@teleflip.com',
    'Telus': '@msg.telus.com',
    'TerreStar': '@mobile-satellite.com',
    'Truphone': '@sms.truphone.com',
    'Union Wireless': '@union-tel.com',
    'West Central Wireless': '@sms.wcc.net',
}



# Set up the path to your file with phone numbers
filename = 'phone.txt'

# Open the file and read in the phone numbers
with open(filename, 'r') as f:
    phone_numbers = [line.strip() for line in f]

# Loop over the phone numbers and look up the carrier using Twilio's Lookup API
with open('result.txt', 'w') as outfile:
    for phone_number in phone_numbers:
        try:
            # Look up the phone number and get the carrier name
            phone_info = client.lookups.v1.phone_numbers(phone_number).fetch(type=['carrier'])
            carrier_name = phone_info.carrier['name']
           
            
            # Check if the carrier is a mobile carrier, and if so, append the appropriate email domain
            if phone_info.carrier['type'] == 'mobile':
                for carrier in carrier_domains.keys():
                    if re.match(carrier, carrier_name):
                        email_domain = carrier_domains.get(carrier, '')
                        if email_domain:
                            # Write the phone number and carrier email domain to the output file
                            outfile.write(f"{phone_number}{email_domain}\n")
                   
        except Exception as e:
            # If an error occurs during the lookup, print the error message
            print(f"Error looking up phone number {phone_number}: {e}")
