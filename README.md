# **IMT 542: Final Project: ‘The Diary Project’**

## **1. Overview**

This document summarizes the key files contained in this GitHub repository, all of which relate to my IMT 542 Final Project. I (Tara Hulcome) am presenting ‘The Diary Project’, which explores the end-to-end process for creating a new information product that transforms my personal diary collection into a machine-readable structure.

## **2. Key Working Documents**

This section contains seven working files that provide evidence of the project development and iteration process over the Spring 2025 quarter. These include:

**2.1. [G3_Ideating_Information_Story](2.1_G3_Ideating_Information_Story.json)**

Overview: This file provides a brief overview of my early ideation about ‘The Diary Project’.

Last Updated: 15 April 2025

Format: JSON

**2.2. [G4_Initial_Information_Story](2.2_G4_Initial_Information_Story.pdf)**

Overview: This file provides a visual summary of ‘The Diary Project’ information story, including wireframes, access considerations, and information architecture.

Last Updated: 22 April 2025

Format: PDF

**2.3. [G5_FAIR_Assessment](2.3_G5_FAIR_Assessment.txt)**

Overview: This file describes how my new information structure intersects with the FAIR (Findable, Accessible, Interoperable, Reusable) model. 

Last Updated: 28 April 2025

Format: TXT

**2.4. [G6_Availability_Limitations_Ethics_Societal_Impact_Assessment](2.4_G6_Availability_Limitations_Ethics_Societal_Impact_Assessment.html)**

Overview: This file contains an Availability, Limitations, Ethics and Societal Impact analysis to accompany my new information product.

Last Updated: 7 May 2025

Format: HTML

**2.5. [G7_Improved_Information_Structure_Format](2.5_G7_Improved_Information_Structure_Format.pdf)**

Overview: This file contains samples of the existing information structure and new proposed structure. It also describes how my new information structure promotes quality maintenance and information security.

Last Updated: 14 May 2025

Format: PDF

**2.6. [G8_Improved_Access_Methodology](2.6_G8_Improved_Access_Methodology.md)**

Overview: This file describes how to access the first version of my information structure, including specific instructions. (Note that these instructions were updated on 5 June 2025, to reflect the final version of my information structure – see *Section 5* below).

Last Updated: 21 May 2025

Format: MD

**2.7. [G9_Test_Plan](2.7_G9_Test_Plan.md)**

Overview: This file contains a test plan for ‘The Diary Project’, including several basic functional and performance tests. It has been updated to reflect feedback regarding inclusion of specific monitoring and alerts, automated actions, and an ongoing maintenance schedule.

Last Updated: 6 June 2025

Format: MD

## **3. Key Project Artifacts**

**3.1. [Project_Artifact_A_dummy_diary_entries_list](3.1_Project_Artifact_A_dummy_diary_entries_list.json)**

Overview: This file contains the 300 dummy diary entries, structured in line with my new taxonomy and generated with the assistance of artificial intelligence (AI) tools (Google Gemini Pro).

Format: JSON

**3.2. [Project_Artifact_B_Python_code](3.2_Project_Artifact_B_Python_code.py)**

Overview: This file contains the Python code used to build my Flask-based API, generated with the assistance of Google Gemini Pro.

Format: Python

**3.3. [Project_Artifact_C_User_Interface_Code](3.3_Project_Artifact_C_User_Interface_Code.html)**

Overview: This file contains the HTML code used to build my front-end interface that allows users to filter entries via form fields (e.g., country, date, OCR confidence) and visualize the results. This code was generated with the assistance of Google Gemini Pro.

Format: HTML

## **4. Final Presentation Files**

**4.1. [Final_Presentation_Slides](4.1_FINAL_Presentation_Slides.pdf)**

Overview: This file contains the slide deck from my in-class presentation.

Last Updated: 3 June 2025

Format: PDF

**4.2. [Final_Presentation_Speaking_Notes](4.2_FINAL_Presentation_Speaking_Notes.pdf)**

Overview: This file contains the accompanying speaking notes from my in-class presentation.

Last Updated: 3 June 2025

Format: PDF

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

-	Use the dropdowns and input fields to: (a) Search for entries written in a specific country; (b) Narrow down by date (on or after a given date); (c) View entries with high OCR confidence; or (d) Explore entries mentioning specific people.

-	Each result includes key fields such as country, entry text, place, and date.

**Step 5: Refresh the data for updates**

-	If the underlying JSON file is updated on the server, refresh your browser page to see the latest content.

**Step 6: Understand What You Can and Can’t Do**

-	The API currently supports GET requests only.

-	You can view and download data, but you cannot edit or add entries via the browser or API.

-	Enjoy exploring Tara’s Secret Diary Entries (…but ssshhhh, don’t tell!)

## **6. Video Tutorials**

These three URL addresses link to video tutorials demonstrating how to access the endpoint through the API, as well as my vision for a more sophisticated front-end user interface.

**Video Tutorial 1**

This [tutorial](https://drive.google.com/file/d/1IUZbwNhP5qxJoJdUMVOUZTbvMxPJDPpN/view?usp=drive_link) shows how to access the endpoint through the API (based on my first iteration).

**Video Tutorial 2**

This [tutorial](https://drive.google.com/file/d/1atG-FTf1D-8lUEU5Y6pxdSNwruLZyQa1/view?usp=drive_link) shows how to access the endpoint through the API (based on my second / final iteration).

**Video Tutorial 3**

This [video](https://drive.google.com/file/d/1eOnymmoOeDxR3uE3jtpK3FJyqFwFfOqY/view?usp=sharing) introduces a functional prototype with a more sophisticated front-end user interface. It was created with the assistance of Lovable AI Coding.

## **7. Cloud Hosting**

Note that there is a ‘.github/workflows’ folder, which relates to my (unsuccessful) attempt to add an Azure Web App (cloud service provider) to host my new information structure. I aim to trouble-shoot and complete this task after project submission
