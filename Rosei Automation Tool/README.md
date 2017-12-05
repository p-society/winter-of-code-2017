# IIIT-Bh Rosei Automation Tool (RAT) (With GUI).
###### Last Updated on 28 March 2017.

### Prerequisites for RAT.
* Selenium
* Chrome Webdriver (ChromeDriver)
* Tkinter

## Selenium
Installing Selenium is mandatory for the program to run. To download and install selenium, using pip is recommended.

`pip install selenium`

pip comes prebundled with Python 3.

## ChromeDriver
Please visit [ChromeDriver - WebDriver for Chrome](https://sites.google.com/a/chromium.org/chromedriver/) website for downloads.

## Tkinter
The Tkinter module comes preinstalled with both Python 2 and Python 3.

# Format for Preferences File
The preferences file can either be a text file (.txt) or a binary file (.dat). The preferences file **must contain four lines**. The first line shall contain the username (BXXXXXX). The second line shall contain the password. The third line shall contain the Roseighara 1 food preferences with V or N prefixed to the food codes and every meal preference must be separated by a space. The fourth line shall contain the Roseighara 2 food preferences in similar format as specified above.

## Sample preference file
**A preference file must contain four lines.**<br /><br />
`BX16XXX`<br />
`passwordgoeshere`<br />
`V112 V113 V122 V123`<br />
`V232 V233 V242 V243`<br /><br />

**NOTE: If the user doesn't want to book coupons in any of the Roseigharas, then the corresponsing line may be left blank (line 3 can be left blank for no coupons from Roseighara 1 and line 4 can be left blank for no coupons from Roseighara 2).**
***

# Issues
### The program sometimes gets stuck at the 'booking complete' webpage when the coupons are to be booked at both the roseigharas. A temporary fix by using `sleep(2)` has been made for this issue at line #95, although it doesn't work everytime.

#### Distributed under MIT License.
#### Copyright © 2017 Ravi Teja Gannavarapu.
