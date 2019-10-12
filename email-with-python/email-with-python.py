import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

from datetime import datetime
from os import path, remove
import configparser
import pandas as pd
import shutil

CREDENTIAL_PATH = "credential.json"
PROJECT_ID = "yourProjectID"

def bigquery_to_csv(sub_conf):
    """
    Output a csv file by reading query in config file
    Arguments:
        sub_conf {String} -- [Sub Confiq name in the confiq file]
    """
    query = config.get(sub_conf, 'query')
    filename = config.get(sub_conf, 'filename')
    dialect = config.get(sub_conf, 'dialect')

    table = pd.read_gbq(query, project_id=PROJECT_ID, dialect=dialect, private_key=CREDENTIAL_PATH)

    filename = filename + current_date.strftime("%Y%m%d") + ".csv"
    filelist.append(filename)
    table.to_csv(filename)


def delete(filename):
    if path.exists(filename):
        if path.isfile(filename):
            remove(filename)
        else: #if it is a folder
            shutil.rmtree(filename)
        print("Deleted " + filename)
    else:
        print(filename + " does not exist")


FOLDER = path.dirname(path.realpath(__file__))
CONFIG_FILE = path.join(FOLDER, "query_detail.conf")
config = configparser.RawConfigParser()
config.read(CONFIG_FILE)

current_date = datetime.now()
filelist = []

# Read all the sub confiq and output csv files
sub_conf_list = config.sections()
for sub_conf in sub_conf_list:
    bigquery_to_csv(sub_conf)

print("Reports are extracted successfully!")

# Email
msg = MIMEMultipart()
fromaddr = 'yourEmail@outlook.com'
msg['From'] = fromaddr
msg["To"] = "sender1@outlook.com,sender2@outlook.com"
msg["Cc"] = "yourEmail@outlook.com"
msg['Subject'] = "Report"

htmlEmail = """
<p> Dear Sir/Madam, <br/><br/>
    Please find the attached Report below.<br/><br/>
<br/></p>
<p> Please contact XXX directly if you have any questions. <br/>
    Thank you! <br/><br/>
    Best Regards, <br/>
    XXX </p>
<br/><br/>
<font color="red">Please do not reply to this email as it is auto-generated. </font>
"""

for f in filelist:
    f = path.join(FOLDER, f)
    with open(f, "rb") as attached_file:
            part = MIMEApplication(
                attached_file.read(),
                Name=path.basename(f)
            )
        # After the file is closed
    part['Content-Disposition'] = 'attachment; filename="%s"' % path.basename(f)
    msg.attach(part)



msg.attach(MIMEText(htmlEmail, 'html'))
server = smtplib.SMTP('smtp.office365.com', 587)
server.starttls()
server.login(fromaddr, "yourpassword")
text = msg.as_string()
server.sendmail(fromaddr, ['sender1@outlook.com','sender2@outlook.com'], text)
server.quit()

print("Email are sent successfully!")

# Delete files on server after sending them
for f in filelist:
    delete(path.join(FOLDER, f))
print("Files are deleted successfully!")
