==================
Skyline API Server
==================

English \| `简体中文 <./README-zh_CN.rst>`__ \| `한국어 <./README-ko_KR.rst>`__

Skyline is an OpenStack dashboard optimized by UI and UE, support
OpenStack Train+. It has a modern technology stack and ecology, is
easier for developers to maintain and operate by users, and has higher
concurrency performance.

Skyline's mascot is the nine-color deer. The nine-color deer comes from
Dunhuang mural “the nine-color king deer”, whose moral is Buddhist
cause-effect and gratefulness, which is consistent with 99cloud's
philosophy of embracing and feedback community since its inception. We
also hope Skyline can keep light, elegant and powerful as the nine-color
deer, to provide a better dashboard for the openstack community and
users.

|image0|

**Table of contents**

-  `Skyline API Server <#skyline-api-server>`__

   -  `Resources <#resources>`__
   -  `Quick Start <#quick-start>`__

      -  `Prerequisites <#prerequisites>`__
      -  `Configure <#configure>`__
      -  `Deployment with Sqlite <#deployment-with-sqlite>`__
      -  `Deployment with MariaDB <#deployment-with-mariadb>`__
      -  `Test Access <#test-access>`__

   -  `Develop Skyline-apiserver <#develop-skyline-apiserver>`__

      -  `Dependent tools <#dependent-tools>`__
      -  `Install & Run <#install--run>`__

   -  `Devstack Integration <#devstack-integration>`__
   -  `Kolla Ansible Deployment <#kolla-ansible-deployment>`__

Resources
---------

-  `Developer Docs <https://docs.openstack.org/skyline-apiserver/latest/>`__
-  `Release notes <https://docs.openstack.org/releasenotes/skyline-apiserver/>`__
-  `Wiki <https://wiki.openstack.org/wiki/Skyline>`__
-  `Bug Tracker <https://launchpad.net/skyline-apiserver>`__

Container Environment Quick Start
----------------------------------

Prerequisites
~~~~~~~~~~~~~

-  An OpenStack environment that runs at least core components and can
   access OpenStack components through Keystone endpoints
-  A Linux server with container engine
   (`docker <https://docs.docker.com/engine/install/>`__ or
   `podman <https://podman.io/getting-started/installation>`__)
   installed

Configure
~~~~~~~~~

1. Edit the ``/etc/skyline/skyline.yaml`` file in linux server

   You can refer to the `sample file <etc/skyline.yaml.sample>`__, and
   modify the following parameters according to the actual environment

   -  database_url
   -  keystone_url
   -  default_region
   -  interface_type
   -  system_project_domain
   -  system_project
   -  system_user_domain
   -  system_user_name
   -  system_user_password

   Replace SKYLINE_DBPASS, DB_SERVER, KEYSTONE_SERVER and SKYLINE_SERVICE_PASSWORD with a correct value.

   .. code:: vim

      default:
         database_url: mysql://skyline:SKYLINE_DBPASS@DB_SERVER:3306/skyline
         debug: true
         log_dir: /var/log/skyline
      openstack:
         keystone_url: http://KEYSTONE_SERVER:5000/v3/
         system_user_password: SKYLINE_SERVICE_PASSWORD

2. create database and add role

   Use the database access client to connect to the database server as the root user:
   (If openstack is already using the database, you can use it as it is.)

   .. code:: mysql

      create database skyline DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;
      create user skyline@localhost identified by 'skyline_pass';
      grant all privileges on skyline.* to 'skyline'@localhost;
      create user skyline@'%' identified by 'skyline_pass';
      grant all privileges on skyline.* to 'skyline'@'%';
      FLUSH PRIVILEGES;
      exit

   Source the admin credentials to gain access to admin-only CLI commands:

   .. code:: bash

      . admin-openrc

   To create the service credentials, complete these steps:

   .. code:: bash

      openstack user create --domain default --password-prompt skyline

      User Password:
      Repeat User Password:
      +---------------------+----------------------------------+
      | Field               | Value                            |
      +---------------------+----------------------------------+
      | domain_id           | default                          |
      | enabled             | True                             |
      | id                  | 1qaz2wsx3edc4rfv5tgb6yhn7ujm8ikl |
      | name                | skyline                          |
      | options             | {}                               |
      | password_expires_at | None                             |
      +---------------------+----------------------------------+

   Add the admin role to the skyline user:

   .. code:: bash

      openstack role add --project service --user skyline admin

3. Run the skyline_bootstrap container to bootstrap

   .. code:: bash

      rm -rf /tmp/skyline && mkdir /tmp/skyline && mkdir /var/log/skyline

      docker run -d --name skyline_bootstrap -e KOLLA_BOOTSTRAP="" -v /var/log/skyline:/var/log/skyline -v /etc/skyline/skyline.yaml:/etc/skyline/skyline.yaml -v /tmp/skyline:/tmp --net=host 99cloud/skyline:latest

      # Check bootstrap is normal `exit 0`
      docker logs skyline_bootstrap
   

   If you see the following message, it means that the bootstrap server is successful:

   .. code:: bash

      + echo '/usr/local/bin/gunicorn -c /etc/skyline/gunicorn.py skyline_apiserver.main:app'
      + mapfile -t CMD
      ++ xargs -n 1
      ++ tail /run_command
      + [[ -n 0 ]]
      + cd /skyline-apiserver/
      + make db_sync
      alembic -c skyline_apiserver/db/alembic/alembic.ini upgrade head
      2022-08-19 07:49:16.004 | INFO     | alembic.runtime.migration:__init__:204 - Context impl MySQLImpl.
      2022-08-19 07:49:16.005 | INFO     | alembic.runtime.migration:__init__:207 - Will assume non-transactional DDL.
      + exit 0

4. Run the skyline service after bootstrap is complete

   .. code:: bash

      docker rm -f skyline_bootstrap

   If you need to modify skyline port, add ``-e LISTEN_ADDRESS=<ip:port>`` in the following command

   ``LISTEN_ADDRESS`` defaults to ``0.0.0.0:9999``

   If you need to modify the policy rules of a service, add ``-v /etc/skyline/policy:/etc/skyline/policy`` in the following command

   Rename the service policy yaml file to ``<service_name>_policy.yaml``, and place it in ``/etc/skyline/policy`` folder

   .. code:: bash

      docker run -d --name skyline --restart=always -v /var/log/skyline:/var/log/skyline -v /etc/skyline/skyline.yaml:/etc/skyline/skyline.yaml -v /tmp/skyline:/tmp --net=host 99cloud/skyline:latest


Non-container Skyline-apiserver Quick Start
-------------------------------------------

If you want to install skyline without container env. follow this guide.
The order may be a little different from the above ``container Quick Start``.

Prerequisites
~~~~~~~~~~~~~

-  An OpenStack environment that runs at least core components and can
   access OpenStack components through Keystone endpoints
-  Ubuntu server where nginx can be installed. - [other os require confirm.]
   (using Apache version is progress in the develop.)

Configure
~~~~~~~~~

1. create database and add role

   Use the database access client to connect to the database server as the root user:
   (If openstack is already using the database, you can use it as it is.)

   .. code:: mysql

      create database skyline DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;
      create user skyline@localhost identified by 'skyline_pass';
      grant all privileges on skyline.* to 'skyline'@localhost;
      create user skyline@'%' identified by 'skyline_pass';
      grant all privileges on skyline.* to 'skyline'@'%';
      FLUSH PRIVILEGES;
      exit

   Source the admin credentials to gain access to admin-only CLI commands:

   .. code:: bash

      . admin-openrc

   To create the service credentials, complete these steps:

   .. code:: bash

      openstack user create --domain default --password-prompt skyline

      User Password:
      Repeat User Password:
      +---------------------+----------------------------------+
      | Field               | Value                            |
      +---------------------+----------------------------------+
      | domain_id           | default                          |
      | enabled             | True                             |
      | id                  | 1qaz2wsx3edc4rfv5tgb6yhn7ujm8ikl |
      | name                | skyline                          |
      | options             | {}                               |
      | password_expires_at | None                             |
      +---------------------+----------------------------------+

   Add the admin role to the skyline user:

   .. code:: bash

      openstack role add --project service --user skyline admin

2. apt packages install

   .. code:: bash

      #apt package install
      apt install python3-dev make gcc

      #if using ssl
      apt install ssl-cert


3. git clone and checkout

   .. code:: bash

      git clone https://opendev.org/openstack/skyline-apiserver.git
      cd skyline-apiserver
      git checkout master # support stable/zed, stable/2023.1, stable/2023.2 

   .. code:: bash
      
      #python package install
      pip3 install skyline-apiserver/

4. sample file copy and setting

   copy file

   .. code:: bash
      
      #gunicorn
      cp skyline-apiserver/etc/gunicorn.py /etc/skyline/gunicorn.py
      #skyline config file
      cp skyline-apiserver/etc/skyline.yaml.sample /etc/skyline/skyline.yaml


   Edit the ``/etc/skyline/skyline.yaml`` file

   You can refer to the `sample file <etc/skyline.yaml.sample>`__, and
   modify the following parameters according to the actual environment

   -  database_url
   -  keystone_url
   -  default_region
   -  interface_type
   -  system_project_domain
   -  system_project
   -  system_user_domain
   -  system_user_name
   -  system_user_password

   Replace SKYLINE_DBPASS, DB_SERVER, KEYSTONE_SERVER and SKYLINE_SERVICE_PASSWORD with a correct value.

   .. code:: vim

      default:
         database_url: mysql://skyline:SKYLINE_DBPASS@DB_SERVER:3306/skyline
         debug: true
         log_dir: /var/log/skyline
      openstack:
         keystone_url: http://KEYSTONE_SERVER:5000/v3/ 
         #keystone_url: http://KEYSTONE_SERVER:5000/identity
         system_user_password: SKYLINE_SERVICE_PASSWORD

5. db sync

   .. code:: bash

      make db_sync

6. deamon setting

   Edit the ``vim /etc/systemd/system/skyline-apiserver.service`` file

   .. code:: vim
      [Unit]
      Description=Skyline APIServer

      [Service]
      Type=simple
      ExecStart=/usr/local/bin/gunicorn -c /etc/skyline/gunicorn.py skyline_apiserver.main:app
      LimitNOFILE=32768

      [Install]
      WantedBy=multi-user.target

   daemon start

   .. code:: bash
      systemctl daemon-reload
      systemctl enable skyline-apiserver
      systemctl start skyline-apiserver
      systemctl status skyline-apiserver

API Doc
~~~~~~~~~

You can visit the API doc ``https://<ip_address>:9999/api/openstack/skyline/docs``

Test Access
~~~~~~~~~~~

You can now access the dashboard: ``https://<ip_address>:9999``

openstack official docs
~~~~~~~~~~~~~~~~~~~~~~~~

https://docs.openstack.org/skyline-apiserver/latest/install/docker-install-ubuntu.html



   
Develop Skyline-apiserver
-------------------------

**Support Linux & Mac OS (Recommend Linux OS) (Because uvloop & cython)**

Dependent tools
~~~~~~~~~~~~~~~

Use the new feature Context Variables of python37 & uvloop(0.15.0+
requires python37). Considering that most systems do not support
python37, we choose to support python38 at least.

-  make >= 3.82
-  python >= 3.8
-  node >= 10.22.0 (Optional if you only develop with apiserver)
-  yarn >= 1.22.4 (Optional if you only develop with apiserver)

Install & Run
~~~~~~~~~~~~~

1. Installing dependency packages

   .. code:: bash

      tox -e venv

2. Set skyline.yaml config file

   .. code:: bash

      cp etc/skyline.yaml.sample etc/skyline.yaml
      export OS_CONFIG_DIR=$(pwd)/etc

   Maybe you should change the params with your real environment as
   followed:

   .. code:: yaml

      - database_url
      - keystone_url
      - default_region
      - interface_type
      - system_project_domain
      - system_project
      - system_user_domain
      - system_user_name
      - system_user_password

   If you set such as ``sqlite:////tmp/skyline.db`` for
   ``database_url`` , just do as followed. If you set such as
   ``mysql://root:root@localhost:3306/skyline`` for ``database_url``
   , you should refer to steps ``1`` and ``2`` of the chapter
   ``Deployment with MariaDB`` at first.

3. Init skyline database

   .. code:: bash

      source .tox/venv/bin/activate
      make db_sync
      deactivate

4. Run skyline-apiserver

   .. code:: console

      $ source .tox/venv/bin/activate
      $ uvicorn --reload --reload-dir skyline_apiserver --port 28000 --log-level debug skyline_apiserver.main:app

      INFO:     Uvicorn running on http://127.0.0.1:28000 (Press CTRL+C to quit)
      INFO:     Started reloader process [154033] using statreload
      INFO:     Started server process [154037]
      INFO:     Waiting for application startup.
      INFO:     Application startup complete.

   You can now access the online API documentation:
   ``http://127.0.0.1:28000/docs``.

   Or, you can launch debugger with ``.vscode/lauch.json`` with vscode.

5. Build Image

   .. code:: bash

      make build

Devstack Integration
--------------------

`Fast integration with Devstack to build an
environment. <../devstack/README.rst>`__

Kolla Ansible Deployment
------------------------

`Kolla Ansible to build an environment. <../kolla/README.md>`__

|image1|

.. |image0| image:: ../doc/source/images/logo/OpenStack_Project_Skyline_horizontal.png
.. |image1| image:: ../doc/source/images/logo/nine-color-deer-64.png

FAQ
---

1. Policy

   Q: Why common user could login, but could list the nova servers?
      `Bug #2049807 <https://bugs.launchpad.net/skyline-apiserver/+bug/2049807>`_

   ::

      Symptom:
      -----------------------------------
      1. Login Horizon with common user A, list servers OK.
      2. Login Skyline with same common user A, could list the nova servers, F12 show no http requests sent from network, however webpage show 401, do not allow to list servers

      Root Cause Analysis:
      -----------------------------------
      1. Horizon don't know whether a user could do an action at a resource or not. It simply pass request to recording service, & service (Nova) do the check by its policy file. So it works.
      2. Skyline check the action by itself, with /policy API. If you do not configure it, the default value follows community, like: https://docs.openstack.org/nova/2023.2/configuration/sample-policy.html

      How to fix:
      -----------------------------------
      1. By default, list servers need "project_reader_api": "role:reader and project_id:%(project_id)s"
      2. You should config your customized role, for example: member, _member_, projectAdmin, etc, create implied reader role. "openstack implied role create --implied-role member projectAdmin", or "openstack implied role create --implied-role reader _member_"

      # openstack implied role list
      +----------------------------------+-----------------+----------------------------------+-------------------+
      | Prior Role ID | Prior Role Name | Implied Role ID | Implied Role Name |
      +----------------------------------+-----------------+----------------------------------+-------------------+
      | fe21c5a0d17149c2a7b02bf39154d110 | admin | 4376fc38ba6a44e794671af0a9c60ef5 | member |
      | 4376fc38ba6a44e794671af0a9c60ef5 | member | e081e01b7a4345bc85f8d3210b95362d | reader |
      | bee8fa36149e434ebb69b61d12113031 | projectAdmin | 4376fc38ba6a44e794671af0a9c60ef5 | member |
      | 77cec9fc7e764bd4bf60581869c048de | _member_ | e081e01b7a4345bc85f8d3210b95362d | reader |
      +----------------------------------+-----------------+----------------------------------+-------------------+
