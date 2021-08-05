from SAF.email.imap_client import IMAPClient
from SAF.email.gmail_client import GmailClient

from selenium.common.exceptions import *
import logging
import time
import re


class NoEmailException(Exception):
    pass

class CONST():
    GMAIL_IMAP = "imap.gmail.com"
    SENDER_EMAIL = "donotreply@hpeprint.com"
    GMAIL_SUBJECT = "ePrint mobile registration"

class GmailImap(object):
    def __init__(self, username, pwd):
        """
        :type cfg: MobiConfig
        :param cfg:
        """
        self.gmail = IMAPClient(CONST.GMAIL_IMAP,username, pwd)

    def delete_messages_pin_code(self):
        """
        Delete all messages about pin code
        """
        self.gmail.delete_emails_by_sender_email(CONST.SENDER_EMAIL)

    def get_subject_with_sender_email(self, sender_email):
        """
        Get Subject content from an email with its sender_email

        :param sender_email: sender's email
        :return: Subject content
        """
        subject_content = self.gmail.get_newest_unread_message_with_sender_email(sender_email=sender_email)[0]
        return subject_content

    def delete_messages_with_sender_email(self, sender_email):
        """
        Delete all massages corresponding to sender
        """
        self.gmail.delete_emails_by_sender_email(sender_email=sender_email)


class GmailAPI(object):
    def __init__(self, credential_path):
        """
        Due to security reasons we do not cache any Google API tokens in the test repository.
        If you want a copy of the API token for the qamobiauto@gmail.com account 
        Please contact Hai Tran
        """
        self.gmail = GmailClient(credential_path =credential_path)

    def send_email(self, to='', subject='', content='', file_paths=[]):
        """
        Send an email

        :param to: recipient
        :type to: str
        :param subject: subject of the email
        :type subject: str
        :param content: content of the email
        :type content: str
        :param file_paths: file path of the attachment
        :type file_paths: list
        :return: message: a message resource
        """
        if file_paths:  # has attachment
            message = self.gmail.create_message_with_attachment(
                to=to, subject=subject, message_text=content, file_paths=file_paths)
        else:  # empty = no attachment
            message = self.gmail.create_message(to=to, subject=subject, message_text=content)
        draft = self.gmail.create_draft(message)
        message = self.gmail.send_draft(draft)
        return message

    def mark_email_as_read(self, msg_id):
        """
        Mark the message as read.

        :param msg_id: message id
        :type msg_id: str
        """
        self.gmail.modify_message_label(msg_id=msg_id, remove_label=['UNREAD'])

    def mark_email_as_unread(self, msg_id):
        """
        Mark the message as unread.

        :param msg_id: message id
        :type msg_id: str
        """
        self.gmail.modify_message_label(msg_id=msg_id, add_label=['UNREAD'])

    def delete_email(self, msg_id):
        """
        Move the message into Trash.

        :param msg_id: message id : [{'id': "","threadid": ""},{'id': "","threadid": ""},...]
        :type msg_id: str
        """
        for id in msg_id:
            self.gmail.trash_message(msg_id=id['id'])

    def delete_specified_email(self, msg_id):
        """
        Move the message into Trash.

        :param msg_id: message id : [{'id': "","threadid": ""},{'id': "","threadid": ""},...]
        :type msg_id: str
        """
        self.gmail.trash_message(msg_id=msg_id)

    def get_attachments(self, msg_id, store_dir=''):
        """
        Retrieve the attachments of a message; if store_dir is not specified, just return the names.

        :param msg_id: The ID of the Message containing attachments.
        :type msg_id: str
        :param store_dir: The directory used to store attachments.
        :type store_dir: str
        :return files: a list of file names for the attachments
        """
        return self.gmail.get_attachment(msg_id, store_dir)

    def get_eprint_pin_code(self, clear_msg=True):
        """
        Extract the PIN code from the eprint activation email;
        assuming it's the latest unread email from CONST.SENDER_EMAIL.

        :param clear_msg: whether to mark email as read and move it to trash at the end or not
        :type clear_msg: bool
        :return: PIN: PIN code from activation email
        """
        timeout = time.time() + self.timeout
        msgs = []
        while time.time() < timeout:
            msgs = self.gmail.list_messages_matching_query('is:unread from:' + CONST.SENDER_EMAIL)
            if msgs:
                msg = self.gmail.get_message(msgs[0]['id'], 'raw')
                content = self.gmail.decode_raw_message(msg)
                PIN = content[content.rfind(':')+2:content.rfind(':')+6]
                # logging.info('content: ' + content)
                logging.info('PIN: ' + PIN)
                if clear_msg:
                    self.mark_email_as_read(msgs[0]['id'])
                    self.delete_specified_email(msgs[0]['id'])
                return PIN
            else:
                time.sleep(self.poll_frequency)
        raise TimeoutException("ePrint PIN Code email was not received in {} seconds".format(self.timeout))

    def get_instagram_security_code(self, clear_msg=True):
        """
        Get Security Code of Instagram
        It always gets the latest unread email for this security code
        :param clear_msg:
        :return: security code
        """
        timeout = time.time() + 60
        while time.time() < timeout:
            msgs = self.gmail.list_messages_matching_query('is:unread from: security@mail.instagram.com')
            if msgs:
                msg = self.gmail.get_message(msgs[0]['id'], 'raw')
                content = self.gmail.decode_raw_message(msg)
                if clear_msg:
                    self.mark_email_as_read(msgs[0]['id'])
                    self.delete_specified_email(msgs[0]['id'])
                return re.search("[0-9]{6}", content).group(0)
            else:
                time.sleep(5)       # break 5 seconds before next checking.
        raise TimeoutException("Security Code of Instagram email was not received in 60 seconds")

    def get_hpid_verification_code(self, to, clear_msg=True):
        """
        Get Verification Code for HPID
        It always gets the latest unread email for this security code
        :param clear_msg: delete the email after getting code
        :return: verification code
        """
        timeout = time.time() + 60
        while time.time() < timeout:
            msgs = self.search_for_messages(q_to=to, q_from="HP ID Support", q_unread=True)
            if msgs:
                msg = self.gmail.get_message(msgs[0]['id'], 'raw')
                content = self.gmail.decode_raw_message(msg)
                self.mark_email_as_read(msgs[0]['id'])
                if clear_msg:
                    self.delete_specified_email(msgs[0]['id'])
                return re.search(">[A-Z0-9]{6}<", content).group(0)[1:-1]
            else:
                time.sleep(5)       # break 5 seconds before next checking.
        raise NoEmailException("Verification code of HPID email was not received in 60 seconds")

    def delete_hpid_verification_code_email(self, to):
        """
        Delete Email for HPID verification code
        :param to: 'to' email
        """
        timeout = time.time() + 60
        while time.time() < timeout:
            msgs = self.gmail.list_messages_matching_query('is:unread from: no-reply@stg.cd.id.hpcwp.com to: {}'.format(to))
            if msgs:
                self.delete_email(msgs)
                return True
            else:
                time.sleep(5)       # break 5 seconds before next checking.
        return False
        
    def delete_all_messages_from_inbox(self):
        """
        Remove all messages in Inbox.
        """
        msgs = self.gmail.list_messages_matching_query('in:inbox')
        logging.info('Removing {} messages...'.format(len(msgs)))
        for msg in msgs:
            self.gmail.trash_message(msg['id'])

    def search_for_messages(self, q_to='', q_from='', q_subject='', q_label='', q_unread=False, q_content='', timeout=3):
        """
        Search for all Messages matching the criteria.

        :param q_to: recipient's email address
        :type q_to: str
        :param q_from: sender's email address
        :type q_from: str
        :param q_subject: subject of email
        :type q_subject: str
        :param q_label: tags/labels of the email
        :type q_label: str
        :param q_unread: whether the email is unread or not
        :type q_unread: bool
        :param q_content: any words from within the email
        :type q_content: str

        :return messages: List of Messages IDs that match the criteria of the query. Note that the
                          returned list contains Message IDs, you must use get with the
                          appropriate ID to get the details of a Message; or [].
        """
        start_time = time.time()
        while time.time() < start_time + timeout:

            message_id = self.gmail.list_messages_matching_query(self.gmail.query_builder(
            q_to=q_to, q_from=q_from, q_subject=q_subject, q_label=q_label, q_unread=q_unread, q_content=q_content))

            if message_id:
                logging.info("{}:[Message Found! ID: {}]".format(self.search_for_messages.__name__,message_id ))
                return message_id

        raise TimeoutException("Took longer than {} seconds to retrieve email from Gmail".format(timeout))

    #******************************************************************************************************************
    #                                   Send your own email and delete what you sent                                  *
    #******************************************************************************************************************
    def send_email_with_keyword(self, to='', subject='', content='', keyword = ''):
        """
        Send an email

        :param to: recipient
        :type to: str
        :param subject: subject of the email
        :type subject: str
        :param content: content of the email
        :type content: str
        :return: message: a message resource
        """
        keyword = self.cfg.get("DEVICE", "udid")
        message = self.gmail.create_message(to=to, subject=subject, message_text="{}_{}".format(content, keyword))
        draft = self.gmail.create_draft(message)
        message = self.gmail.send_draft(draft)
        return message