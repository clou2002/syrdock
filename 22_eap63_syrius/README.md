#Syrius Image
Before you can build this image, make sure you have built to JBoss base image described in the previous steps.
You must extract an official Syrius tar to 22_eap63_syrius/syrius/software.

##Build the image
```
cd 22_eap63_syrius
./build.sh
```

##Run Syrius
Make sure you have the credentials of your running Syrius database ready. The database schema must have the exact same release as the Syrius software you want to run.
