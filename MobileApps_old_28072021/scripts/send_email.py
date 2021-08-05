import os
import zipfile
import smtplib
import shutil
import time
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.message import EmailMessage
from MobileApps.libs.ma_misc import ma_misc
from argparse import ArgumentParser

class Gather_Screenshots:

    def __init__(self):
        self.parser = ArgumentParser()
        self.parser.add_argument("--folder-ss", dest="foldername",help="folder containing ss")
        self.args = self.parser.parse_args()
        self.path = self.args.foldername
        self.subject = "Screenshots from Android Devices *Automated Email-DO NOT REPLY*"
        self.text = "Attachment should contain screenshots for Android Devices. For queries contact nachiket.wattamwarm@hp.com" 
        self.recipients = ['daixuefeng@beyondsoft.com','nachiket.wattamwarm@hp.com']
        system_cfg = ma_misc.load_system_config_file()
        self.root_path = system_cfg["bulk_image_root"]

    def list_of_recipients(self):
        return self.recipients

    def zip_screenshots(self,path,zipfile):
        for root,_,files in os.walk(path):
            for file in files:
                zipfile.write(os.path.join(root,file))

    def send_message(self,attachment=None):
        # build message contents
        msg = MIMEMultipart()
        msg['Subject'] = str(self.subject)
        msg.attach(MIMEText(self.text))
        zippedAttachments = MIMEBase('application', 'zip')
        zf = open(attachment,'rb')
        zippedAttachments.set_payload(zf.read())
        encoders.encode_base64(zippedAttachments)
        file_name = attachment.split("/")[-1]
        zippedAttachments.add_header('Content-Disposition', 'attachment', 
               filename=file_name)
        msg.attach(zippedAttachments)
        return str(msg)
    
    def delete_screenshots(self):
        try:
            print("root path ",self.root_path+'/'+self.path)
            shutil.rmtree(self.root_path+'/'+self.path)
            print("zip path",self.root_path+'/Android_screenshots.zip')
            os.remove(self.root_path+'/Android_screenshots.zip')
        except OSError as e:
            print("Error: %s : %s" %("Folder Deletion Error",e.strerror))


if __name__ == "__main__":
    Gather_Screenshots = Gather_Screenshots()
    screenshots_captured = Gather_Screenshots.root_path+'/'+Gather_Screenshots.path
    Gather_Screenshots.zip_screenshots(screenshots_captured,zipfile.ZipFile(Gather_Screenshots.root_path+'/Android_screenshots.zip','w',zipfile.ZIP_DEFLATED))
    smtp = smtplib.SMTP('localhost', port=25)
    try:
        smtp.sendmail(to_addrs=Gather_Screenshots.list_of_recipients(),msg=Gather_Screenshots.send_message(attachment=(Gather_Screenshots.root_path+'/Android_screenshots.zip')),from_addr="nachiket.wattamwarm@hp.com")
        time.sleep(3)
    except:
        raise Exception("Sending email failed")
    Gather_Screenshots.delete_screenshots()
