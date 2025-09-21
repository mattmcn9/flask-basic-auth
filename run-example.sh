docker run -e USERNAME=user -e PASSWORD=Password! -e PORT=9090 -v $PWD:/data 
-p 9090:9090 flask-file-server:latest
