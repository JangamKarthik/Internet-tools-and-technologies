def merge_mails(mail_list):
    return '; '.join(mail_list)

mails = input("Enter email addresses separated by spaces: ").split()

merged_mails = merge_mails(mails)
print(f"Merged email addresses: {merged_mails}")
