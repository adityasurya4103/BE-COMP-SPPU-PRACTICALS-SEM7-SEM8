import re

def matchre(data, *args):
    for regstr in args:
        matchObj = re.search(regstr + '.*', data, re.M | re.I)
        if matchObj:
            print(matchObj.group(0).lstrip().rstrip())
        else:
            print("No ", regstr, "found")

# Function to extract additional details
def extract_message_id(data):
    message_id_pattern = r'(?<=Message-ID: ).*'
    message_id = re.search(message_id_pattern, data, re.I)
    if message_id:
        return message_id.group(0).lstrip().rstrip()
    else:
        return "No Message-ID found"

def extract_received_from(data):
    received_pattern = r'(?<=Received: from ).*?(?=\))'
    received_from = re.findall(received_pattern, data, re.I)
    if received_from:
        return received_from[-1].lstrip().rstrip()
    else:
        return "No Received from details found"

def extract_received_ip(data):
    received_ip_pattern = r'\[([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)\]'
    received_ip = re.findall(received_ip_pattern, data, re.I)
    if received_ip:
        return received_ip[-1].lstrip().rstrip()
    else:
        return "No Received IP found"

def extract_subject(data):
    subject_pattern = r'(?<=Subject: ).*'
    subject = re.search(subject_pattern, data, re.I)
    if subject:
        return subject.group(0).lstrip().rstrip()
    else:
        return "No Subject found"

def extract_dkim_signature(data):
    dkim_signature_pattern = r'(?<=DKIM-Signature: ).*'
    dkim_signature = re.search(dkim_signature_pattern, data, re.I)
    if dkim_signature:
        return dkim_signature.group(0).lstrip().rstrip()
    else:
        return "No DKIM Signature found"

def extract_content_transfer_encoding(data):
    cte_pattern = r'(?<=Content-Transfer-Encoding: ).*'
    cte = re.search(cte_pattern, data, re.I)
    if cte:
        return cte.group(0).lstrip().rstrip()
    else:
        return "No Content Transfer Encoding found"

def extract_date(data):
    date_pattern = r'(?<=Date: ).*'
    date = re.search(date_pattern, data, re.I)
    if date:
        return date.group(0).lstrip().rstrip()
    else:
        return "No Date found"

def extract_mime_version(data):
    mime_version_pattern = r'(?<=MIME-Version: ).*'
    mime_version = re.search(mime_version_pattern, data, re.I)
    if mime_version:
        return mime_version.group(0).lstrip().rstrip()
    else:
        return "No MIME Version found"

def extract_senders_and_receivers(data):
    senders = re.findall(r'(?<=From: ).*', data, re.I)
    receivers = re.findall(r'(?<=To: ).*', data, re.I)
    return senders, receivers

def extract_dkim(data):
    dkim_pattern = r'(?<=DKIM-Signature: ).*'
    dkim = re.search(dkim_pattern, data, re.I)
    if dkim:
        return dkim.group(0).lstrip().rstrip()
    else:
        return "No DKIM found"

def extract_spf(data):
    spf_pattern = r'(?<=Received-SPF: ).*'
    spf = re.search(spf_pattern, data, re.I)
    if spf:
        return spf.group(0).lstrip().rstrip()
    else:
        return "No SPF found"

def display_analysis_results(data):
    print("\n**********************************************************************\n")
    print("\nAdditional Extracted Details:")
    print("\nMessage ID:")
    print(extract_message_id(data))
    print("\nReceived from:")
    print(extract_received_from(data))
    print("\nSubject:")
    print(extract_subject(data))
    print("\nReceived IP:")
    print(extract_received_ip(data))
    print("\nDKIM Signature:")
    print(extract_dkim_signature(data))
    print("\nContent Transfer Encoding:")
    print(extract_content_transfer_encoding(data))
    print("\nDate:")
    print(extract_date(data))
    print("\nMIME Version:")
    print(extract_mime_version(data))
    
    senders, receivers = extract_senders_and_receivers(data)
    print("\nSenders:")
    for sender in senders:
        print(sender)
    
    print("\nReceivers:")
    for receiver in receivers:
        print(receiver)
    
    print("\nDKIM:")
    print(extract_dkim(data))
    print("\nSPF:")
    print(extract_spf(data))
    print("\n**********************************************************************\n")

# Main section to read file and call the functions
def main():
    # Get file input
    filename = input("Enter the path for the email header file: ")
    #filename = "/content/input.txt"  # Hardcoded file path

    with open(filename, "r") as fo:
        data = fo.read()

    print("Extracted Details:")
    matchre(data, "MIME-version", "Date:", "Subject:", "Delivered-to:", "From:", "^To:")
    display_analysis_results(data)

if __name__ == "__main__":
    main()
