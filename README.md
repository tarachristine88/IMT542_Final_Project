# **IMT 542: Final Project: ‘The Diary Project’**

## **1. Description**

This document summarizes the key files contained in this GitHub repository, all of which relate to my IMT 542 Final Project. I (Tara Hulcome) am presenting ‘The Diary Project’, which explores the end-to-end process for creating a new information product that transforms my personal diary collection into a machine-readable structure.

## **2. Key Working Documents**

The files containing titles that begin with ‘G#’ are working files that provide evidence of the project development and iteration process over Spring 2025 quarter. These include:

**2.1. G3_Ideating_Information_Story**

Overview: This file provides a brief overview of my early ideation about ‘The Diary Project’.

Last Updated: 15 April 2025

Information Format: JSON

**2.2. G4_Initial_Information_Story**

Overview: This file provides a visual summary of ‘The Diary Project’ information story, including wireframes, access considerations, and information architecture.

Last Updated: 22 April 2025

Information Format: PDF

**2.3. G5_FAIR_Assessment**

Overview: This file describes how my new information structure intersects with the FAIR (Findable, Accessible, Interoperable, Reusable) model. 

Last Updated: 28 April 2025

Information Format: TXT

**2.4. G6_Availability_Limitations_Ethics_Societal_Impact_Assessment**

Overview: This file contains an Availability, Limitations, Ethics and Societal Impact analysis to accompany my new information product.

Last Updated: 7 May 2025

Information Format: HTML

**2.5. G7_Improved_Information_Structure_Format**

Overview: This file contains a sample of the existing information structure as well as a sample of the new proposed structure I’ve developed. It also describes how my new information structure will promote quality maintenance and information security.

Last Updated: 14 May 2025

Information Format: PDF

**2.6. G8_Improved_Access_Methodoloy**

Overview: This file describes how to access my new information structure, including specific instructions.

Last Updated: 21 May 2025

Information Format: MD

**2.7. G9_Test_Plan**

Overview: This file contains a test plan for ‘The Diary Project’, including several basic functional and performance tests.

Last Updated: 30 May 2025

Information Format: MD

## **3. Key Project Artifacts**

**3.1. Project_Artifact_A_dummy_diary_entries_list.json**:  

**Overview**: This file contains the 300 dummy diary entries, structured in line with my new taxonomy and generated using artificial intelligence (AI) tools (Google Gemini Pro).

**Information Format**: JSON

**3.2. Project_Artifact_B_Python_code.py**: 

**Overview**: This file contains the Python code used to build my Flask-based API, generated with the assistance of Google Gemini Pro.

**Information Format**: Python

**3.3. Project_Artifact_C_User_Interface_Code**:

**Overview**: This file contains the HTML code used to build my front-end interface that allows users to filter entries via form fields (e.g., country, date, OCR confidence) and visualize the results.

**Information Format**: HTML

## **4. Final Presentation Files**

**4.1. FINAL_Presentation_Slides **:

**Overview**: This file contains the slide deck from my in-class presentation.

**Last Updated**: 3 June 2025

**Information Format**: PDF

**4.2. FINAL_Presentation_Speaking_Notes **:

**Overview**: This file contains the accompanying speaking notes from my in-class presentation.

**Last Updated**: 3 June 2025

**Information Format**: PDF

## **5. Access Instructions**

This section provides updated instructions (as at 5 June 2025) for how to access my new information structure, building on the details provided in G8.

**Step 1: Retrieve public API URL**

-	Once your Flask server is running and exposed using nGrok, copy the public URL shown in your terminal (i.e., https:// ee80-193-37-33-62.ngrok-free.app). This is your public access point.

**Step 2: Access the Data Endpoint**

-	To view the raw diary data, append /diary to the URL (i.e., https:// ee80-193-37-33-62.ngrok-free.app/diary). Paste this URL into your web browser.

**Step 3: Explore the Web Interface**

-	Navigating to the base URL in your browser will load the front-end interface.
-	This interface allows you to filter diary entries by country, date, OCR confidence, and people mentioned.

**Step 4: Filter and Experiment with the Data**

-	Use the dropdowns and input fields to:
o	Search for entries written in a specific country
o	Narrow down by date (on or after a given date)
o	View entries with high OCR confidence
o	Explore entries mentioning specific people

-	Each result includes key fields like:
o	country, entry text, place, and date.

**Step 5: Refresh the data for updates**

-	If the underlying JSON file is updated on the server, simply refresh your browser page to see the latest content.

**Step 6: Understand What You Can and Can’t Do**

-	The API currently supports GET requests only.

-	You can view and download data, but you cannot edit or add entries via the browser or API.

-	Enjoy exploring Tara’s Secret Diary Entries (…but ssshhhh, don’t tell!)

## **6. Cloud Hosting**

Note that there is a ‘.github/workflows’ folder, which relates to my (unsuccessful) attempt to add an Azure Web App (cloud service provider) to host my new information structure. I aim to trouble-shoot and complete this task after project submission.
