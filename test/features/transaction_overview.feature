Feature: transaction overview

  As user I want to see which transactions occurred within a specific time frame.

  Scenario: List transactions
     Given a working system with example data
	  When requesting the latest transactions
	  Then all transactions within the last month are listed
	   And sorted by date descending
	   
  Scenario: List transactions within a specific time range
     Given a working system with example data
	  When requesting transactions from "1 August 2024" - "30 August 2024" 
	  Then all transactions within "August 2024" are listed
	   And sorted by date descending

  Scenario: List transactions within a specific amount range
     Given a working system with example data
	  When requesting transactions of at least "EUR" "100"
	  Then all transactions of "EUR" "100" or more within the last month are listed
	   And sorted by date descending

  Scenario: List transactions matching a description
     Given a working system with example data
	  When requesting transactions where the description contains "rent"  
	  Then all transactions with the word "rent" in the description within the last month are listed
	   And sorted by date descending
