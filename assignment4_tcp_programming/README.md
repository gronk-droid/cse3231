### Assignment 4 - TCP Programming
For this assignment, you will make a TCP connection to a web server to retrieve two different HTML pages and display the text of those pages on the screen.  You do not have to render them as web pages, just display the text you receive. For this assignment, you have a choice of C/C++, Java or Python.  However, for both parts, the connection to the web server must be made using the language's socket API, not a specialized class library or API (like Python's HTTP.client or Java's HttpClient). You can use any method to parse the text to find the second URL (substring search, find(), etc.).

There are two parts to the assignment and each one will be graded separately, so if you only get the first part working, you will get credit for that part.  However, Part 1 must be completed to do Part 2 since Part 1 gives you the information you need for Part 2.

##### Part 1:
Make a TCP connection to port **23456** of the server at http://0.cloud.chals.io
Sent a properly formatted HTTP header (see the slides) to retrieve the default webpage at that location.
Receive and display the text of the HTML document the server sends as a reply

    If you receive nothing, an error message or an incomplete HTML document, your request may not have been formatted correctly

##### Part 2:
The HTML document you received in Part 1 contains the URL for another webpage and your program must extract that URL and send a second request to the same web server to retrieve that new web page.
When you receive the new page, display it on the screen.

For both parts, **submit your source code and a screenshot showing the results when you run that program.**
