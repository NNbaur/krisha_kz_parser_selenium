# krisha_kz_parser_selenium

### Description

______
Parser on selenium and beautifulsoup4 for the most popular website for the sale of real estate in Kazakhstan. Parser imitate behaviour of default user by using selenium to avoid blocking cause of a large number of requests to the server. Then get required info from ads with beautifulsoup4 and stored it to excel file with openpyxl.

### Features

______
* Application is configured to work with proxy
* Filter offers with flats by number of rooms and city
* Parses the following information from ads: location of flat, title of ad, price, description, type of building, floor, live square, residential complex, built year.
* Received information is stored in an excel spreadsheet(.xlsx)
* Parser created for chrome on Windows, but it's simply changed to other browsers and OS


### Install

______

Run the following commands to use locally:

```
$ git clone https://github.com/NNbaur/krisha_kz_parser_selenium
```

or

```
pip install git+https://github.com/NNbaur/krisha_kz_parser_selenium.git
```



### How to use

______

#### 1) You need to fill the file ("proxy/proxy_list.json") with proxy data. 
Structure of file is:
[{"proxy": "https://username:password@ip:port", "user-agent":user_agent}, 
{"proxy": "https://username:password@ip:port", "user-agent":user_agent}, ...]

Enter username, password, ip, port and user-agent. You can see an example of completed file "proxy/proxy_list.json".
Please choose a good quality proxy. The speed and quality of the parser's work depends on this. One of the best options would be proxy with HTTPS and chrome support, located in Kazakhstan/Uzbekistan/Russia.
#### 2) ...
#### 3) ...
#### 4) ...
...
