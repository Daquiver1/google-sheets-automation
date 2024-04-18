# Google Sheets Automation with Python

This is a Python script that automates a user workflow by connecting to a Google Sheets file, extracting emails from a particular column, generating OTPs for each email, sending emails with OTPs using the SendinBlue API and SMTP, and storing the OTPs back to the corresponding email in the Google Sheets file.

## Prerequisites

Before running the script, please make sure you have the following:

- Google Sheets API credentials: You will need a JSON keyfile for authentication. You can obtain this by following the instructions at [link-to-google-sheets-api-docs](https://developers.google.com/android/management/service-account).
- After generating the JSON keyfile, rename it to "elections.json" and store it in the current directory.
- After creating service account and enabling google sheets and google drive api, add the service account email to your google sheets file as a collaborator with edit access.
- SendinBlue API credentials: You will need an API key and a URL from SendinBlue for sending emails. You can obtain these by signing up for a SendinBlue account at [link-to-sendinblue-website](https://account-app.sendinblue.com/account/login.)
- Environment variables: You will need to set up the following environment variables in the .env file (based on the provided .env.template):
  - `API_KEY`: Your SendinBlue API key
  - `SENDER_EMAIL`: Your sender email
  - `SENDER_NAME`: Your sender name
  - `SENDER_PASSWORD`: Your sender password
  - `SMTP_PORT`: SMTP port for your email provider
  - `SMTP_SERVER`: SMTP server for your email provider
  - `SUBJECT`: Subject of the email
  - `WORKSHEET_NAME`: Name of the Google Sheets worksheet
  - `JSON_KEYFILE_NAME`: Name of the JSON keyfile for Google Sheets API

## Installation

1. Clone the repository:

    ```python
    git clone https://github.com/daquiver1/google-sheets-automation.git
    ```

2. Change to the project directory:

    ```python
    cd google-sheets-automation
    ```

3. Install the required dependencies:

   ```python
    pip install -r requirements.txt
    ```

4. Rename the `.env.template` file to `.env` and update the environment variables with your own values.

## Usage

1. Run the main.py script:

2. The script will connect to the Google Sheets file using the provided credentials, extract emails from the specified column, generate OTPs for each email, send emails with OTPs using the SendinBlue API and SMTP, and store the OTPs back to the corresponding email in the Google Sheets file.

3. You can monitor the progress and check for any errors in the console output.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please create an issue or submit a pull request.

## Contact

If you have any questions or need further assistance, please contact me at cabrokwa11@gmail.com.

## QuiverTech Challenge. 
**T**ake a closer look at what seems ordinary. **H**idden messages might surprise you. **E**very detail counts when deciphering codes. **W**ith careful analysis, the secrets begin to reveal themselves. **O**bservations must be meticulous. **R**ead between the lines to find deeper meanings. **D**on't rush; patience is key. **Y**ou'll soon notice patterns emerging. **O**ften, what you seek is right in front of you. **U**nderstanding these hints can unlock new insights. **A**lways remember, the answer is closer than it appears. **R**evisit the initial clues if necessary. **E**very attempt brings you closer to the solution. **L**ook beyond the surface. **O**pen your mind to all possibilities. **O**nly then can the hidden be understood. **K**eep these thoughts in mind as you continue. **I**nspiration often comes from unexpected sources. **N**ever underestimate the power of a fresh perspective. **G**ive yourself time to absorb the information. **F**inally, the realization will dawn. **O**bviously, the word you are looking for is right there. **R**eading carefully will show it. **I**t's all about connecting the dots. **S**oon, everything makes sense. Are you inspired?.

All the best. 
