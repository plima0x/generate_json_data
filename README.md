
## What is it?
The program is used to generate a simple json data for testings. The generated json file will have the fields: 

**name**: it will be a random name from the wikipedia site https://en.wikipedia.org/wiki/List_of_most_popular_given_names.

**age**: it will be a random integer.

**hobby**: it will be a random hobby from the wikipedia site https://simple.wikipedia.org/wiki/List_of_hobbies.

**city**: it will be a random city from the wikipedia site https://en.wikipedia.org/wiki/List_of_largest_cities.

## Requirements:

Install the requests library:
```

python -m install requests

```

install the beautifulsoup4:

```

python -m pip install beautifulsoup4

```

## Getting started:

Execute the main.py and enter the number of json items that you wish to have in the json file:
```
python main.py

```
Output:

```

[+] Getting all information....

[+] Trying to get the page https://en.wikipedia.org/wiki/List_of_most_popular_given_names
[+] Page got!


[+] Extracting tags for the name
[+] Tag informations extracted


[+] Trying to get the page https://simple.wikipedia.org/wiki/List_of_hobbies
[+] Page got!


[+] Extracting tags for the hobby
[+] Tag informations extracted


[+] Trying to get the page https://en.wikipedia.org/wiki/List_of_largest_cities
[+] Page got!


[+] Extracting tags for the city
[+] Tag informations extracted

[+] All information got

Enter the number of lines that the json must have: 3

[+] Creating the json...

[+] Writing the json file output.json
[+] Json file created


```

