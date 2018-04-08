# Project 7 - WordPress Pentesting

Time spent: **10** hours spent in total

> Objective: Find, analyze, recreate, and document **five vulnerabilities** affecting an old version of WordPress

## Pentesting Report

1. Authenticated Shortcode Tags XSS
  - [X] Summary: 
    - Vulnerability types: XSS
    - Tested in version: 4.2
    - Fixed in version: 4.7.2
  - [X] GIF Walkthrough:
    - ![1](/gif/XSS.gif?raw=true)
  - [X] Steps to recreate:
    1. As admin, write in the comment 
    ```html
    <a href = "XSS" onmouseover=alert(1) rel="nofollow">CLICK ME!</a>
    ```
    2. Hover over the link. 
  - [X] Affected source code:
    - [Vulnerability DB](https://wpvulndb.com/vulnerabilities/8186)
    - [Source Code](https://github.com/WordPress/WordPress/commit/f72b21af23da6b6d54208e5c1d65ececdaa109c8)

2. SQLI 
  - [X] Summary: 
    - Vulnerability types: SQLI 
    - Tested in version: 4.2
    - Fixed in version: 4.6
  - [X] GIF Walkthrough: 
    <!--- ![2](/gif/.gif?raw=true)-->
  - [X] Steps to recreate: 
  - [X] Affected source code:
    <!--- [Source Code]()-->


3. Persisten CSRF 
  - [X] Summary: 
    - Vulnerability types: CSRF 
    - Tested in version: 4.2
    - Fixed in version: 4.7.2
  - [X] GIF Walkthrough: 
    - ![3](/gif/CSRF.gif?raw=true)
  - [X] Steps to recreate: 
    1. As user, post a comment.
    2. Insert the following 
	```html
	<a title='x onmouseover=alert(unescape(/hello%20world/.source)) style=position:absolute;left:0;top:0;width:5000px;height:5000px  AAAAAAAAAAAA...[64 kb]..AAA'></a>
    ```
    3. The code requires an input of 64kb size of A's 
    4. When admin loads the message the code is executed 
  - [X] Affected source code:
    - CVE = CVE-2015-3440
    - [Source](https://www.exploit-db.com/exploits/36844/)	

4. User Enumeration
  - [X] Summary: 
    - Vulnerability types: 
    - Tested in version: 4.2
    - Fixed in version: 4.4
  - [X] GIF Walkthrough: 
    - ![4](/gif/UserEnumeration.gif?raw=true)
  - [X] Steps to recreate: 
    1. Go to the login page  
    2. Start trying different username & password combos
    3. WP 4.2 is giving the information whether a username is valid
    4. After learning the username you can brute force the password

5. Privilage Escalation 
  - [X] Summary: 
    - Vulnerability types: privilage escalation 
      - plugin: Extra user details	
    - Tested in version: 0.4.2
    - Fixed in version: 0.4.2.1
  - [X] GIF Walkthrough: 
    - ![4](/gif/Privilegeescalation.gif?raw=true)
  - [X] Steps to recreate: 
    1. Download the plugin "Extra user details, version 0.4.2"
      - Use plugin "Rollback" to install older version
    2. Create a new use with Author privilages
    3. Run the python script, privilage.py, with the login information
    4. After the script is done reload the page, to see the changes
  - [Source](https://www.exploit-db.com/exploits/39489/)	
## Assets

List any additional assets, such as scripts or files
- privilage.py

## Resources

- [WordPress Source Browser](https://core.trac.wordpress.org/browser/)
- [WordPress Developer Reference](https://developer.wordpress.org/reference/)

GIFs created with [Peek](https://github.com/phw/peek).

## Notes

Finding the exploit and trying to reproduce the result

## License

    Copyright [2018] [Carlos Ng]

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.# CodePath Cybersecurity - Week7

