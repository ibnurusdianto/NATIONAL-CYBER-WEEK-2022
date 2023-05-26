# BEC Chitchat [331 pts]

**Category:** Forensic
**Solves:** 12

## Description
>*"A few days ago, I went to a store wanting to buy groceries, but the store was closed. Then, in front of the store I saw a banner with an email referring to the owner of the store. I contacted the email several times and I received a reply message from the email along with a brochure. Long story short, I go back home and opened the brochure from my computer and my computer got hacked, and I only realized after a few days later."*\r\n\r\n***As a Forensic Expert, you are given a document to analyze these evidences :***\r\n\r\n```\r\n1. What\s the name of suspected person(attacker) that send the malicious brochure?\r\n(FULLNAME all lower case + if the name consists of two words like "Ismail Marzuki" then seperate those with whitespace character)\r\n\r\n2. What is the attacker\s phone number?\r\n[Example Format = +62..........] -> Country-Code number format\r\n\r\n3. What is the Address(FQDN) that is close to the source email(sender)?\r\n(E.g : VG7SCF8EV1D.prod.ncwctf.donat.gula.id)\r\n\r\n4. What is the Address(IPv6 Address) that is close to the destination email(receiver)?\r\n(E.g : a05:a612:2d3:09f1:blah:blah:blah:blah)\r\n```\r\n\r\n\r\nHere is the netcat service to validate your answer :<br>\r\n``nc 103.167.136.75 1111``\r\n\r\n``nc 103.167.136.123 1111``\r\n\r\nThe flag is all the answers concatenated with **underscore**.\r\n\r\n`NCW22{answer1_answer2_answer3_answer4}`

**Hint**
* -

## Solution

### Flag

