#Syrius Image
The creation and handling of this image is almost the same as in the previous chapter, with the following differences

##What's different
The Syrius Software, configuration files and logs are not part of the image. They are mounted from the host to the
container at runtime.

The image becomes smaller
Configuration can be changed and the containers restarted with the new config - without building a new image.
Logfiles are persisted.

