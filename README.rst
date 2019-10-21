Description
===========

This telegram bot can show you the weather.

How to use
==========

You need to find bot on the Telegram.
Write ``/start`` and bot will will be launched.
After that you can use various commands to get information about the weather.

Commands
========

``/weather``

After this command bot will ask you about city and then output you weather for today.

**Example**:

| **input:** /weather
| **output:** Please, tell me City_name.
| **input:** Tokyo
| **output:** 35 F, Cloudy

``/forecast``

After this command bot will ask you about city and then output you weather forecast for current week.

**Example**:

| **input:** /forecast
| **output:** Please, tell me City_name.
| **input:** Tokyo
| **output:**
|
| 22 Jul 2019
| 61 F
| Cloudy
|
| 23 Jul 2019
| 59 F
| Mostly Sunny

etc.

``/amount_days``

After this command bot will ask you City_name and then output you weather forecast for nearest N days.

**Example**:

| **input:** /weather
| **output:** Please, tell me City_name.
| **input:** Tokyo, 2
| **output:**
|
| 22 Jul 2019
| 61 F
| Cloudy
|
| 23 Jul 2019
| 59 F
| Mostly Sunny
