# **G9: Control for quality and performance of information system: 'The Diary Project'**

This test plan for ‘The Diary Project’ includes several basic functional and performance tests, to ensure the quality and usability of the information system is maintained on an ongoing basis.

## **1. Project summary**

‘The Diary Project’ is an information system that hosts a structured dataset of personal (dummy) diary entries. It provides access to this data through a simple, web-based API and interactive user interface. Users can view, search, and filter diary entries by fields such as date, country, people mentioned, milestone events, stage of life, and the Optical Character Recognition (OCR) confidence level. *(Note: OCR confidence was discussed in detail in assignment G7).* Users cannot add or delete diary entries.

## **2. Functional Tests**

Below are two categories of tests to examine whether the ‘The Diary Project’ API behaves correctly with valid and invalid inputs.

### **2.1. Endpoint accessibility** 

The goal of this category of tests is to check the functionality of the endpoint when returning all diary entries. Once Flask is running and the local server is exposed using nGrok, copy the public HTTPS link shown in the terminal. Append */diary* to the end of the URL. It will be a variation of the following address: https://abc123.ngrok-free.app/diary. 

•	Test that a GET request (i.e., an allowed action) returns a list of entries in JSON format.
•	Test that the GET request returns at least 200 entries.
•	Test whether the user can accomplish actions that are not allowed, such as POST or DELETE. This request should alert the user by returning an error message such as *405 Method Not Allowed*.

### **2.2. Endpoint Filtering**

The goal of this category of tests is to check the filtering functionality. Append */filter* to the end of the URL: https://abc123.ngrok-free.app/filter. 

•	Test that an empty filter request returns all entries.
•	Test that a single filter returns a specific entry as expected (i.e., change the ‘country’ filter to ‘Australia’, and check that all diary entries with an ‘Australia’ tag are returned. The relevant URL is: https://abc123.ngrok-free.app/filter?country=australia)
•	Test that a combination of filters returns specific entries as expected (i.e., country + OCR level, theme + people mentioned).
•	Test using abnormal inputs in open-text fields to ensure errors are handled smoothly (i.e, OCR_confidence = ‘hello’, date = 1902/13/13). 
•	Test that filters do not silently fail (i.e., if no entries match the user’s GET request, return a helpful message like ‘No entries found.’). This alerts the user that they should modify their query.

## **3. Performance Tests**

As the API will only be used by a small number of users, it is not essential to conduct rigorous stress testing. However, as the dataset grows, it is important to test regular response time and filter efficiency tests. These tests are outlined below.

### **3.1. Response Time** 

•	Test that the GET request returns data within an acceptable time threshold. For the current size of ‘The Diary Project’ file, the definition of ‘acceptable’ is under 1 second for 100+ entries.

### **3.2. Filter Efficiency** 

•	Test whether the user can use a realistic combination of multiple filters, and that this filtering logic does not add a noticeable delay. If there is a prolonged delay (i.e., more than 20 seconds), the user should be alerted by a message such as *Request Timeout*.

## **4. Automation**

In the pilot phase of ‘The Diary Project’, these functional and performance tests will be conducted manually. In subsequent phases, these tests may be automated (i.e., using the Python testing framework (pytest), or other API testing tools such as Postman or JMeter).
