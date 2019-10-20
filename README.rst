Description
===========

This bot for Telegram can show you the weather.

How to use
==========

You need to find bot on the Telegram.
Write ``/start`` and bot will be launch.
After that you can use various commands to get information about the weather.

Commands
========

``/weather``

After introducing this command bot will ask you City_name and then output you today weather.

**For example**:
| input: /weather
| output: Please, tell me City_name.
| input: Tokyo
| output: 35 F, Cloudy

``/forecast``

After introducing this command bot will ask you City_name and then output you current week weather forecast.

**For example**:
| input: /forecast
| output: Please, tell me City_name.
| input: Tokyo
| output:

| 22 Jul 2019
| 61 F
| Cloudy

| 23 Jul 2019
| 59 F
| Mostly Sunny

etc.

``/amount_days``

After introducing this command bot will ask you City_name and then output you the weather forecast for nearest N days.

**For example**:
| input: /weather
| output: Please, tell me City_name.
| input: Tokyo, 2
| output:

| 22 Jul 2019
| 61 F
| Cloudy

| 23 Jul 2019
| 59 F
| Mostly Sunny
