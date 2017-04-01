# SeleniumFramework
This is a loose example of a python-selenium script under POM model that is perfectly scalable . 
The current implementation is for google driver with remote webdriver
Script will login to gmail and send a mail to the specified email address. To use the script populate the remaning fields in the config file.



The framework expects to tackle two major issue with selenium automation: 
1. Scalability 
    Any selenium script could be easily broken when the developers deicdes on one design change . The problem in using the in built selenium methods like find_elements_by_xpath() directly in scripts is that we would need to go and edit each and every find element in the script. Instead this example makes use of a custom made method which will auto detect which locator (say xpath, id , name ) you are  using and find the element for you. This makes sure that you dont need to re edit the script, instead just edit the configuration file that holds the locator for each element that had changed. This helps you to preserve the same script and use it again 
    
2. Wait for element
  Another problem with selenium automation is the need to wait for element. We could use a time.sleep() but that is not a perfect idea as the script sleep for the given time even if element appeared before the specified time. This framework removes this problem by inherently  stopping the script until the specific element is found and resumes automatically. This makes sure our script is dynamic and is as fast as possible . Refer wait_for_element() method to find out how to use this

