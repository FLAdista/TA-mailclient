[mail://<name>]
* The name of the stanza should be an email address which would be used to connect to the server.

protocol = [POP3|IMAP]
* The protocol to be used to fetch emails from the server

mailserver = <value>
* This is the mailserver to fetch mails from

password = <value>
* The password for the account provided in the stanza name

is_secure = <bool>
* This determines if POPS/IMAPS should be used.

mailbox_cleanup = [delete,delayed,readonly]
* This determines if the mails should be one of the following:
 * delete: deleted as they are indexed
 * delayed: deleted on next connection to the mailbox after verifying that the mail was indexed
 * readonly: mails will not be deleted. It will be read and left in the mailbox.
* If this is not set, the default option used will be readonly

interval = [<number>|<cron schedule>]
* This inherits the interval parameter from the Splunk inputs.
* This should be set to occur frequently, as it fetches a maximum of 20 emails for each run.

include_headers =  <bool>
* This determines if email headers should be included.
