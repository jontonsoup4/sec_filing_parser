# Purpose:
Takes an online SEC filing, turns it into a txt document and parses that document for the start and stop index of paragraphs containing a `$`. The resulting index is then put into a new document for reference. This script creates a folder using the last indices of the url provide (if the folder is not already created) and outputs two files. `document.txt` is the filing in txt format and `paragraph.txt` is the resulting index.

# Requirements:
beautifulsoup4==4.4.1
html2text==2015.6.21
requests==2.7.0

# Running:
python3 sec_filing.py

When prompted, paste the desired url to parse.

example url: http://www.sec.gov/Archives/edgar/data/54473/000005447314000007/kcli-ex10o_20131231x10k.htm

# Testing:
index_test.py is an added test to make sure indexes are correct. sec_filing.py needs to have already created the resulting files in order to test. When run, input the url and the start/stop index values that you wish to check.

# File breakdown
Dependencies.txt - required modules

index_test.py - index test

kcli-ex10o_20131231x10k - example folder and files created sec_filing.py

README.md - a read with appropriate information

sec_filing.py - main script
