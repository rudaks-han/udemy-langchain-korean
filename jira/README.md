usage: jql_to_csv.py [-h] [-j [JQL_query]] -u username [-p [password]]
[-n [Number_of_issues]] -U Base_URL

Calls a JQL query and export it to CSV files. We suggest that the JQL queries
end with "ORDER BY key"

optional arguments:
-h, --help            show this help message and exit
-j [JQL_query], --jql [JQL_query]
JQL query - default query is "ORDER BY key"
-u username           Username
-p [password]         Password. If parameter is not passed, the password
will be prompted
-n [Number_of_issues]
Number of issues per CSV batch. Default of 1000 in
line with Jiras default. For more details, check
https://confluence.atlassian.com/jirakb/filter-export-
only-contains-1000-issues-in-jira-
server-191500982.html
-U Base_URL, --url Base_URL
Jiras base URL. For example,
https://jira.mycompany.com