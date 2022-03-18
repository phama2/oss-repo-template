# Lab 8
### Checkpoint 1
![image](https://user-images.githubusercontent.com/70230763/159038007-0eb68132-ee26-4ffe-bfd2-385a146295e6.png)
### Checkpoint 2
#### Find the Nightly and Experimental sections and look at some of the submissions. How can you see what tests were run for a particular submission?
Click on the build and then scroll down to the bottom to view the tests summary section. Click the "View Tests Summary". On this new page, it should show all of the tests run along with which passed and failed. Also, you can click on the name of the test to show additional details.
#### Find a submission with errors. Can you see what the error condition was? How does this help you debug the failure?
I couldn't find any submissions with errors, but I assume its the same process as the question above. However, instead of the tests section, you would look at the build section and click the "View Errors Summary". From this page, you can probably see what the error condition is. This aids in debugging failure since it directly points out the point of failure so you can go back and fix it.
#### Find a system that is close to your specific configuration in the Nightly, Nightly Expected or one of the Masters sections. How clean is the dashboard? Are there any errors that you need to be concerned with?
The closest to my specification is "cmake-windows_vs2022_x64" in the master section, since I'm running Windows x64 and used Visual Studio 2022 to compile. The dashboard is clean with no errors and passing all tests. No errors at all that I 
![image](https://user-images.githubusercontent.com/70230763/159045389-0a71b416-72fa-4947-bd4c-d75355bbe0a9.png)
![image](https://user-images.githubusercontent.com/70230763/159045468-d22cc245-6f94-422c-b4a6-58026df273b9.png)
![image](https://user-images.githubusercontent.com/70230763/159045305-760575ff-39b2-4f26-ae7c-86a021c3257a.png)
No errors :).
### Checkpoint 3
Error: \
![image](https://user-images.githubusercontent.com/70230763/159049096-44e2bfcc-f4c5-427b-b61f-9b13951ee00b.png)
![image](https://user-images.githubusercontent.com/70230763/159050592-1195ef50-c829-46f9-bcd6-f5c02a3cca10.png)
Fixed: \
![image](https://user-images.githubusercontent.com/70230763/159052996-0b462d7f-1e9d-4186-96ad-699c8aa14bf6.png)
### Checkpoint 4
