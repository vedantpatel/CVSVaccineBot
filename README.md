# CVSVaccineBot

## Overview 
* Given cities, state, phone number, and gmail email address, program will send message alerts notifying the vaccine status for your entered cities in the state.
* Bot uses CVS covid vaccine website to pull the information.

## How to Run
* Simply paste your ```email_addr``` and ```app_pwd``` as a string.
* To continously run ```CVSVaccineBot.py``` every 2 minutes, create a cron job and paste the following into your ```crontab -e``` editor:
 ```
 */2 * * * * /usr/bin/python3 /{path_to_dir}/CVSVaccineBot.py
 ```

## Requirements
* Python 3.7
* Install ```smtplib``` and ```EmailMessage```
* Refer to __requirements.txt__ file 
```
 pip install -r requirements.txt
 ```
 * ***For sending msg alerts:*** 
   * Enter your gmail email address for ```email_addr``` var.
   * Get ```app pwd``` by going into ***gmail account*** -> ***security*** -> ***Turn On 2-Step Verification*** and then click on ```App password```. Select ***app*** and choose ```other``` enter ```msg Alert``` and select ```generate```. Copy that app password and paste it into your ```app_pwd``` env var.
   * For entering your phone number on line 25 with proper mobile carrier's SMS Gateway Address, refer to the following:
     * Verizon – number@vtext.com
     * T-Mobile – number@tmomail.net
     * Sprint – number@messaging.sprintpcs.com
     * AT&T – number@txt.att.net
     * Boost Mobile – number@smsmyboostmobile.com
     * Cricket – number@sms.cricketwireless.net
     * U.S. Cellular – number@email.uscc.net