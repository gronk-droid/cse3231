# Assignment # 5 - More TCP Programming

For this assignment, you will make a **TCP connection** to an open-relay SMTP server to send an email to my **wallen@fit.edu** email address. For this assignment, you have a choice of C/C++, Java or Python.  However, the connection to the SMTP server **must** be made using the language's socket API, **not** a specialized class library or API (like Python's smtplib or Java's JavaMail).

This SMTP server does not require authentication, so you can send your email directly from your program without including certificates or other authentication data. However, while it may take a few emails to get it working, it is not a good idea to spam me because *I will decide your final grade in this class*.

There are two parts to the assignment and each one will be graded separately, so if you only get the first part working, you will get credit for that part.  However, Part 1 must be completed to do Part 2 since Part 2 just adds content into the Part 1 email.

For **Part 1** you will make a TCP connection to an SMTP relay server at **0.cloud.chals.io**, port **32907** (*same server, different port #*) to send an email to <span style="background-color: #fbeeb8">**wallen@fit.edu**</span>. You must make a socket connection to that email relay server, not by using an email client program. Look at examples in [Networks_15](notes/Networks_15_Socket\ Programming.pdf) and [Networks_21.pdf](notes/Networks_21_Applications-part\ 2.pdf).

For **Part 2** you will include the following MIME component in the body of your email. It should display as an HTML document in the email I receive, with the format shown below, not as plain text that shows the HTML tags. **Do not** use a specialized library to create the MIME component, look at the MIME email example in the [Networks_22](notes/Networks_23_Cryptography-part\ 1.pdf) slides. Note, if you don't know HTML, the code is in the second example below, you just have to figure out how to include that in the body of the email you send to me.

**The email I receive should look like this** (not including the border):
- - -
### Hello,
- I am your TRACKS
- This is my Assignment # 5
- - -
**Not like this** (ignore the border here too):
- - -
```html
<h3>Hello,</h3>
<ul>
<li>I am <em>your TRACKS</em></li>
<li>This is my Assignment # 5</li>
<ul>
```
- - -
Make sure that you have **included your TRACKS account** in the HTML code so that I can give you credit for the assignment.

For both parts you will just **submit your source code**. The email I receive will be proof that it worked and I will email you when I receive your email.
