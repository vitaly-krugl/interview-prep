Here are the links to some of my open-source work on github under github handle "vitaly-krugl". This includes Numenta projects as well as external open-source projects (external citations are at the bottom)

=========NUMENTA PROJECTS==========

Please note that Numenta open-sourced our code in June of 2015, and all commits were squashed, so much of the work appears to originate from "Numenta Team". I will call out some of the modules that I "owned" or contributed to heavily:


NUPIC.CORE:

https://github.com/numenta/nupic.core/pull/1285 : Fixed critical issue with the integration of capnproto serialization library into nupic.core project, including new tests.


BUILD SYSTEM:

https://github.com/numenta/nupic.core/blob/master/ci/build-and-test-nupic-bindings.sh : work sample on build/test script; I originated, others contributed later.

https://github.com/numenta/manylinux : Based on my initiative, researched, convinced team, and created a fork of the manylinux python wheel-building project, and adapted it to support the capnproto library build that relies on newer system APIs (based on centos-6 vs. centos-5).

https://github.com/numenta/nupic.core/pull/885 : Major refactoring of nupic.core's build on Windows, Linux, and OS X that restored ability to build external components from source code. The legacy build included many binary components that were pre-compiled by contractor without capability to rebuild them from source or deal with ABI issues.

https://github.com/numenta/nupic.core/pull/1039 : Fixed symbol preemption issues in Numenta's python extension.


SERVICES:

https://github.com/numenta/numenta-apps/blob/master/unicorn/py/unicorn_backend/model_runner_2.py : A very simple prototype of a back-end process that I created for the demo application project "unicorn".

https://github.com/numenta/numenta-apps/tree/master/htmengine/htmengine/model_swapper : This package is responsible for scheduling many models to run within the limitations of the machine's resources; it also implements the data path API on top of AMQP. The core scheduling logic is in https://github.com/numenta/numenta-apps/blob/master/htmengine/htmengine/model_swapper/swap_controller.py. I originated almost all of the code in this package.

https://github.com/numenta/numenta-apps/blob/master/taurus_metric_collectors/taurus_metric_collectors/twitterdirect/twitter_direct_agent.py : service that streams and aggregates twitter data feed on companies of interest. Most of the code under twitterdirect/ is mine.


MONITORS:

https://github.com/numenta/numenta-apps/blob/master/htmengine/htmengine/monitors/rmq_metric_collector_agent.py : collects/aggregates RabbitMQ statistics for analysis, failure detection.

https://github.com/numenta/numenta-apps/blob/master/taurus_metric_collectors/taurus_metric_collectors/xignite/check_company_symbols.py : detects when stock symbols of interest become invalid (e.g., are renamed, obsoleted, incorrectly configured, etc.) and generates an email that results is subsequently processed into a JIRA issue.


UTILITIES:

Error-handling decorators: https://github.com/numenta/numenta-apps/blob/master/nta.utils/nta/utils/error_handling.py

Logging configuration utilities: https://github.com/numenta/numenta-apps/blob/master/nta.utils/nta/utils/logging_support_raw.py


INTEGRATION TESTS:

https://github.com/numenta/numenta-apps/blob/master/htmengine/tests/integration/model_swapper/model_runner_test.py


UNIT TESTS:

https://github.com/numenta/numenta-apps/blob/master/htmengine/tests/unit/model_swapper/model_scheduler_service_test.py
https://github.com/numenta/numenta-apps/blob/master/htmengine/tests/unit/model_swapper/slot_agent_test.py


EXAMPLE OF CODE CLEANUP/REFACTORING OF EXISTING CODE: https://github.com/numenta/nupic/pull/2432
    

========= EXTERNAL OPEN-SOURCE CONTRIBUTIONS ============

* https://github.com/pika/pika : pika is a popular python AMQP client. I completely re-wrote the BlockingConnection adapter (https://github.com/pika/pika/blame/f72b58f5181f48b362a86a2fa1226ec88ddf400c/pika/adapters/blocking_connection.py), which remedied many systemic bugs in the legacy version and resulted in upwards of 40X performance improvement. 

I also made fixes to other parts of the code in pika that improved stability, performed code reviews, provided guidance to other contributors, and implemented a complete acceptance test suite for the blocking adapter (https://github.com/pika/pika/blame/f72b58f5181f48b362a86a2fa1226ec88ddf400c/tests/acceptance/blocking_adapter_test.py)

* https://github.com/agoragames/haigha : haigha is another python AMQP client that we switched to recently due to licensing incompatibilities with pika at the time that numenta's code was being open-sourced. 

Haigha was missing support for several core protocol features that we needed, such as broker-initiated Basic.Cancel and Basic.Return. Basic.Return PR: https://github.com/agoragames/haigha/pull/73. Basic.Cancel PR: https://github.com/agoragames/haigha/pull/82. 

Also performed code reviews and provided guidance to other contributor(s): e.g., https://github.com/agoragames/haigha/pull/69.


============ OLDER WORK IN C/C++ ON WEBOS AT PALM 6+ YEARS AGO ===========
* https://github.com/openwebos/libpalmsocket : I took over libpalmsocket from a team of engineers. The open/TLS communications abstraction was in very bad shape (systemic bugs, design, and performance issues). I re-implemented it quickly under severe development schedule pressure. I also identified and worked around several issues in OpenSSL.  The new implementation makes use of the Hierarchical State Machine Engine that I also developed at Palm.

* https://github.com/openwebos/pmstatemachineengine: Implementation of the Hierarchical State Machine Engine based on Miro Samek's book on the subject.