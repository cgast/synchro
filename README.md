# synchro - synchronized presentation of layouts on various devices in sync

## Usecase 
You want to present a website design for multiple devices (we call it responsive) to a client. And you want to present a wireframe dummy on stage and simultaneously show the real designs on actual devices. This is what synchro is for.

## Setup
* You setup a wifi on your presentation computer (aka master) and connect all devices (aka slaves) to it
* on master: You start the server with python server.py running on 8080 (or use server.command)
* on all slaves: You set the browser to the servers ip on port 8080 (e.g. http://192.168.2.1:8080)
* on master: You go to the remote control page ( /rc.html , e.g. http://192.168.2.1:8080/rc.html )
* no you control the page content on the slaves from the master

## Background
This uses a simple polling mechanism (every second the current page id will be pulled from the server) and a very simple python simplehttpserver based server with a single purpose - store the current page id.
You can set the current page id on the server with /setPage/{pageId} 
All polling devices will get the id within a second by calling /getPage
You can see in index.html that the devices are switching between divs by their id. the page id on the server has to match with the div ids on the device pages.

## Finish
This is just the starting point. a boilerplate to set up your presentation. You can combine this with an axure dummy and include on every page a /setPage/ call to change the slave pages accordingly. Then you have the effect of a wireframe presentation and devices following it magically

