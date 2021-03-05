# InternetOfThings

## On Jetson
### Run mosquitto on Jetson
`docker run --name mosquitto --network hw03 -p 1883:1883 -ti alpine sh`

`apk update && apk add mosquitto`

`/usr/sbin/mosquitto -v`

## Run detector 
`docker run --privileged --runtime nvidia --rm --network hw03 -v /home/wangjoa/InternetOfThings:/data -e DISPLAY -v /tmp:/tmp -ti --name detctorContainer detector bash` 

`cd data`

`python3 detector.py`


### Run forwarder 
`docker run --rm --network hw03 -v /home/wangjoa/InternetOfThings:/data -ti --name forwarderContainer detector bash `

`cd data`

`python3 forwarder.py`

### Run mosquitto on AWS
`docker run --name mosquitto --network hw03 -p 1883:1883 -ti alpine sh`

`apk update && apk add mosquitto`

`/usr/sbin/mosquitto -v`

### Run processor on AWS
`docker run --privileged  --rm --network hw03 -v /home/ubuntu/InternetOfThings:/data -e DISPLAY -v /mnt/mountpoint/:/mnt/mountpoint/ -ti --name processorContainer processor bash`

`cd data`

`python3 processor.py`
