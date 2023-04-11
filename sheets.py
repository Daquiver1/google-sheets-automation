"""Google sheets API"""
import os
from typing import List

from dotenv import load_dotenv

load_dotenv()

import gspread
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

from emails import send_bulk_email, send_email_via_send_in_blue, send_single_email
from util import is_variable_none

load_dotenv()
JSON_KEYFILE_NAME = os.getenv("JSON_KEYFILE_NAME")
WORKSHEET_NAME = os.getenv("WORKSHEET_NAME")

required_variables = [WORKSHEET_NAME, JSON_KEYFILE_NAME]

if is_variable_none(required_variables):
    raise ValueError("One or more env variables are missing.")

# Connect to Google Sheets
scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/spreadsheets.readonly",
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

token_cred = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEYFILE_NAME, scope)
client = gspread.authorize(token_cred)
worksheet = client.open(WORKSHEET_NAME).sheet1


def read_emails():
    """
    This function reads and returns a list of email addresses from the second column of a worksheet,
    excluding the first value which is the column title.

    Returns:
      The function `read_emails` is returning a list of email addresses. The email addresses are
    extracted from the second column of a worksheet, with the first value (column title) removed from
    the list.
    """
    values_list = worksheet.col_values(2)
    values_list.pop(0)  # First value is column title
    return values_list


def add_otp_to_sheet(student_code: List[str]):
    """
    Updates a Google Sheets worksheet with a list of student codes in the "J" column.

    Args:
      student_code (List): The parameter `student_code` is expected to be a list of strings, where each
    string represents a unique code for a student.
    """
    for code_index in range(len(student_code)):
        worksheet.update(f"j{code_index+2}", student_code[code_index])
