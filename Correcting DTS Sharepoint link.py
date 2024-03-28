import re

# Example of a corrupted link (replace with your own)
corrupted_link = "Ingkarninthi.docx"


def repair_corrupted_link(corrupted_link):
    # regex to match the link structure
    pattern = re.compile(
        r".*?(personal/\w+_unisa_edu_au)/([A-Za-z0-9_\-]+)\?e=([A-Za-z0-9]+)"
    )
    match = pattern.search(corrupted_link)

    if not match:
        return "The link could not be repaired because it doesn't match the expected pattern."

    # Extracted components
    user_path = match.group(1)
    document_id = match.group(2)
    access_token = match.group(3)

    # Reconstruct the URL using the new base URL provided
    base_url = "https://mymailunisaedu-my.sharepoint.com"
    repaired_link = f"{base_url}/:w:/g/{user_path}/{document_id}?e={access_token}"

    return repaired_link


# Repair the link
repaired_link = repair_corrupted_link(corrupted_link)
print(repaired_link)
