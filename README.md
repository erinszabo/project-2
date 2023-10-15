
# UO CS 322 - Project 2  

## Erin Szabo
#### Fall 2023
### eszabo@uoregon.edu


The purpose of this project is to get started with Docker and Flask. It has the same functionality as Project 1, except the heavy lifting is done by Docker using a Flask app.

## Steps

-  cd into `web/` 
-  Build the simple flask app image using
    ```
    docker build -t some-image-name .
    ```
- Run the container using

  ```
  docker run -d -p 5001:5000 some-image-name
  ```
 - Launch `http://hostname:5001` using your web browser 

    - if just at the port, the output is just "UOCIS docker demo!"
    - if a request contains the name of a valid file in the DOCROOT, then a status of 200 'OK' is transmitted along with the specified page with associated style if applicable. 
    - if a request contains a file that does not exist in the DOCROOT, then a status of 404 'file not found' is transmitted with my 404.html file.
    - if a request contains the illegal charactars ".." or "~", then a status of 403 'forbidden' is transmitted with my 403.html file.

- When done, stop the container using
    ```
    docker stop <123>
    ```
    but replace <123> with the first 3 characters of the running container ID


## Original Authors

Michal Young, Ram Durairajan. Updated by Ali Hassani.
