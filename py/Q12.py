# write a program to parse an email id to print from which email server it was sent and when (input from abcjims@gmail.com sun jan 27 20:29:15 2023) output : the email has been sent through gmail.com)
def parse_email_info(email_info):
    # Split the input string to extract email and date-time information
    parts = email_info.split()
    email = parts[2]
    date_time = " ".join(parts[3:])

    # Extract the email server from the email address
    email_server = email.split("@")[1]

    # Print the output
    print(f"The email has been sent through {email_server} on {date_time}")


# Example input
email_info = "input from abcjims@gmail.com sun jan 27 20:29:15 2023"
parse_email_info(email_info)
