score = 0
print("Answer all the following questions below")

answer = input("What is the primary purpose of a firewall in network security? \
               \n A. Encrypting data \n B. Monitoring network traffic \n C. Controlling access to network resources \
               \n D. Detecting malware")

if answer == "c" or answer == "C":
    score = score+1
    print("Correct Answer!")
else:
    print("Wrong Answer!")

answer = input("What type of attack involves intercepting and modifying communication between two parties? \
               \n A. Phishing \n B. Man-in-the-middle \n C. DDoS \n D. Brute force \n ")

if answer == "b" or answer == "B":
    score = score+1
    print("Correct! Good answer")
else:
    print("Wrong!")

answer = input("Which of the following encryption algorithms is symmetric? \
               \n A. RSA \n B. AES \n C. Diffle-Hellman \n D. ECC \n")

if answer == "b" or answer == "B":
    score = score+1
    print("Good!")
else:
    print("Wrong Answer!")

answer = input("What is the primary purpose of a VPN (Virtual Private Network)? \
               \n A. Anonymize browsing \n B. Secure communication over public networks \n C. Filter out malicious content \n D. Monitor network traffic \n")

if answer == "b" or answer == "B":
    score = score+1
    print("Correct!")
else:
    print("Wrong!")

answer = input("5. Which of the following is a secure protocol for transferring files? \
               \n A.FTP \n B.SFTP \n C.TFTP \n D.SNMP \n")

if answer == "b" or answer == "B":
    score = score+1
    print("Correct!")
else:
    print("Wrong!")

answer = input("6. Which of the following is Not a type of access control? \
               \n A.Dac \n B.Mac \n C.Rbac \n D.HAC")

if answer == "d" or answer == "D":
    score = score+1
    print("Good Answer!")
else:
    print("Wrong Answer")

answer = input("7.What does a rootkit primarily target? \
               \n A.Network traffic \n B.User Data \n C.Operating System \n D.Firewall Rules")

if answer == "b" or answer == "B":
    print("Correct Answer")
    score = score=1
else:
    print("Wrong Answer")

answer = input("8.A cybersecurity analyst has discovered that an attacker has been moving laterally within the network. What is the best next step? \
               \n A.Implement a honeypot \n B.Disconnect the entire network \n C.Perform a risk assessment \n D.Contain the compromise")

if answer == "c" or answer == "C":
    print("Correct Answer")
    score = score+1
else:
    print("Wrong Answer!")

answer = input("9.Which of the following is considered an example of a technical control? \
               \n A.Security policy \n B.User Training \n C.Firewall \n D.Background Checks")

if answer == "c" or answer == "C":
    print("Correct!")
    score = score+1
else:
    print("Wrong!")

answer = input("10.A company has implemented a system to centralize the management of user credentials. What is this system known as? \
               \n A.Network Access Control (NAC) \n B.Security Information and Event Management (SIEM) \n C.Identity and Access Management (IAM) \n D.Data Loss Prevention (DLP)")

if answer == "b" or answer == "B":
    print("Good Answer!")
    score = score+1
else:
    print("Wrong!")

answer = input("11.What is the primary purpose of a Web Application Firewall (WAF)? \
                   \n A.Block malicious IP addresses \n B.Protect against SQL injection and XSS attacks \n C.Filter out spam emails \n D.Provide VPN access for remote users")

if answer == "d" or answer == "D":
    print("Correct!")
    score = score+1
else:
    print("Wrong!")

answer = input("12.What is the main difference between a worm and a virus? \
               \n A.A worm is always malicious, while a virus can be benign \n B.A virus requires user action to spread, while a worm can spread by itself \n C.A worm can be programmed, while a virus cannot \n D.A virus targets the operating system, while a worm targets applications")

if answer == "b" or answer == "B":
    print("Good Answer!")
    score = score+1
else:
    print("Wrong!")

answer = input("13.Which of the following is a type of public key infrastructure (PKI) attack where the attacker redirects the user toWhich of the following is a type of public key infrastructure (PKI) attack where the attacker redirects the user toa malicious website that appears to be legitimate? \
               \n A.Replay attack \n B.Pharming attack \n C.Session hijacking \n D.Man-in-the-Middle attack")

if answer == "c" or answer == "C":
    print("Good!")
    score = score+1
else:
    print("Incorrect!")

answer = input("14. A system administrator finds a file on a user's desktop that appears to contain a list of passwords for various company systems. What type of attack has likely occurred? \
               \n A.Password spraying \n B.Credential harvesting \n C.Rainbow table attack \n D.Birthday attack")

if answer == "a" or answer == "A":
    print("Correct!")
    score = score+1
else:
    print("Incorrect")

answer = input("15. A company has implemented a system that uses a single secure private key to encrypt and decrypt messages.What type of encryption system is this? \
               \n A.Asymmetric encryption \n B.Symmetric encryption \n C.Hash function \n D.Digital signature")

if answer == "B" or answer == "b":
    print("Correct")
    score = score+1
else:
    print("Incorrect")