Here are the links to some of my open-source work on github under github handle "vitaly-krugl". This includes Numenta projects as well as external open-source projects (more external citations are at the bottom)

# RECENT OSS CONTRIBUTIONS

In https://github.com/pika:
* Pull Request: [Implement add_callback_threadsafe in all connection adapters](https://github.com/pika/pika/pull/956)
* Pull Request: [Use minheap as timeout container and fix collision of multiple SelectConnection timeouts with same deadline and callback](https://github.com/pika/pika/pull/947)
* Pull Request: [Implemented BlockingConnection acceptance tests for the consume generator encountering server's Basic.Cancel](https://github.com/pika/pika/pull/962)
* Code Review: [BlockingConnection tune for heartbeat=0 properly](https://github.com/pika/pika/pull/966)
* Code Review: [Rename no_ack => auto_ack to match Java and .NET clients](https://github.com/pika/pika/pull/955)
* Code Review: [Ensure blocked Channel.Close methods are processed](https://github.com/pika/pika/pull/957)
* Root-cause:  [Blocking channel Publish nevert completes](https://github.com/pika/pika/issues/708#issuecomment-370105566)


# NUMENTA PROJECTS

Please note that Numenta open-sourced our code in June of 2015, and all commits were squashed, so much of the work appears to originate from "Numenta Team". Below, I reference some of the modules that I owned or contributed to heavily:


## NUPIC.CORE

[Fixed critical issue](https://github.com/numenta/nupic.core/pull/1285) with the integration of capnproto serialization library into nupic.core project, including new tests.


## BUILD SYSTEM

[Build/test script work sample](https://github.com/numenta/nupic.core/blob/0e2f5ac8554fc1addcdd45d4a36b33f7e839b3e2/ci/build-and-test-nupic-bindings.sh); I originated, others contributed later.

[Manylinux python wheel build using Docker](https://github.com/numenta/manylinux/tree/da197b08d56b057e3e3a4b30c543b316e7a1a78a) : Based on my initiative, researched, convinced team, and created a fork of the manylinux python wheel-building docker-based project, and adapted it to support the capnproto library build that relies on newer system APIs (based on centos-6 vs. centos-5).

[Major refactoring of nupic.core's build on Windows, Linux, and OS X](https://github.com/numenta/nupic.core/pull/885) that restored ability to build external components from source code. The legacy build included many binary components that were pre-compiled by contractor without capability to rebuild them from source or deal with ABI issues.

[Fixed symbol preemption issues](https://github.com/numenta/nupic.core/pull/1039) in Numenta's python extension.


## SERVICES

[Backend service prototype](https://github.com/numenta/numenta-apps/blob/d175229311046599fbe206e7a0a37e8d209e6f7a/unicorn/py/unicorn_backend/model_runner_2.py) : A very simple prototype of a back-end process that I created for the demo application project "unicorn".

[ML model execution scheduler](https://github.com/numenta/numenta-apps/tree/865680bbeaf9ba56e29f468e70ce4dd1aeec4a9c/htmengine/htmengine/model_swapper) This package is responsible for scheduling many models to run within the limitations of the machine's resources; it also implements the data path API on top of AMQP. The core scheduling logic [called SwapController is here](https://github.com/numenta/numenta-apps/blob/865680bbeaf9ba56e29f468e70ce4dd1aeec4a9c/htmengine/htmengine/model_swapper/swap_controller.py). I originated almost all of the code in this package.

[Twitter data streaming and aggregation service](https://github.com/numenta/numenta-apps/blob/81f6e9bb4122c47fbbf6c208c795915027fac473/taurus.metric_collectors/taurus/metric_collectors/twitterdirect/twitter_direct_agent.py) that streams and aggregates twitter data feed on companies of interest. Most of the code under twitterdirect/ is mine. Note that most commit history was compromised when the company open-sourced its projects.


## MONITORS

https://github.com/numenta/numenta-apps/blob/f79f919e80747fae2e35e6d679f2f0633fe48789/htmengine/htmengine/monitors/rmq_metric_collector_agent.py : collects/aggregates RabbitMQ statistics for analysis, failure detection.

[Stock symbol validation service](https://github.com/numenta/numenta-apps/blob/81f6e9bb4122c47fbbf6c208c795915027fac473/taurus.metric_collectors/taurus/metric_collectors/xignite/check_company_symbols.py) : detects when stock symbols of interest become invalid (e.g., are renamed, obsoleted, incorrectly configured, etc.) and generates an email that results is subsequently processed into a JIRA issue.


## UTILITIES

[Error-handling decorators](https://github.com/numenta/numenta-apps/blob/10b20f473d1bf5949b9cc96050874ce63163e515/nta.utils/nta/utils/error_handling.py)

[Logging configuration utilities](https://github.com/numenta/numenta-apps/blob/d9d7c7aec3149059a6ea436ec4e3166521d264f6/nta.utils/nta/utils/logging_support_raw.py)


## INTEGRATION TESTS

[Model Runner integration tests[(https://github.com/numenta/numenta-apps/commits/2392061961340b24430fb39e8b6603e910bef948/htmengine/tests/integration/model_swapper/model_runner_test.py)


## UNIT TESTS

[Unit tests for Model Scheduler service](https://github.com/numenta/numenta-apps/blob/1ff572a21a5c27fd290822e572ce33f42e1ee19e/htmengine/tests/unit/model_swapper/model_scheduler_service_test.py)
[Unit tests for SlogAgent class used by Model Scheduler](https://github.com/numenta/numenta-apps/blob/1ff572a21a5c27fd290822e572ce33f42e1ee19e/htmengine/tests/unit/model_swapper/slot_agent_test.py)


## EXAMPLE OF CODE CLEANUP/REFACTORING OF EXISTING CODE

[Refactor Input Model Record Encoder](https://github.com/numenta/nupic/pull/2432)
    

# EXTERNAL OPEN-SOURCE CONTRIBUTIONS

https://github.com/pika/pika : pika is a popular python AMQP client.

* I completely re-wrote the [BlockingConnection adapter](https://github.com/pika/pika/blame/f72b58f5181f48b362a86a2fa1226ec88ddf400c/pika/adapters/blocking_connection.py), which remedied many systemic bugs in the legacy version and resulted in upwards of 40X performance improvement. 

* I also made fixes to other parts of the code in pika that improved stability, performed code reviews, provided guidance to other contributors, and implemented a [complete acceptance test suite for the blocking adapter](https://github.com/pika/pika/blame/f72b58f5181f48b362a86a2fa1226ec88ddf400c/tests/acceptance/blocking_adapter_test.py)

https://github.com/agoragames/haigha : haigha is another python AMQP client that we switched to recently due to licensing incompatibilities with pika at the time that numenta's code was being open-sourced. 

* Haigha was missing support for several core protocol features that we needed, such as broker-initiated Basic.Cancel and Basic.Return. My Basic.Return PR: https://github.com/agoragames/haigha/pull/73. My Basic.Cancel PR: https://github.com/agoragames/haigha/pull/82. 

* Also performed code reviews and provided guidance to other contributor(s): e.g., https://github.com/agoragames/haigha/pull/69.


# OLDER WORK IN C/C++ ON WEBOS AT PALM 7+ YEARS AGO
* [I took over libpalmsocket](https://github.com/openwebos/libpalmsocket/tree/9533a7c46f8d35e69112a8c5e671532d059b2e8d) from a team of engineers. The open/TLS communications abstraction was in very bad shape (systemic bugs, crashes, design, and performance issues). I re-implemented it quickly under severe development schedule pressure. I also identified and worked around several issues in OpenSSL.  The new implementation makes use of the Hierarchical State Machine Engine that I also developed at Palm.

* [My implementation of the Hierarchical State Machine Engine](https://github.com/openwebos/pmstatemachineengine/tree/34f1a4fa6022259e0b8dc3e8b683782e28659186) based on Miro Samek's book on the subject.
