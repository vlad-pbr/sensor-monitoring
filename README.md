# Sensor Data Monitoring and Alerting System

A Python-based service to monitor sensor data.

## Task

The system should be able to read sensor data from various types of sensors (temperature, humidity, pressure, etc.),
validate the data based on configured rules, and alert an alert service if invalid data is detected. The alert service
should notify on invalid data.

## Implementation

Each sensor is an iterable class that yields sensor values in a predefined range at a predefined interval. Separate
classes called `Validator`s validate values of a specific sensor by inspecting yielded values and checking whether
they are in a valid range. Multiple validators can be assigned a single sensor, but only one sensor can be assigned
to a single validator. Each time a sensor value is deemed as not valid by a validator, an `Alert` is inserted into
an alert queue which is shared between all validators. A separate alerting task will handle each alert coming from
the queue and redistribute it to the configured alerting channels (such as E-Mail).

## Assumptions

- Usage of third-party libraries is allowed. Only select, widely acknowledged and trusted libraries were used.
  The reason behind the decision is to provide a solution to some of the problems irrelevant to the task. For example,
  `pydantic` was chosen to load and validate configuration so no irrelevant bugs would occur as a result of faulty
  code that would otherwise have to be manually implemented.
- Real sensors would be separate processes that yield same values to all "subscribed" validators, but for the sake
  of simplicity of the exercise, each sensor is an entirely separate instance.
- Sensors can have many validators, but each validator can only validate a single type of sensor. The assumption here
  is that there is a set relationship between a validator and a sensor. In our case, we simply validate values in
  range, but in the real world other factors would come into play. Current implementation allows to have multiple
  validators validating various ranges of the same sensor, but makes it easy to expand on validation logic in the
  future.

## Usage

This app is written in Python 3.11. Project dependencies are managed by `poetry`, but a corresponding
`requirements.txt` exists as well. In order to run the app, install the relevant requirements from `requirements.txt`
(preferably in a virtual environment), then start the app by running `python .`.

The default configuration will send sensor alerts as e-mail to a local SMTP server which can be started using
`python -m smtpd -c DebuggingServer -n localhost:1025`.

Tests can be executed via `python -m unittest discover -s test`
